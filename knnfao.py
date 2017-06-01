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

def getFactor():
    with open("factorinput.txt","r") as input:
        factor = input.read()  
    return factor
    
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
    factor = getFactor()
    defaultcase = Case([],'not %s' % factor,[],[],'DEFAULT',0)
    casebase.append(defaultcase)
    for datum in data:
        outcome = datum["decision"][0].strip()
        origtext = datum["proposal"][0].strip()
        if (outcome == 'Application Approved'):
            args = []
            proposal = extract(datum["proposal"][0].strip(),wordlist)
            if factor in proposal:
                proposal.remove(factor)
                outcome = factor
            else:
                outcome = 'not %s' % factor
            constraints = [(x.replace(":","")).strip() for x in datum["constraints"]]
            args.append(proposal)
            args.append(constraints)
            args = [item for sublist in args for item in sublist]
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
                    
def similarity(list1,list2):
    inter = set(list1).intersection(set(list2))
    union = set(list1).union(set(list2))
    return len(inter)/len(union)
       
def computePrediction(newcase,casebase,n):
    factor = getFactor()
    for case in casebase:
        case.similarity = similarity(newcase.args,case.args)
    casebase = sorted(casebase, key=lambda x: x.similarity)
    casebase.reverse()
    similarcases = casebase[:n]
    '''for c in similarcases:
        print(c.origtext)
        print("outcome:" + c.outcome)
        print(c.similarity)'''
    nots = [case for case in similarcases if case.outcome == 'not %s' % factor]
    if len(nots) >= (len(similarcases)/2):
        return 'not %s' % factor
    else:
        return factor