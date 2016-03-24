# load data
def loadData(filenames):
    f = open(filenames)
    result = list()
    while 1:
        line = f.readline()
        result.append(line)
        if not line:
            break
    return result