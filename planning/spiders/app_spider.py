import scrapy
from scrapy.http import FormRequest

class Case(scrapy.Item):
    address = scrapy.Field()
    proposal = scrapy.Field()
    decision = scrapy.Field()
    constraints = scrapy.Field()

class ApplicationSpider(scrapy.Spider):
    name = "app"
    start_urls = [
        'http://public-access.lbhf.gov.uk/online-applications/search.do?action=simple&searchType=Application',
    ]
    
    def parse(self,response):
        yield FormRequest.from_response(response, formdata = {"searchCriteria.simpleSearchString":"oxberry"}, callback=self.parseResultsPage)
    
    def parseResultsPage(self,response):
        for result in response.css("li.searchresult"):
            summaryPage = response.urljoin(result.css("a::attr(href)")[0].extract())       
            yield scrapy.Request(summaryPage, callback=self.parseSummaryPage)
        nextPage = response.css("a.next::attr(href)")[0].extract()
        if nextPage.endswith('2'):
            nextPage = response.urljoin(nextPage)
            yield scrapy.Request(nextPage, callback = self.parseResultsPage)
            
    def parseSummaryPage(self,response):
        case = Case()    
           
        table = response.xpath("/html/body/div/div/div[2]/div[3]/div[3]/table")
        case['address'] = table.xpath("//tr[5]/td/text()").extract()
        case['proposal'] = table.xpath("//tr[6]/td/text()").extract()
        case['decision'] = table.xpath("//tr[8]/td/text()").extract()           
        constraintspage = response.css("ul.tabs a::attr(href)")[5].extract()
        constraintspage = response.urljoin(constraintspage)
        request = scrapy.Request(constraintspage, callback=self.parseConstraintsPage)
        request.meta['case'] = case
        yield request
        
    def parseConstraintsPage(self,response):
        case = response.meta['case']
        table = response.xpath("/html/body/div/div/div[2]/div[3]/div[3]/table")        
        case['constraints'] = table.xpath("//tr/td[1]/text()").extract()
        yield case