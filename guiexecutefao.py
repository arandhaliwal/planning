from factorsasoutcomes import *

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

newcase = getNewCase(wordlist)

print("Prediction:")
print(computePrediction(newcase,casebase))
print("\nExplanation - The nearest case(s):")
printnearest(newcase,casebase)