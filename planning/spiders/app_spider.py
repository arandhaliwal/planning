import scrapy


class ApplicationSpider(scrapy.Spider):
    name = "app"
    start_urls = [
        'http://public-access.lbhf.gov.uk/online-applications/applicationDetails.do?activeTab=summary&keyVal=OHTSSLBIIIT00',
    ]

    
    def parse(self,response):            
        table = response.xpath("/html/body/div/div/div[2]/div[3]/div[3]/table")
        yield {
            "address" : table.xpath("//tr[5]/td/text()").extract(),
            "proposal": table.xpath("//tr[6]/td/text()").extract(),
            "decision": table.xpath("//tr[8]/td/text()").extract(),
        }
            
        constraintspage = response.css("ul.tabs a::attr(href)")[5].extract()
        constraintspage = response.urljoin(constraintspage)
        yield scrapy.Request(constraintspage, callback=self.parse_constraints)
        
    def parse_constraints(self,response):
        table = response.xpath("/html/body/div/div/div[2]/div[3]/div[3]/table")
        yield {
            "constraints" : table.xpath("//tr/td[1]/text()").extract()
        }
        