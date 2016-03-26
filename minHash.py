import random

def minHash(hashShingle,number):
    minHashFunction = []
    for i in range(number):
        minHashFunction.append(random.getrandbits(64))
    minHashShingle = [[] for i in range(len(hashShingle))]
    for i in range(len(hashShingle)):
        if hashShingle[i] == []:
            continue
        for j in range(number):
            otherHashShingle = []
            for z in range(len(hashShingle[i])):
                otherHashShingle.append(hashShingle[i][z]^minHashFunction[j])
            minHashShingle[i].append(min(otherHashShingle))
    return minHashShingle
