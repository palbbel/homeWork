def encode(text, rot=0):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    code_text = ''
    if rot >= len(alpha):
        new_rot = rot - int(rot/len(alpha)) * len(alpha)
    else:
        new_rot = rot

    for k in text:
        if k.isalpha() == True:
            if k.isupper() == True:
                if alpha.index(k.lower()) + new_rot + 1 > len(alpha):
                    ind = alpha.index(k.lower()) + new_rot - len(alpha)
                    code_text += alpha[ind].upper()
                elif alpha.index(k.lower()) + new_rot + 1 <= len(alpha):
                    code_text += alpha[alpha.index(k.lower()) + new_rot].upper()

            elif k.islower() == True:
                if alpha.index(k.lower()) + new_rot + 1 > len(alpha):
                    ind = alpha.index(k.lower()) + new_rot - len(alpha)
                    code_text += alpha[ind]
                elif alpha.index(k.lower()) + new_rot + 1 <= len(alpha):
                    code_text += alpha[alpha.index(k.lower()) + new_rot]

        else:
            code_text += k

    return code_text


def decode(text, rot=0):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    decode_text = ''
    if rot >= len(alpha):
        new_rot = rot - int(rot/len(alpha)) * len(alpha)
    else:
        new_rot = rot

    for k in text:
        if k.isalpha() == True:
            if k.isupper() == True:
                if alpha.index(k.lower()) - new_rot < 0:
                    ind = alpha.index(k.lower()) + len(alpha) - new_rot
                    decode_text += alpha[ind].upper()
                elif alpha.index(k.lower()) - new_rot >= 0:
                    decode_text += alpha[alpha.index(k.lower()) - new_rot].upper()

            elif k.islower() == True:
                if alpha.index(k.lower()) - new_rot < 0:
                    ind = alpha.index(k.lower()) + len(alpha) - new_rot
                    decode_text += alpha[ind]
                elif alpha.index(k.lower()) - new_rot  >= 0:
                    decode_text += alpha[alpha.index(k.lower()) - new_rot]

        else:
            decode_text += k

    return decode_text



encode('Hello, Python3!',27)
#encode('Hello, Python3!',30)
encode("Gur pyrnare naq avpre gur cebtenz, gur snfgre vg'f tbvat gb eha. Naq vs vg qbrfa'g, vg'yy or rnfl gb znxr vg snfg.", 13)
encode('There is no programming language, no matter how structured, that will prevent programmers from making bad programs.', 25)
#encode('Ifmmp, Qzuipo3!',1)


decode('Gdkkn, Oxsgnm3!',26000000001)
decode("The cleaner and nicer the program, the faster it's going to run. And if it doesn't, it'll be easy to make it fast.",13)
decode('Sgdqd hr mn oqnfqzllhmf kzmftzfd, mn lzssdq gnv rsqtbstqdc, sgzs vhkk oqdudms oqnfqzlldqr eqnl lzjhmf azc oqnfqzlr.',25)

