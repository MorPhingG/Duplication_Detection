from loadData import *
from preprocessing import *
from shingle import *
from hashFunction import *
from computeSimiliarity import *
from rabinFingerprint import *


if __name__ == "__main__":
    result = loadData("dtoEmails_1_0.txt") # load data
    body = extractBody(result) # extract body

    # compute shingle

    #shingleBody = computeShingle(body)

    print go_shingle(go_tokens(body),5)[0]
    print go_k_shingle(body,5)[0]

    shingleBody = [[] for i in range(2)]
    shingleBody[0]=['123','222','346','165']
    shingleBody[1]=['155','123','234','357']
    hashShingle = hashFunction(shingleBody) # create hash table

    # compute fingerprint


    test = go_shingle(go_tokens(body),3)[0:25]
    print rabinFingerprint(test)[0]

    similiarity = computeSimiliary(hashShingle) # compute similarity
    print(similiarity)

