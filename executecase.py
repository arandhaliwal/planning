from case import *
import re

wordlist = getKeywords()

#casebase = buildCasebase(wordlist)

#newcase = getNewCase(wordlist)

case1 = Case([],"plus",[],[])
case2 = Case(["S"],"minus",[],[])
case3 = Case(["S","O"],"plus",[],[])
case4 = Case(["S","E"],"plus",[],[])
case5 = Case(["S","E","O"],"minus",[],[])
case6 = Case(["S","E","O","M"],"plus",[],[])
case7 = Case(["S","E","O","G"],"plus",[],[])
case8 = Case(["S","E","O","G","M"],"minus",[],[])
casebase = [case1,case2,case3,case4,case5,case6,case7,case8]
newcase = Case(["S","E","O","G","M","P"],"unknown",[],[])

print("Prediction:")
print(computePrediction(newcase,casebase))
#print("\nExplanation - The nearest case(s):")
#printnearest(newcase,casebase)
   
with(open("extension.txt")) as extension:
    for line in extension:
        if line.startswith("in"):
            groundedextension = line
            
ge = re.findall(r'\d+', groundedextension)
ge = [int(s) for s in ge]
ge = [casebase[x-1] for x in ge]
if "newcase" in groundedextension:
    ge.append(newcase)

#default is plus, outcome is minus

print("\nexplanation:\n")

def recursivefunctionagree(tree,case,count):
    treecopy = list(tree)
    nextcase = case.attackedby[count]
    if nextcase.attackedby == [] or newcase in nextcase.attackedby:
        return treecopy
    else:
        treecopy.append(nextcase)
        return recursivefunctiondisagree(treecopy,nextcase)

def recursivefunctiondisagree(tree,case):
    treecopy = list(tree)
    for nextcase in ge:
        if case in nextcase.attacks:
            treecopy.append(nextcase)
            break
    if nextcase.attackedby == []:
        return treecopy
    else:
        anothertreeslist = []
        count = 0
        for next2case in nextcase.attackedby:
            anothertreeslist.append(recursivefunctionagree(treecopy,nextcase,count))
            count += 1
        return anothertreeslist

for case in ge:
    if casebase[0] in case.attacks:
        treebase = [casebase[0],case]
        treeslist = []
        count = 0
        for nextcase in case.attackedby:
            treeslist.append(recursivefunctionagree(treebase,case,count))
            count += 1

print(treeslist)            
'''for tree in treeslist:            
    for case in tree:
        pprint(case.args)
        pprint(case.outcome)
        if tree[len(tree)-1] != case:
           print("\nis attacked by...\n")
        else:
            print("\nwhich is unattacked\n")
    if treeslist[len(treeslist)-1] != tree:
        print("\nOR\n")'''