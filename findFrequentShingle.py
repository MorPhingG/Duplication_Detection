from datasketch import MinHash, MinHashLSH
import rabinFingerprint as rf
import shingle as shingle
from preprocessing import extractBody


body = extractBody.extraBody('dtoEmails_1_0.txt')
shingle = shingle.go_shingle(shingle.go_tokens(body),20)

allshingle = []
for i in range(0, shingle.__len__()):
    for j in range(0, shingle[i].__len__()):
        allshingle.append(''.join(shingle[i][j]).split())

# Create MinHash objects
m = []
for i in range(0,allshingle.__len__()):
    m.append(MinHash(num_perm=128))


for i in range(allshingle.__len__()):
    for d in allshingle[i]:
        m[i].update(d.encode('utf8'))


# Create an MinHashLSH index optimized for Jaccard threshold 0.5,
# that accepts MinHash objects with 128 permutations functions
lsh = MinHashLSH(threshold=1, num_perm=128)

# Insert m into the index
for i in range(0, m.__len__()):
    lsh.insert("m%d"%i, m[i])

# Search all the frequent shingle which frequency bigger than 100
result = []
for i in range(0, m.__len__()):
    if len(lsh.query(m[i])) > 100:
        result.append(lsh.query(m[i]))

#Find the frequency of the shingle
index = []
for i in range(0,result.__len__()):
    tem = len(result[i])
    index.append(tem)
