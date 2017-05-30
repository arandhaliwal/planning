
from case import *
import re

wordlist = getKeywords()

#casebase = buildCasebase(wordlist)

#newcase = getNewCase(wordlist)

'''case1 = Case([],"plus",[],[])
case2 = Case(["S"],"minus",[],[])
case3 = Case(["S","O"],"plus",[],[])
case4 = Case(["S","E"],"plus",[],[])
case5 = Case(["S","E","O"],"minus",[],[])
case6 = Case(["S","E","O","M"],"plus",[],[])
case7 = Case(["S","E","O","G"],"plus",[],[])
case8 = Case(["S","E","O","G","M"],"minus",[],[])
casebase = [case1,case2,case3,case4,case5]
newcase = Case(["S","E","O","G"],"unknown",[],[])'''

case1 = Case([],"minus",[],[])
case2 = Case(["A"],"plus",[],[])
case3 = Case(["A","B"],"minus",[],[])
case4 = Case(["B","C"],"minus",[],[])
case5 = Case(["A","B","C"],"plus",[],[])
case6 = Case(["A","B","D"],"minus",[],[])
case7 = Case(["B","C","D"],"plus",[],[])
case8 = Case(["A","B","C","D"],"minus",[],[])
case9 = Case(["A","B","D","F"],"plus",[],[])
case10 = Case(["A","B","C","D","E"],"plus",[],[])
case11 = Case(["A","B","C","D","E","F"],"plus",[],[])
case12 = Case(["A","B","C","D","E","F","G"],"minus",[],[])
casebase = [case1,case2,case3,case4,case5,case6,case7,case8,case9,case10,case11,case12]
newcase = Case(["A","B","C","D","E","F","H","J","K","M"],"unknown",[],[])

print("Prediction:")
prediction = computePrediction(newcase,casebase)
if prediction == "Application Approved":
    prediction = "minus"
else:
    prediction = "plus"
print(prediction)
agreement = prediction == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print(trees)
print("\nExplanation:\n")
printExplanation(trees)