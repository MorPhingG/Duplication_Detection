
def computeSimilarity(hashShingle):
    similarity = [[] for i in range(len(hashShingle))]
    for i in range(len(similarity)):
        if(hashShingle[i] == []):
            continue
        for j in range(len(similarity)):
            if(hashShingle[j] == []):
                similarity[i].append(0)
                continue
            union = list(set(hashShingle[i]).union(set(hashShingle[j])))   # computer union set
            intersection = list(set(hashShingle[i]).intersection(set(hashShingle[j]))) # computer intersection set
            similarity[i].append(len(intersection)/len(union))
    return(similarity)

def computeSimilarity2(string1,string2):
    union = list(set(string1).union(set(string2)))   # computer union set
    intersection = list(set(string1).intersection(set(string2))) # computer intersection set
    return(len(intersection)/len(union))