from case import *
import sys
from datetime import datetime

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

casebase.sort(key=lambda c: c.date)

count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(case.date)

'''newcase = getNewCase(wordlist)

print("Prediction:")
prediction = computePrediction(newcase,casebase)
print(prediction)
agreement = prediction == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanations:\n")
printExplanation(trees)'''
