import json
from pprint import pprint
import os
import sys
import re

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
    
class Case:

    def __init__(self, args, outcome,attacks,attackedby,origtext,similarity):
        self.args = args
        self.outcome = outcome
        self.attacks = attacks
        self.attackedby = attackedby
        self.origtext = origtext
        self.similarity = similarity
              
        
def buildCasebase(wordlist):
    with open('app.json') as datafile:
        data = json.load(datafile) 
    casebase = []

    defaultcase = Case([],'Application Approved',[],[],'DEFAULT',0)
    casebase.append(defaultcase)
    for datum in data:
        args = []
        origtext = datum["proposal"][0].strip()
        proposal = extract(origtext,wordlist)
        constraints = [(x.replace(":","")).strip() for x in datum["constraints"]]
        args.append(proposal)
        args.append(constraints)
        args = [item for sublist in args for item in sublist]
        outcome = datum["decision"][0].strip()
        if (outcome == 'Application Approved' or outcome == 'Application Refused'):
            case = Case(args,outcome,[],[],origtext,0)
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
        
    newcase = Case(args,"Outcome Unknown",[],[],'NEWCASE: ' + proposal,0)
    return newcase

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(vars(case))'''

def similarity(list1,list2):
    count = 0
    if len(list1) < len(list2):
        for i in list1:
            if i in list2:
                count+=1
    else:
        for i in list2:
            if i in list1:
                count+=1
    return count
    
    
def computePrediction(newcase,casebase,n):
    for case in casebase:
        case.similarity = similarity(newcase.args,case.args)
    casebase = sorted(casebase, key=lambda x: x.similarity)
    casebase.reverse()
    similarcases = casebase[:n]
    approvals = [case for case in similarcases if case.outcome == "Application Approved"]
    if len(approvals) >= (len(similarcases)/2):
        return "Application Approved"
    else:
        return "Application Refused"
        
        
