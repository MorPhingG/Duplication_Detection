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