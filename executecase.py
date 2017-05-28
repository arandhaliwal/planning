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
casebase = [case1,case2,case3,case4,case5]
newcase = Case(["S","E","O","G"],"unknown",[],[])

print("Prediction:")
prediction = computePrediction(newcase,casebase)
print(prediction)
agreement = prediction == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanation:\n")
printExplanation(trees)