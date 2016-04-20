from nltk.corpus import wordnet as wn

def synsets(str):
    return wn.synsets(str)

def synonymsOf(synsets):
    synonyms = [synset.name().split('.')[0] for synset in synsets]
    #return [y for y in synonyms if y != synonyms[0]]
    if len(synonyms) > 1:
        return list(set(synonyms))
    else:
        return synonyms

def similarities(synsets):
    return [wn.wup_similarity(item,synsets[0]) for item in synsets ]

def antonymsOf(syns):
    antonyms = []
    for syn in syns:
        for lem in syn.lemmas():
            lem_type = str(lem).split('.')[1]
            if lem_type != 'n' and lem_type != 's' and lem_type != 'r':
                antonyms.append(lem.antonyms()[0].name())
    return antonyms

def wordEg(syns):
    print 'wordEg : ',syns[0].examples()
    return syns[0].examples()


#print good, good[0],type(good[0])
#anto =  good[0].lemmas()[0].antonyms()[0].name()
#print type(anto),anto
#print good[0].lemmas()[0]

#print synonymsOf(synsets('good'))
#print synonymsOf(synsets('able'))
#print antonymsOf(synsets('able'))
#print syns
#for syn in syns:
#print syns[0].lemmas()[0]
#[0].antonyms()[0].name()

#print wordEg(synsets('ugly'))


'''
print synonymsOf(synsets('dog'))[1:]
print '_________'
print similarities(synsets('dog'))[1:]
word = 'like dog'
words = word.split(' ')
if len(words) == 2 and words[0] == 'like':
    synonyms =  synonymsOf(synsets(words[1]))
    print ', '.join(synonyms)
'''
 
