<<<<<<< HEAD
import binascii


#split the string and store in array
def splitString(str, width):
    return [str[x:x+width] for x in range(0,len(str),width)]

# binary polynomials division
class binary1polynomials:
    #binary arithemtic on polynomials
    def __init__(self,expr):
        self.expr = expr
    def degree(self):
        return len(self.expr)
    def id(self):
        return [self.expr[i]%2 for i in range(len(self.expr))]
    def listToInt(self):
        #return int(reduce(lambda x,y: x+str(y), self.expr, ''))
        result = binary1polynomials.id(self)
        return int(''.join(map(str,result)))
    def divide(a,b): #a,b are lists like (1,0,1,0,0,1,....)
        a = binary1polynomials.listToInt(a); b = binary1polynomials.listToInt(b)

        bina = int(str(a),2); binb = int(str(b),2)
        a = min(bina,binb); b = max(bina,binb);

        g = []; bitsa = "{0:b}".format(a); bitsb = "{0:b}".format(b)
        difflen = len(str(bitsb)) - len(str(bitsa))

        c = a<<difflen

        #for bit in range(difflen):
        #for i,bit in enumerate(bitsa): #'bitsa' must be an integer base 2 before passing in
        while difflen >= 0 and b != 0:

            b = b^c #,a*int(bitsa[bit])
            lendif = abs(len(str(bin(b))) - len(str(bin(c))))
            c = c>>lendif
            difflen -= lendif

        z = "{0:b}".format(b)
        return z





#gemerate the fingerprint
#input list, output list
def rabinFingerprint(singlings):

    fingerPrint = []
    #generate random polynomial of degree 64
    p=[1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0]
    # for i in range(0,64):
    #     p.append(random.randrange(2))
    # print p
    for i in range(0,singlings.__len__()):
        chunk = str((singlings[i])[0])
        s_16 = binascii.b2a_hex(chunk)
        s_10 = int(s_16,16)
        s_2 = bin(s_10).replace('0b','')
        j = map(int,splitString(s_2,1))
        x = binary1polynomials(j)
        y = binary1polynomials(p)
        fingerPrint.append(binary1polynomials.divide(x,y))
=======
from rabin import Rabin, set_min_block_size, set_max_block_size, set_average_block_size

reached = []


def block_reached(start, length, fingerprint):
    # print '(%s, %s, %s)' % (start, length, fingerprint)
    reached.append((fingerprint))


r = Rabin()
r.register(block_reached)


def rabinFinger(subEmailBody):
    for i in range(0, subEmailBody.__len__()):
        chunk = str((subEmailBody[i])[0])
        set_min_block_size(chunk.__len__())
        set_max_block_size(chunk.__len__())
        set_average_block_size(chunk.__len__())
        r.update(subEmailBody[i][0])

    return reached


# def rabinFingerprint(emailBody):
#     fingerPrint = []
#     for i in range(0, len(emailBody)):
#         if len(emailBody[i]) > 0:
#             # print rabinFingerprint(test[i])
#             fingerPrint.append(rabinFinger(emailBody[i]))
#
#     return fingerPrint

def rabinFingerprint(emailBody):
    fingerPrint = []
    for i in range(0, 3):
        if len(emailBody[i]) > 0:

            fingerPrint.append(rabinFinger(emailBody[i]))
            global reached
            reached = []
>>>>>>> origin/master

    return fingerPrint