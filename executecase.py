from case import *
import re

wordlist = getKeywords()

#casebase = buildCasebase(wordlist)

#newcase = getNewCase(wordlist)

'''case1 = Case([],"plus",[],[],'default',datetime(1900, 1, 1, 0, 0))
case2 = Case(["S"],"minus",[],[],'S',datetime(1900, 1, 1, 0, 0))
case3 = Case(["S","O"],"plus",[],[],'SO',datetime(1900, 1, 1, 0, 0))
case4 = Case(["S","E"],"plus",[],[],'SE',datetime(1900, 1, 1, 0, 0))
case5 = Case(["S","E","O"],"minus",[],[],'SEO',datetime(1900, 1, 1, 0, 0))
case6 = Case(["S","E","O","M"],"plus",[],[],'SEOM',datetime(1900, 1, 1, 0, 0))
case7 = Case(["S","E","O","G"],"plus",[],[],'SEOG',datetime(1900, 1, 1, 0, 0))
case8 = Case(["S","E","O","G","M"],"minus",[],[],'SEOGM',datetime(1900, 1, 1, 0, 0))
casebase = [case1,case2,case3,case4,case5]
newcase = Case(["S","E","O","G"],"unknown",[],[],'SEOG',datetime(1900, 1, 1, 0, 0))'''

case1 = Case([],"minus",[],[],'default',datetime(1900, 1, 1, 0, 0),0)
case2 = Case(["A"],"plus",[],[],'A',datetime(1900, 1, 1, 0, 0),0)
case3 = Case(["A","B"],"minus",[],[],'AB',datetime(1900, 1, 1, 0, 0),0)
case4 = Case(["B","C"],"minus",[],[],'BC',datetime(1900, 1, 1, 0, 0),0)
case5 = Case(["A","B","C"],"plus",[],[],'ABC',datetime(1900, 1, 1, 0, 0),0)
case6 = Case(["A","B","D"],"minus",[],[],'ABD',datetime(1900, 1, 1, 0, 0),0)
case7 = Case(["B","C","D"],"plus",[],[],'BCD',datetime(1900, 1, 1, 0, 0),0)
case8 = Case(["A","B","C","D"],"minus",[],[],'ABCD',datetime(1900, 1, 1, 0, 0),0)
case9 = Case(["A","B","D","F"],"plus",[],[],'ABDF',datetime(1900, 1, 1, 0, 0),0)
case10 = Case(["A","B","C","D","E"],"plus",[],[],'ABCDE',datetime(1900, 1, 1, 0, 0),0)
case11 = Case(["A","B","C","D","E","F"],"plus",[],[],'ABCDEF',datetime(1900, 1, 1, 0, 0),0)
case12 = Case(["H"],"plus",[],[],'H',datetime(1900, 1, 1, 0, 0),0)
case13 = Case(["A","B","C","D","E","F","G"],"minus",[],[],'ABCDEFG',datetime(1900, 1, 1, 0, 0),0)
case14 = Case(["B","C","H"],"minus",[],[],'BCH',datetime(1900, 1, 1, 0, 0),0)
case15 = Case(["A","B","C","H"],"minus",[],[],'ABCH',datetime(1900, 1, 1, 0, 0),0)
case16 = Case(["A","B","C","D","H"],"plus",[],[],'ABCDH',datetime(1900, 1, 1, 0, 0),0)
case17 = Case(["A","B","C","D","H","M"],"plus",[],[],'ABCDHM',datetime(1900, 1, 1, 0, 0),0)
casebase = [case1,case2,case3,case4,case5,case6,case7,case8,case9,case10,case11,case12,case13,case14,case15,case16,case17]
newcase = Case(["A","B","C","D","E","F","H","J","K","M"],"unknown",[],[],'ABCDEFHJKM',datetime(1900, 1, 1, 0, 0),0)

print("Prediction:")
prediction = computePrediction(newcase,casebase)
if prediction == "Application Approved":
    prediction = "minus"    #KRIS TESTCASE HAS DEFAULT MINUS
else:
    prediction = "plus"
print(prediction)
agreement = prediction == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nSee tree image for explanation\n")
drawExplanation(trees)
#printExplanation(trees)
#trees = [item for sublist in trees for item in sublist]
os.system("tree.png")