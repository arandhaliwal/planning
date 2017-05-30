from knn import *
import random


wordlist = getKeywords()

casebase = buildCasebase(wordlist)

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(vars(case))'''


for i in range(1,250):
    newcase = casebase[i]
    casebase.remove(newcase)
    predo = computePrediction(newcase,casebase,5)
    actual = newcase.outcome
    if predo == actual:
        result = "success"
    else:
        result = "fail"
    print("predicted = " + predo + ", actual = " + actual + "      " + result)
    casebase.append(newcase)