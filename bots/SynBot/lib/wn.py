from nltk.corpus import wordnet as wn

def synsets(str):
    return wn.synsets(str)

def synonymsOf(synsets):
    return [synset.name().split('.')[0] for synset in synsets]

def similarities(synsets):
    return [wn.wup_similarity(item,synsets[0]) for item in synsets ]


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
 
