
from case import *
import re

wordlist = getKeywords()

#casebase = buildCasebase(wordlist)

#newcase = getNewCase(wordlist)

'''case1 = Case([],"plus",[],[],'default')
case2 = Case(["S"],"minus",[],[],'S')
case3 = Case(["S","O"],"plus",[],[],'SO')
case4 = Case(["S","E"],"plus",[],[],'SE')
case5 = Case(["S","E","O"],"minus",[],[],'SEO')
case6 = Case(["S","E","O","M"],"plus",[],[],'SEOM')
case7 = Case(["S","E","O","G"],"plus",[],[],'SEOG')
case8 = Case(["S","E","O","G","M"],"minus",[],[],'SEOGM')
casebase = [case1,case2,case3,case4,case5]
newcase = Case(["S","E","O","G"],"unknown",[],[],'SEOG')'''

case1 = Case([],"minus",[],[],'default')
case2 = Case(["A"],"plus",[],[],'A')
case3 = Case(["A","B"],"minus",[],[],'AB')
case4 = Case(["B","C"],"minus",[],[],'BC')
case5 = Case(["A","B","C"],"plus",[],[],'ABC')
case6 = Case(["A","B","D"],"minus",[],[],'ABD')
case7 = Case(["B","C","D"],"plus",[],[],'BCD')
case8 = Case(["A","B","C","D"],"minus",[],[],'ABCD')
case9 = Case(["A","B","D","F"],"plus",[],[],'ABDF')
case10 = Case(["A","B","C","D","E"],"plus",[],[],'ABCDE')
case11 = Case(["A","B","C","D","E","F"],"plus",[],[],'ABCDEF')
case12 = Case(["H"],"plus",[],[],'H')
case13 = Case(["A","B","C","D","E","F","G"],"minus",[],[],'ABCDEFG')
case14 = Case(["B","C","H"],"minus",[],[],'BCH')
case15 = Case(["A","B","C","H"],"minus",[],[],'ABCH')
case16 = Case(["A","B","C","D","H"],"plus",[],[],'ABCDH')
case17 = Case(["A","B","C","D","H","M"],"plus",[],[],'ABCDHM')
casebase = [case1,case2,case3,case4,case5,case6,case7,case8,case9,case10,case11,case12,case13,case14,case15,case16,case17]
newcase = Case(["A","B","C","D","E","F","H","J","K","M"],"unknown",[],[],'ABCDEFHJKM')

print("Prediction:")
prediction = computePrediction(newcase,casebase)
if prediction == "Application Approved":
    prediction = "minus"    #TESTCASE HAS DEFAULT MINUS
else:
    prediction = "plus"
print(prediction)
agreement = prediction == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanation:\n")
printExplanation(trees)