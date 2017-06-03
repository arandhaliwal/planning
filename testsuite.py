from case import *


wordlist = getKeywords()

casebase = buildCasebase(wordlist)

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(vars(case))'''

fcount = 0
for i in range(1,299):
    newcase = casebase[1]
    actual = newcase.outcome
    casebase.remove(newcase)
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,casebase)
    if predo == actual:
        result = "success"
    else:
        result = "fail"
        fcount +=1
    print("case" + str(i+1) + " predicted = " + predo + ", actual = " + actual + "      " + result)
    newcase.outcome = actual
    casebase.append(newcase)
print(fcount)

'''newcase = casebase[17]
actual = newcase.outcome
casebase.remove(newcase)
newcase.outcome = "Outcome Unknown"
predo = computePrediction(newcase,casebase)
print(predo)
agreement = predo == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanation:\n")
printExplanation(trees)'''