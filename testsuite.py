from case import *
import time

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

#casebase.sort(key=lambda c: c.date)
#limit casebase to certain number
casebase = [casebase[0]] + casebase[26:]

'''li = []
for case in casebase:
    for arg in case.args:
        li.append(arg)
        
for word in wordlist:
    print(word + " " + str(li.count(word)))'''


'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(case.args)
    pprint(case.outcome)'''
    
print(len(casebase))

#flat test of whole cb, no time element
#tpcount = 0
#fpcount = 0
#tncount = 0
#fncount = 0
'''timings = []
for i in range(1,11):
    newcase = casebase[1]
    actual = newcase.outcome
    casebase.remove(newcase)
    newcase.outcome = "Outcome Unknown"
    start_time = time.time()
    predo = computePrediction(newcase,casebase)
    ti = time.time() - start_time
    timings.append(ti)
    print(ti)
    if predo == actual:
        result = "success"
        if predo == "Application Approved":
            tpcount += 1
        else:
            tncount += 1
    else:
        result = "fail"
        if predo == "Application Approved":
            fpcount += 1
        else:
            fncount += 1     
    #print("case" + str(i+1) + " predicted = " + predo + ", actual = " + actual + "      " + result)
    newcase.outcome = actual
    casebase.append(newcase)
print("average:")
print(sum(timings)/len(timings))'''
# print("minimum:")
# print(min(timings))
#print("tpcount = " + str(tpcount))
#print("fpcount = " + str(fpcount))
#print("tncount = " + str(tncount))
#print("fncount = " + str(fncount))'''

#temporal order testing, with cb = all previous cases each time
'''tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
for i in range(1,301):
    newcase = casebase[i]
    actual = newcase.outcome
    cbtotest = casebase[:i]
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,cbtotest)
    if predo == actual:
        result = "success"
        if predo == "Application Approved":
            tpcount += 1
        else:
            tncount += 1
    else:
        result = "fail"
        if predo == "Application Approved":
            fpcount += 1
        else:
            fncount += 1
    print("case" + str(i+1) + " predicted = " + predo + ", actual = " + actual + "      " + result)
    newcase.outcome = actual
print("tpcount = " + str(tpcount))
print("fpcount = " + str(fpcount))
print("tncount = " + str(tncount))
print("fncount = " + str(fncount))'''
    

#test on one case
'''newcase = casebase[17]
actual = newcase.outcome
casebase.remove(newcase)
newcase.outcome = "Outcome Unknown"
predo = computePrediction(newcase,casebase)
print(predo)
agreement = predo == casebase[0].outcome
ge = getGroundedExtension(casebase,newcase)
trees = computeExplanation(agreement,ge,casebase,newcase)
print("\nExplanation:\n")
printExplanation(trees)'''