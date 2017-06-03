from case import *


wordlist = getKeywords()

casebase = buildCasebase(wordlist)

casebase.sort(key=lambda c: c.date)
#limit casebase to 300 items for now
casebase = [casebase[0]] + casebase[38:]

'''count = 0
for case in casebase:
    count += 1
    pprint("case%d:" % count)
    pprint(vars(case))'''

#flat test of whole cb, no time element
tpcount = 0
fpcount = 0
tncount = 0
fncount = 0
for i in range(1,301):
    newcase = casebase[1]
    actual = newcase.outcome
    casebase.remove(newcase)
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,casebase)
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
    casebase.append(newcase)
print("tpcount = " + str(tpcount))
print("fpcount = " + str(fpcount))
print("tncount = " + str(tncount))
print("fncount = " + str(fncount))

#temporal order testing, with cb = all previous cases each time
'''fcount = 0
for i in range(1,300):
    newcase = casebase[i]
    actual = newcase.outcome
    cbtotest = casebase[:i]
    newcase.outcome = "Outcome Unknown"
    predo = computePrediction(newcase,cbtotest)
    if predo == actual:
        result = "success"
    else:
        result = "fail"
        fcount +=1
    print("case" + str(i+1) + " predicted = " + predo + ", actual = " + actual + "      " + result + "   fcount =" + str(fcount))
    newcase.outcome = actual
print(fcount)'''
    

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