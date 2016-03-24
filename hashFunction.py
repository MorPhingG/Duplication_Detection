
def hashFunction(shingleBody):
    hashShingle = [[] for i in range(len(shingleBody))]
    for i in range(len(shingleBody)):
        for j in range(len(shingleBody[0])):
            hashShingle[i].append(hash(shingleBody[i][j]))
    return(hashShingle)