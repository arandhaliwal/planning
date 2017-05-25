from case import *
import re

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

newcase = getNewCase(wordlist)

'''case1 = Case([],"plus",[],[])
case2 = Case(["S"],"minus",[],[])
case3 = Case(["S","O"],"plus",[],[])
case4 = Case(["S","E"],"plus",[],[])
case5 = Case(["S","E","O"],"minus",[],[])
case6 = Case(["S","E","O","M"],"plus",[],[])
casebase = [case1,case2,case3,case4,case5]
newcase = Case(["S","E","O","G"],"unknown",[],[])'''

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

print("explanation\n")

def recursivefunctionagree(tree,case):
    nextcase = case.attackedby[0]
    if nextcase.attackedby == [] or newcase in nextcase.attackedby:
        return tree
    else:
        tree.append(nextcase)
        return recursivefunctiondisagree(tree,nextcase)

def recursivefunctiondisagree(tree,case):
    for nextcase in ge:
        if case in nextcase.attacks:
            tree.append(nextcase)
            break
    if nextcase.attackedby == []:
        return tree
    else:
        return recursivefunctionagree(tree,nextcase)
    

for case in ge:
    if casebase[0] in case.attacks:
        tree = [casebase[0],case]
        tree = recursivefunctionagree(tree,case)
        
for case in tree:
    pprint(case.args)
    pprint(case.outcome)
    if tree[len(tree)-1] != case:
        print("\nis attacked by...")
    else:
        print("\nwhich is unattacked")