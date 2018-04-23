def encode(text, rot=0):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    code_text = ''
    if rot > len(alpha):
        new_rot = rot - int(rot/len(alpha)) * len(alpha) - 1
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
    if rot > len(alpha):
        new_rot = rot - int(rot/len(alpha)) * len(alpha) - 1
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



