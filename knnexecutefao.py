from knnfao import *

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

newcase = getNewCase(wordlist)

prediction = computePrediction(newcase,casebase,4)

print("prediction")
print(prediction)

