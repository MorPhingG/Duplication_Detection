
def extractBody(result):
    index = list() # record the index of "#"
    for i in range(len(result)):
        if(result[i]=="##########################################################\n"):
            index.append(i)
    body = list()
    stop = 5
    body.append(' '.join(result[2:stop-1])[6:-1])
    for i in index[1:-1]:
        body.append(' '.join(result[stop+3:i])[6:-1])
        stop = i
    return(body)