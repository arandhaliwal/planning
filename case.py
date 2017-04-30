import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.stem import WordNetLemmatizer
import json
from pprint import pprint

def extract(text):
    """Gets the keywords from a text excerpt.
    The text is split into words and the boring words are removed.
    Args:
        text (str): The text to get keywords from.
    Returns:
        (Sequence[str]): The keywords of the text.
    """
    tokens = [word.lower() for word in word_tokenize(text)]

    # tag words as verb, noun etc
    tagged_words = pos_tag(tokens)
    tagged_words = [("shed","NN") if x[0] == "shed"
                    else ("screening","NN") if x[0] == "screening"
                    else ("existing","JJ") if x[0] == "existing"
                    else ("glazed","JJ") if x[0] == "glazed"
                    else x for x in tagged_words]

    
    #We don't want keywords to contain anything in this list
    forbidden = ['.',',',';',':','?','!','+',')','(','[',']','/','<','>','"','©','1','2','3','4','5','6','7','8','9','0']

    # NLTK Chunking - detects noun phrases and phrases of form verb noun or adj noun
    patterns = """NP: {<CD><JJ><JJ><NN>}
                      {<JJ>*<NN><NNS>}
                      {<CD><NNS>}
                      {<CD>}
                      {<JJ><NN><RB><NN>}
                      {<JJ><RP><NN>}
                      {<JJ><NN><JJ><NN>}
                      {<JJR><NNS>}
                      {<JJ>*<NNS>}
                      {<NN><NNS>} 
                      {<JJ><NNS>}
                      {<JJ>*<NN>*}
                      {<NN>*}
                      {<NNS>*}"""
    chunker = RegexpParser(patterns)
    chunks = chunker.parse(tagged_words)

    #these are the phrases we want, as lists within a list
    validphrases = []
    for t in chunks.subtrees():
        if t.label() == 'NP':
            validphrases.append([x for x,y in t.leaves()])

    #turning lists within lists into actual noun phrases i.e [[radiation], [breast,cancer]] becomes [radiation, breast cancer]
    lemmatizables = []
    for sublist in validphrases:
        lemmatizables.append(' '.join(sublist))

    lemmatizer = WordNetLemmatizer()
    lems = [lemmatizer.lemmatize(x) for x in lemmatizables]

    with open('stopwords.txt', 'r') as stopwords:
        wordlist = []
        for line in stopwords:
            wordlist.append(line)
        wordlist = [i.strip() for i in wordlist]
    #removing stopwords after lemmatizinga, then removing anything containing punctuation or a number
    lems = filter(lambda lem: lem not in wordlist, lems)
    #lems = filter(lambda lem: not any(char in lem for char in forbidden), lems)

    return tuple(lems)
    #return tagged_words
    
    
class Case:

    def __init__(self, args, outcome):
        self.args = args
        self.outcome = outcome
        

with open('app.json') as datafile:
    data = json.load(datafile)

casebase = []
for datum in data:
    args = []
    #proposal = extract(datum["proposal"][0].strip())
    constraints = [(x.replace(":","")).strip() for x in datum["constraints"]]
    #args.append(proposal)
    args.append(constraints)
    args = [item for sublist in args for item in sublist]
    outcome = datum["decision"][0].strip()
    if (outcome == 'Application Approved' or outcome == 'Application Refused'):
        case = Case(args,outcome)
        casebase.append(case)

#for case in casebase:
    #pprint(vars(case))
    
    
def differentoutcomes(a,b):
    return a.outcome != b.outcome


#A is more specific than B
def specificity(a,b):
    return set(b.args).issubset(a.args)
    
# there does not exist another case in cases which is less specific than a and more specific than b with the same outcome as a
def concision(cases,a,b):
    return not any((specificity(a,case) and specificity(case,b) and not(differentoutcomes(a,case)) and (case != a) and (case!=b)) for case in cases)


def attacks(cases,a,b):
    return differentoutcomes(a,b) and specificity(a,b) and concision(cases,a,b)
    
def newcaseattacks(newcase,targetcase):
    return not specificity(newcase,targetcase)
    
'''case1 = Case([],"plus")
case2 = Case(["S"],"minus")
case3 = Case(["S","O"],"plus")
case4 = Case(["S","E"],"plus")
case5 = Case(["S","E","O"],"minus")
case6 = Case(["S","E","O","M"],"plus")

casebase = [case1,case2,case3,case4,case5,case6]

newcase = Case(["S","E","O","G"],"unknown")'''

for case in casebase:
    for othercase in casebase:
        if attacks(casebase,case,othercase):
            print("ATTACKER")
            #pprint(case)
            pprint(vars(case))
            print("VICTIM")
            #pprint(othercase)
            pprint(vars(othercase))
        '''if newcaseattacks(newcase,case):
            print("ATTACKER")
            pprint(vars(newcase))
            print("VICTIM")
            pprint(vars(case))'''
