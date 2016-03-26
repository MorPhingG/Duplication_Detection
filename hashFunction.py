
def hashFunction(shingleBody):
    hashShingle = [[] for i in range(len(shingleBody))]
    for i in range(len(shingleBody)):
        for j in range(len(shingleBody[i])):
            hashShingle[i].append(hash(shingleBody[i][j][0]))
    return(hashShingle)
