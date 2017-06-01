from factorsasoutcomes import *

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

newcase = getNewCase(wordlist)

print("Prediction:")
prediction = computePrediction(newcase,casebase)
print(prediction)
agreement = prediction == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanations:\n")
printExplanation(trees)
