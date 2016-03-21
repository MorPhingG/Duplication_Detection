# load data
f = open("dtoEmails_1_0.txt")
result = list()
while 1:
    line = f.readline()
    # print(line)
    result.append(line)
    if not line:
        break
print(result[0:100])
f.close()

# preprocessing

# extract body
index = list() # record the index of "#"
for i in range(result.__len__()):
    if(result[i]=="##########################################################\n"):
        index.append(i)
body = list()
stop = 5
body.append(' '.join(result[2:stop-1])[6:end])
for i in index[1:-1]:
    body.append(' '.join(result[stop+3:i])[6:end])
    stop = i

# compute shingle

# listtostr
def listToStr(list):
    newList = list()
    length=list.__len__
    for i in range(length):
        newList = newList + list[i]
    return(newList)
