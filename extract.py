import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.stem import WordNetLemmatizer

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

    
    #We don't want keywords to contain anything in this list
    forbidden = ['.',',',';',':','?','!','+',')','(','[',']','/','<','>','"','©','1','2','3','4','5','6','7','8','9','0']

    # NLTK Chunking - detects noun phrases and phrases of form verb noun or adj noun
    patterns = """NP: {<JJ>*<NN><NNS>}
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
    #return lemmatizables
	
print(extract("Erection of an additional floor at roof level; installation of a door opening from the rear of the second floor and erection of obscure glazed privacy screening over part of the back addition to enable its use as a terrace. "))