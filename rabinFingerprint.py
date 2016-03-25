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

    return fingerPrint