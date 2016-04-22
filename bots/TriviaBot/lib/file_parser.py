import numpy as np
import hickle as hkl

def file2hickle ( category ) :
    prefix = "data/"
    category = prefix + category 
    file = open( category )
    listofcontents = [] 
    choicelist = []
    contents ={}
    linenumber=0
    
    for line in file:
        if line.startswith('#'):
            contents['ques'] = line[2:]
        elif line.startswith('^'):
            contents['ans']= line[2:]
        elif line[0] in ['A','B','C','D']:
            choicelist.append(line[2:])
            if line.startswith('D'):
                choicelist.sort()
                contents['ansnum'] = choicelist.index(contents['ans'])
                choicestring = ""
                for i in range(len(choicelist)):
                    choicestring += "[" + str(i) + "] " + choicelist[i] + " "  
                
                contents["choices"] = choicestring
                listofcontents.append(contents)
                #print "question : ",contents["ques"],"answer :",contents['ansnum'],contents["ans"],"choice :",contents["choices"]
                choicelist = []  
                contents = {}
    return listofcontents

# pick a category
l = file2hickle("people")
print 'Len("people") : ', len(l)

# hickle name
hkl_name = 'people.hkl'

# save as hickle
hkl.dump(l,hkl_name)
