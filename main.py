from loadData import *
from preprocessing import *

# load data
result = loadData("dtoEmails_1_0.txt")

# preprocessing

# extract body
body = extractBody(result)

# compute shingle


# create hash table
prehash = body[0][0:14]
hashShingle = list()
for i in range(100):
    hashShingle.append(hash(body[i]))
print(hashShingle)

# compute fingerprint


# compute similarity
hashShingle1 = hashShingle[0:50]
hashShingle2 = hashShingle[50:100]

union = list(set(hashShingle1).union(set(hashShingle2)))   # computer union set
intersection = list(set(hashShingle1).intersection(set(hashShingle2))) # computer intersection set
similiarity = len(union)/len(intersection)


# listtostr
def listToStr(list):
    newList = list()
    length=list.__len__
    for i in range(length):
        newList = newList + list[i]
    return(newList)
