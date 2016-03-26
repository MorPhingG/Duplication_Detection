from loadData import *
from preprocessing import *
from hashFunction import *
from computeSimilarity import *
from rabinFingerprint import *
from shingle import *
from minHash import *

import datetime


if __name__ == "__main__":
    starttime = datetime.datetime.now()         # save the time
    result = loadData("dtoEmails_1_0.txt")      # load data
    body = extractBody(result)                  # extract body
    shingleBody = go_shingle(go_tokens(body),2) # compute shingle
    hashShingle = hashFunction(shingleBody)     # create hash table

    # rabinFingerprint(shingleBody) # compute fingerprint

    minHashShingle = minHash(hashShingle,200)    # create min hash
    similarity = computeSimilarity(minHashShingle)
    f = open("out.txt","w")
    for i in range(len(similarity)):
        for j in range(len(similarity[i])):
            if(1>similarity[i][j]>0.5):
                f.write("%3d %4d %0.3f\n" % (i,j,similarity[i][j]))
    # use Lsh
    # similiarity = computeSimiliary(hashShingle[0:50]) # compute similarity
    # print(similiarity)

    endtime = datetime.datetime.now()           # save time
    print((endtime - starttime).seconds)

