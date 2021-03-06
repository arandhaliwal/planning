import json
from pprint import pprint
import os
import sys
import re
from datetime import datetime
import pydotplus
import time

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

    def __init__(self, args, outcome,attacks,attackedby,origtext,date,label):
        self.args = args
        self.outcome = outcome
        self.attacks = attacks
        self.attackedby = attackedby
        self.origtext = origtext
        self.date = date
        self.label = label
              
        
def buildCasebase(wordlist):
    with open('app.json') as datafile:
        data = json.load(datafile) 
    casebase = []

    defaultcase = Case([],'Application Approved',[],[],'DEFAULT',datetime(1900, 1, 1, 0, 0),0)
    casebase.append(defaultcase)
    for datum in data:
        date = datum["date"][0].strip()
        date = convertDate(date)
        args = []
        origtext = datum["proposal"][0].strip()
        proposal = extract(origtext,wordlist)
        constraints = [(x.replace(":","")).strip() for x in datum["constraints"]]
        args.append(proposal)
        args.append(constraints)
        args = [item for sublist in args for item in sublist]
        outcome = datum["decision"][0].strip()
        if (outcome == 'Application Approved' or outcome == 'Application Refused'):
            case = Case(args,outcome,[],[],origtext,date,0)
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
        
    newcase = Case(args,"Outcome Unknown",[],[],'NEWCASE: ' + proposal,datetime(1900, 1, 1, 0, 0),0)
    return newcase
    
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
    
'''def isnearest(case,newcase,casebase):
    return specificity(newcase,case) and (not any (specificity(newcase,othercase) and specificity(othercase,case) and case != othercase for othercase in casebase))
  
def printnearest(newcase,casebase):
    for case in casebase:
        if isnearest(case,newcase,casebase):
            pprint(vars(case))'''
                      
            
#case1 is default case
def computePrediction(newcase,casebase):
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
                case.attacks.append(othercase)
                othercase.attackedby.append(case)
        if newcaseattacks(newcase,case):
            f.write("att(newcase,case%d).\n" % (count1))
            newcase.attacks.append(case)
            case.attackedby.append(newcase)
    f.close()
    os.system("gringo --warn none ground.dl input.dl | clasp 0 >extension.txt")
            
    #print("Prediction:")
    if 'in(case1)' in open('extension.txt').read():  
        return("Application Approved")
    else:
        return("Application Refused")
        
    #print("\nExplanation - The nearest case(s):")
    #printnearest(newcase,casebase)

def getGroundedExtension(casebase,newcase):
    with(open("extension.txt")) as extension:
        for line in extension:
            if line.startswith("in"):
                groundedextension = line
            
    ge = re.findall(r'\d+', groundedextension)
    ge = [int(s) for s in ge]
    ge = [casebase[x-1] for x in ge]
    if "newcase" in groundedextension:
        ge.append(newcase)
    return ge
    
def recursivefunctiondisagree(tree,case,nextcase,newcase,ge):
    treecopy = list(tree)
    treecopy.append(nextcase)
    if nextcase.attackedby == []:
        return treecopy
    else:
        return recursivefunctionagree(treecopy,nextcase,ge,newcase)

def recursivefunctionagree(tree,case,ge,newcase):
    biglist = []
    for nextcase in ge:
        if case in nextcase.attacks:
            treecopy = list(tree)
            treecopy.append(nextcase)
            if nextcase.attackedby == []:
                biglist.append(treecopy)
            else:
                for next2case in nextcase.attackedby:
                    biglist.append(recursivefunctiondisagree(treecopy,nextcase,next2case,newcase,ge))
    return biglist
        
def flatten(mylist):
    for i in mylist:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i  

def computeExplanation(agreement,ge,casebase,newcase):
    if agreement:        
       treeslist = []
       for case in casebase[0].attackedby:
           treebase = [casebase[0],case]
           treeslist.append(recursivefunctionagree(treebase,case,ge,newcase))
    else:
        treeslist = []
        for case in ge:
            if casebase[0] in case.attacks:
                treebase = [casebase[0],case]
                if case.attackedby == []:
                    treeslist.append(treebase)
                else:
                    for nextcase in case.attackedby:
                        treeslist.append(recursivefunctiondisagree(treebase,case,nextcase,newcase,ge))
    treeslist = list(flatten(treeslist))  
    
    sublist = []
    trees = []
    for case in treeslist:
        if case == casebase[0]:
            if sublist: 
                trees.append(sublist)
            sublist = [case]
        else:
            sublist.append(case)
    trees.append(sublist)
    return trees

def printExplanation(trees):
    for tree in trees:     
        for case in tree:
            print(case.origtext)
            print(case.outcome)
            if tree[len(tree)-1] != case:
               print("\nis attacked by...\n")
            else:
                print("\nwhich is unattacked\n")
        if trees[len(trees)-1] != tree:
           print("OR\n")

def drawExplanation(trees):    
    graph = pydotplus.Dot(graph_type='graph',dpi = 300)
    
    labelcount = 0
    for tree in trees:
        for i in range(len(tree)):
            case = tree[i]
            if case.label == 0:
                labelcount +=1
                case.label = labelcount
   
    for tree in trees:
        for i in range(len(tree)-1):
                case = tree[i]
                nextcase = tree[i+1]
                if not graph.get_edge(str(case.label),str(nextcase.label)):
                    edge = pydotplus.Edge(str(case.label),str(nextcase.label))
                    graph.add_edge(edge)
    
    treecaseset = [item for sublist in trees for item in sublist]
    treecaseset = set(treecaseset)   
    sortedtreecaseset = sorted(treecaseset, key=lambda x: x.label)
    print("key:")
    for case in sortedtreecaseset:
        print(case.label)
        print(case.origtext)
        print("")
        print("Indentified factors:")
        print("")
        print("\n".join(case.args))
        print("")
        print("Outcome:")
        print(case.outcome)
        print("")
    graph.write_png('tree.png')

