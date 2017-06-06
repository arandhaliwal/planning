from knn import *
import time

wordlist = getKeywords()

casebase = buildCasebase(wordlist)

casebase.sort(key=lambda c: c.date)
#limit casebase to 300 items for now
casebase = [casebase[0]] + casebase[84:]

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(case.args)
    pprint(case.outcome)'''
    
print(len(casebase))    
    
tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
timings = []
for i in range(1,1601):
    newcase = casebase[1]
    actual = newcase.outcome
    casebase.remove(newcase)
    newcase.outcome = "Outcome Unknown"
    #start_time = time.time()
    predo = computePrediction(newcase,casebase,6)
    #ti = time.time() - start_time
    #timings.append(ti)
    #print(ti)
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
    print("predicted = " + predo + ", actual = " + actual + "      " + result)
    newcase.outcome = actual
    casebase.append(newcase)
#print("average:")
#print(sum(timings)/len(timings))
#print("minimum:")
#print(min(timings))
print("tpcount = " + str(tpcount))
print("fpcount = " + str(fpcount))
print("tncount = " + str(tncount))
print("fncount = " + str(fncount))


#temporal ordering
'''tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
for i in range(12,301):
    newcase = casebase[i]
    actual = newcase.outcome
    cbtotest = casebase[:i]
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,casebase,11)
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
    print("predicted = " + predo + ", actual = " + actual + "      " + result)
    newcase.outcome = actual
print("tpcount = " + str(tpcount))
print("fpcount = " + str(fpcount))
print("tncount = " + str(tncount))
print("fncount = " + str(fncount))'''
