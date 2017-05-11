import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.stem import WordNetLemmatizer
import json
from pprint import pprint
import os

with open("keywords.txt","r") as keywords:
    wordlist = []
    for line in keywords:
        wordlist.append(line)
    wordlist = [i.strip() for i in wordlist]
         

def extract(text):
    """Gets the keywords from a text excerpt."""
    result = []
    for keyword in wordlist:
        if keyword in text:
            result.append(keyword)
    result = ["screen" if x == "screening" 
               else "glazed" if x == "glazing"
               else "roof slope" if x == "roofslope"
               else x for x in result]
    result = set(result)
    return result
    
class Case:

    def __init__(self, args, outcome):
        self.args = args
        self.outcome = outcome
        

with open('app.json') as datafile:
    data = json.load(datafile)

casebase = []
defaultcase = Case([],'Application Refused')
casebase.append(defaultcase)
for datum in data:
    args = []
    proposal = extract(datum["proposal"][0].strip())
    constraints = [(x.replace(":","")).strip() for x in datum["constraints"]]
    args.append(proposal)
    args.append(constraints)
    args = [item for sublist in args for item in sublist]
    outcome = datum["decision"][0].strip()
    if (outcome == 'Application Approved' or outcome == 'Application Refused'):
        case = Case(args,outcome)
        casebase.append(case)

newcase = Case(['glazed',
          'erection',
          'screen',
          'roof level',
          'additional floor',
          'back addition',
          'second floor',
          'terrace',
          'door',
          'Adjacent To Conservation Area (50m)',
          'Archaeological Priority Area',
          'Adjacent To Historic Park Or Garden (200m)',
          'Environment Agency Flood Risk Zone 2',
          'Environment Agency Flood Risk Zone 3',
          'Buildings Structures And Works Exceeding 150 Metres',
          'Controlled Parking Zone U',
          'Flood Zone 3 Low Residual Risk',
          'South'],'Outcome Unknown')           
        
#for case in casebase:
    #pprint(vars(case))   
    
def differentoutcomes(a,b):
    return a.outcome != b.outcome


#A is more specific than B
def specificity(a,b):
    return set(b.args).issubset(set(a.args))
    
# there does not exist another case in cases which is less specific than a and more specific than b with the same outcome as a
def concision(cases,a,b):
    return not any((specificity(a,case) and specificity(case,b) and not(differentoutcomes(a,case)) and (case != a) and (case!=b)) for case in cases)


def attacks(cases,a,b):
    return differentoutcomes(a,b) and specificity(a,b) and concision(cases,a,b)
    
def newcaseattacks(newcase,targetcase):
    return not specificity(newcase,targetcase)
    
'''case1 = Case([],"plus")
case2 = Case(["S"],"minus")
case3 = Case(["S","O"],"plus")
case4 = Case(["S","E"],"plus")
case5 = Case(["S","E","O"],"minus")
case6 = Case(["S","E","O","M"],"plus")

casebase = [case1,case2,case3,case4,case5,case6]

newcase = Case(["S","E","O","G"],"unknown")'''

'''for case in casebase:
    for othercase in casebase:
        if attacks(casebase,case,othercase):
            print("ATTACKER")
            #pprint(case)
            pprint(vars(case))
            print("VICTIM")
            #pprint(othercase)
            pprint(vars(othercase))
    if newcaseattacks(newcase,case):
        print("ATTACKER")
        pprint(vars(newcase))
        print("VICTIM")
        pprint(vars(case))'''
            

#case1 is default case
f = open("input.dl","w+")
count = 0
for case in casebase:
    count += 1
    f.write("arg(case%d).\n" % (count))
f.write("arg(newcase).\n")
count1 = 0
for case in casebase:
    count1 += 1
    count2 = 0
    for othercase in casebase:
        count2 += 1
        if attacks(casebase,case,othercase):
            f.write("att(case%d,case%d).\n" % (count1,count2))
    if newcaseattacks(newcase,case):
        f.write("att(newcase,case%d).\n" % (count1))
f.close()

os.system("gringo --warn none ground.dl input.dl | clasp 0 >extension.txt")

with open("extension.txt","r") as extension:
    if "in(case1)" in extension:
        print("Application Refused")
    else:
        print("Application Approved")









