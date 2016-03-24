from loadData import *
from preprocessing import *
from hashFunction import *
from computeSimiliarity import *


if __name__ == "__main__":
    result = loadData("dtoEmails_1_0.txt") # load data
    body = extractBody(result) # extract body

    # compute shingle

    #shingleBody = computeShingle(body)

    shingleBody = [[] for i in range(2)]
    shingleBody[0]=['123','222','346','165']
    shingleBody[1]=['155','123','234','357']
    hashShingle = hashFunction(shingleBody) # create hash table

    # compute fingerprint

    similiarity = computeSimiliary(hashShingle) # compute similarity
    print(similiarity)

