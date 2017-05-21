from case import *
import random


wordlist = getKeywords()

casebase = buildCasebase(wordlist)

randomnumbers = random.sample(range(1, 55), 11)

#randomnumbers = [35, 21, 27, 51, 40, 3, 5, 52, 49, 47, 28] 
#randomnumbers = [39, 53, 35, 50, 32, 13, 48, 6, 33, 14, 17]

print(randomnumbers)

casebasetotest = [x for ind, x in enumerate(casebase) if ind not in randomnumbers]

for i in randomnumbers:
    if computePrediction(casebase[i],casebasetotest) == casebase[i].outcome:
        print("success")
    else:
        print("fail")