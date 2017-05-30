from knn import *
import re

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

newcase = getNewCase(wordlist)

prediction = computePrediction(newcase,casebase,3)

print(prediction)

