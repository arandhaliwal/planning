from knnfao import *


wordlist = getKeywords()

casebase = buildCasebase(wordlist)

#casebase.sort(key=lambda c: c.date)
#limit casebase to 300 items for now
#casebase = [casebase[0]] + casebase[180:209]
#casebase = casebase[:-822]
'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(case.args)
    pprint(case.outcome)'''
    
'''li = []
for case in casebase:
    for arg in case.args:
        li.append(arg)
        
for word in wordlist:
    print(word + " " + str(li.count(word)))'''  

print(len(casebase))    
 
'''tcount = 0
tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
for i in range(1,len(casebase)):
    newcase = casebase[1]
    actual = newcase.outcome
    casebase.remove(newcase)
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,casebase,6)
    if predo == actual:
        result = "success"
        tcount += 1
        if predo == "basement":
            tpcount += 1
        else:
            tncount += 1
    else:
        result = "fail"
        if predo == "basement":
            fpcount += 1
        else:
            fncount += 1
    print("case" + str(i+1) + " predicted = " + predo + ", actual = " + actual + "      " + result)
    newcase.outcome = actual
    casebase.append(newcase)
print("tcount = " + str(tcount))
print("tpcount = " + str(tpcount))
print("fpcount = " + str(fpcount))
print("tncount = " + str(tncount))
print("fncount = " + str(fncount))'''


#temporal
'''tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
tcount = 0
count = 0
for i in range(1,60):
    newcase = casebase[i]
    actual = newcase.outcome
    cbtotest = casebase[:i]
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,cbtotest,6)
    if predo == actual:
        tcount += 1
        result = "success"
        if predo == "back addition":
            tpcount += 1
        else:
            tncount += 1
    else:
        result = "fail"
        if predo == "back addition":
            fpcount += 1
        else:
            fncount += 1
    print("case" + str(i+1) + " predicted = " + predo + ", actual = " + actual + "      " + result)
    count += 1
    if count % 59 == 0:
        print("tcount = " + str(tcount))
        tcount = 0
    newcase.outcome = actual
#print("tcount = " + str(tcount))
print("tpcount = " + str(tpcount))
print("fpcount = " + str(fpcount))
print("tncount = " + str(tncount))
print("fncount = " + str(fncount))'''

#test one
newcase = casebase[13]
actual = newcase.outcome
casebase.remove(newcase)
newcase.outcome = "Outcome Unknown"
predo = computePrediction(newcase,casebase,6)
print("PREDICTION: " + predo)
