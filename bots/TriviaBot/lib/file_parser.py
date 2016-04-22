import numpy as np
import hickle as hkl
from os import walk


def file2list ( category ) :
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
            linenumber += 1
        elif line.startswith('^'):
            contents['ans']= line[2:]
            linenumber += 1
        elif line[0] in ['A','B','C','D']:
            choicelist.append(line[2:])
            linenumber += 1
            if line.startswith('D'):
                choicelist.sort()
                contents['ansnum'] = choicelist.index(contents['ans'])
                choicestring = ""
                for i in range(len(choicelist)):
                    choicestring += "[" + str(i) + "] " + choicelist[i] + " "

                contents["choices"] = choicestring
                listofcontents.append(contents)
                #print "Line :",linenumber,"question : ",contents["ques"],"answer :",contents['ansnum'],contents["ans"],"choice :",contents["choices"]
                choicelist = []
                contents = {}
    return listofcontents

# pick a category
mypath = "../data"
files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)
    break

for file in files:
    print "converting the category",file
    l = file2list(file)
    # hickle name
    hkl_name = "../data/hkldata/"+file+'.hkl'
    # save as hickle
    hkl.dump(l,hkl_name)
