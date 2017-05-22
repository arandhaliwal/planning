from factorsasoutcomes import *
import random

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(vars(case))'''
    
randomnumbers = random.sample(range(1, 268), 45)    
    
print(randomnumbers)

casebasetotest = [x for ind, x in enumerate(casebase) if ind not in randomnumbers]

for i in randomnumbers:
    predo = computePrediction(casebase[i],casebasetotest)
    actual = casebase[i].outcome
    if predo == actual:
        result = "success"
    else:
        result = "fail"
    print("predicted = " + predo + ", actual = " + actual + "      " + result)