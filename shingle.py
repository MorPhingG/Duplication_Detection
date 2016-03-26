import re
import numpy as np

# input: list output: list

#method 1: k-length shingle
# extract the string of body, output subbody
def go_tokens(body):
    tokens = list()
    for i in range(body.__len__()):
        tokens.append(body[i].split())
    return tokens

# extract k-length shingle in one e-mail
def shingle(tokens,shinglelength):
    subbody = list()
    if len(tokens)%2 == 1:
		max_i = len(tokens) - shinglelength
    else:
		max_i = len(tokens) - shinglelength + 1

    for i in range(max_i+1):
		subbody.append([' '.join(tokens[i:i+shinglelength])])
    return subbody

# extract k-length shingle in many e-mails
def go_shingle(tokens,shinglelength):
    sub_body = list()
    for i in range(tokens.__len__()):
        value = shingle(tokens[i],shinglelength)
        sub_body.append(value)
    return sub_body
    sub_list = go_shingle(a)

#print go_shingle(go_tokens(body))[0]



#method2: k characters shingle
#get k characters in strings
def k_shingle(string, k):
    length = len(string)
    list_wtf = list()
    for i in range(length-k):
        list_wtf.append([string[i:i+k]])
    return list_wtf

#get k_characters in a string list
def go_k_shingle(list_a,k):
    length = list_a.__len__()
    sub_body = list()
    for i in range(length):
        sub_body.append(k_shingle(list_a[i],k))
    return sub_body

#k_list = go_k_shingle(body,5)[0]
#print k_list

#change multi-space into one space in a strings
def del_multiple_space(str):
    length = len(str)-2
    k=0
    i=0

    while (i<length-k):
        if (str[i] == ' ' and str[i+1] == ' '):
            str = str[:i] + str[i+1:]
            i -= 1
            k += 1
        i += 1
    return str

#change multi-space into one space in a string list
def go_del_multiple_space(list_a):
    length = list_a.__len__()
    mod_list = list()
    for i in range(length):
        mod_list.append(del_multiple_space(list_a[i]))
    return mod_list

#change the punctuation into space in a string list
def go_alert_to_space(list_a):
    length = list_a.__len__()
    mod_list = list()
    for i in range(length):
        mod_list.append(re.sub('[,?.*/+-]', ' ', list_a[i]))
    return mod_list


#mod_list = go_alert_to_space(body)
#del_mul = go_del_multiple_space(mod_list)


#calculate jaccard coefficient
def jaccard(strings_A,strings_B):
    intersect = {}
    count = 0
    shingle_A = shingle(strings_A)
    shingle_B = shingle(strings_B)


    for key in shingle_A:
	    frozenkey = frozenset(key)
	    intersect[frozenkey] = 0


    for key in shingle_B:
	    frozenkey = frozenset(key)
	    if frozenkey in intersect:
		    count = count +1
    if len(shingle_A) + len(shingle_B) == 0:
        r = 'N/A'
        dist = 'N/'
    else:
        r = float(count)/float(len(shingle_A)+len(shingle_B)-count)
        dist = 1-r
    #print "The Jaccard coeffecient is: ",r
    #print "the Jaccard Distance: ",dist

#jaccard(a[0],a[1])
def do_jaccard(list_A):
    i=0

    while(i<list_A.__len__()):
        j = i
        while (j<list_A.__len__()):
            coeffecient = jaccard(list_A[i],list_A[j])
            j += 1
        i += 1

#matrix_re = do_jaccard(a)
