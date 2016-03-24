
def computeSimiliary(hashShingle):
    union = list(set(hashShingle[0]).union(set(hashShingle[1])))   # computer union set
    intersection = list(set(hashShingle[0]).intersection(set(hashShingle[1]))) # computer intersection set
    similiarity = len(intersection)/len(union)
    return(similiarity)