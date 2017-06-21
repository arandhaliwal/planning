from factorsasoutcomes import *
import time

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

#casebase.sort(key=lambda c: c.date)
#limit casebase to 300 items for now
#casebase = casebase[:-284]

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(case.origtext)
    pprint(case.args)
    pprint(case.outcome)'''
    
'''li = []
for case in casebase:
    for arg in case.args:
        li.append(arg)
        
for word in wordlist:
    print(word + " " + str(li.count(word)))'''
    
print(len(casebase))
    
#BACK ADDITION
#flat test of whole cb, no time element
'''tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
tcount = 0
for i in range(1,len(casebase)):
    newcase = casebase[1]
    actual = newcase.outcome
    casebase.remove(newcase)
    newcase.outcome = "Outcome Unknown"
    #start_time = time.time()
    predo = computePrediction(newcase,casebase)
    #print(time.time() - start_time)
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

#temporal order testing, with cb = all previous cases each time
'''tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
tcount = 0
for i in range(1,295):
    newcase = casebase[i]
    actual = newcase.outcome
    cbtotest = casebase[:i]
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,cbtotest)
    if predo == actual:
        result = "success"
        tcount +=1
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
    if i % 59 == 0:
        print("tcount = " + str(tcount))
        tcount = 0
    newcase.outcome = actual
print("tpcount = " + str(tpcount))
print("fpcount = " + str(fpcount))
print("tncount = " + str(tncount))
print("fncount = " + str(fncount))'''
    

#test on one case
'''newcase = casebase[13]
actual = newcase.outcome
casebase.remove(newcase)
newcase.outcome = "Outcome Unknown"
predo = computePrediction(newcase,casebase)
print("PREDICTION: " + predo)
agreement = predo == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanation:\n")
drawExplanation(trees)
os.system("tree.png")'''

newcase = getNewCase(wordlist)
print("Prediction:")
prediction = computePrediction(newcase,casebase)
print(prediction)
agreement = prediction == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanation: see graph image\n")
drawExplanation(trees)
os.system("tree.png")