import json
from pprint import pprint
import os
import sys
import re
from datetime import datetime

def getKeywords():
    with open("keywords.txt","r") as keywords:
        wordlist = []
        for line in keywords:
            wordlist.append(line)
        wordlist = [i.strip() for i in wordlist]
    return wordlist

def extract(text,wordlist):
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
    
def convertDate(text):
    date = datetime.strptime(text[4:], '%d %b %Y')
    return date
    
class Case:

    def __init__(self, args, outcome,attacks,attackedby,origtext,similarity,date):
        self.args = args
        self.outcome = outcome
        self.attacks = attacks
        self.attackedby = attackedby
        self.origtext = origtext
        self.similarity = similarity
        self.date = date
              
        
def buildCasebase(wordlist):
    with open('app.json') as datafile:
        data = json.load(datafile) 
    casebase = []

    defaultcase = Case([],'Application Approved',[],[],'DEFAULT',0,datetime(1900, 1, 1, 0, 0))
    casebase.append(defaultcase)
    for datum in data:
        args = []
        origtext = datum["proposal"][0].strip()
        date = datum["date"][0].strip()
        date = convertDate(date)
        proposal = extract(origtext,wordlist)
        constraints = [(x.replace(":","")).strip() for x in datum["constraints"]]
        args.append(proposal)
        args.append(constraints)
        args = [item for sublist in args for item in sublist]
        outcome = datum["decision"][0].strip()
        if (outcome == 'Application Approved' or outcome == 'Application Refused'):
            case = Case(args,outcome,[],[],origtext,0,date)
            for othercase in casebase:
                if case.args == othercase.args and case.outcome != othercase.outcome:
                    casebase.remove(othercase)
            casebase.append(case)
    return casebase
  
def getNewCase(wordlist):  
    with open("proposalinput.txt","r") as input:
        proposal = input.read()  
            
    args = extract(proposal,wordlist)
    constraints = []
    with open("constraintsinput.txt","r") as input2:
        for line in input2:
            constraints.append(line.strip())
        args.update(constraints)
        
    newcase = Case(args,"Outcome Unknown",[],[],'NEWCASE: ' + proposal,0,datetime(1900, 1, 1, 0, 0))
    return newcase

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(vars(case))'''

def similarity(list1,list2):
    inter = set(list1).intersection(set(list2))
    union = set(list1).union(set(list2))
    if len(union) == 0:
        return 1
    else:
        return len(inter)/len(union)
       
def computePrediction(newcase,casebase,n):
    for case in casebase:
        case.similarity = similarity(newcase.args,case.args)
    similarcasebase = sorted(casebase, key=lambda x: x.similarity)
    similarcasebase.reverse()   
    similarcases = similarcasebase[:n]
    print("SIMILAR CASES:")
    print("")
    for c in similarcases:
        print(c.origtext)
        print("")
        print("Indentified factors:")
        print("")
        print("\n".join(c.args))
        print("")
        print(c.outcome)
        print("")
        print("Similarity:")
        print(c.similarity)
        print("")
    print("NEWCASE:")
    print(newcase.origtext)
    print("")
    print("\n".join(newcase.args))
    print("")
    approvals = [case for case in similarcases if case.outcome == "Application Approved"]
    if len(approvals) >= (len(similarcases)/2):
        return "Application Approved"
    else:
        return "Application Refused"
        

        
        
