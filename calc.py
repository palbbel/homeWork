def convert(st=None):
    st_list = []
    chislo = ''
    out_str = ''
    out_list = []
    stack = []

    list_operand = ['(', ')', '+', '-', '*', '/', '|', '^', '%']
    dict_priority = {
        '^': 1,
        '*': 2,
        '/': 2,
        '|': 2,
        '%': 2,
        '+': 3,
        '-': 3
    }

    st = st.replace(' ', '').replace('//','|')
    chislo = ''
    for val in st:
        if val.isdigit() == True:
            chislo += val

        else:
            if chislo != '':
                st_list.append(chislo)
                chislo = ''
            if chislo == '':
                st_list.append(val)
    if chislo != '':
        st_list.append(chislo)

    for val in st_list:
        if val in list_operand:
            if len(stack) == 0 and val != ')':
                stack.append(val)
            else:
                if val == '(':
                    stack.append(val)
                elif stack[len(stack) - 1] == '(':
                    stack.append(val)

                elif val == ')':
                    while 1:
                        if len(stack) == 0:
                            break
                        if stack[len(stack) - 1] == '(':
                            stack.pop()
                            break
                        else:
                            out_list.append(stack[len(stack) - 1])
                            stack.pop()

                elif int(dict_priority.get(val)) < int(dict_priority.get(stack[len(stack) - 1])):
                    stack.append(val)
                elif int(dict_priority.get(val)) >= int(dict_priority.get(stack[len(stack) - 1])):
                    while 1:
                        out_list.append(stack[len(stack) - 1])
                        stack.pop()
                        if len(stack) == 0:
                            break
                        if stack[len(stack) - 1] == '(':
                            break
                        elif int(dict_priority.get(val)) < int(dict_priority.get(stack[len(stack) - 1])):
                            break
                    stack.append(val)

        else:
            out_list.append(val)

    while 1:
        if len(stack) != 0:
            if stack[len(stack) - 1] != '(':
                out_list.append(stack[len(stack) - 1])
                stack.pop()
            elif stack[len(stack) - 1] == '(':
                stack.pop()
        else:
            break

    for rec in out_list:
        if rec == '|':
            rec = '//'
        if rec != '':
            out_str = out_str + '{}{}'.format(rec, ' ')

    out_str = out_str.strip()
    #print(out_str)
    return out_str


def calc(str=None):
    list_operand = ['+', '-', '*', '/', '//', '^', '%']
    value = convert(str)
    value_list = value.split(' ')
    resal = None
    while 1:
        flag = False
        i = -1
        if resal:
            break
        if value_list[1] == '-':
            value_list.insert(0, '0')
        for val in value_list:
            if flag == False:
                i += 1
                if val in list_operand and i not in [0,1]:
                    if val == '+':
                        resault = float(value_list[i-2]) + float(value_list[i-1])
                    elif val == '-':
                        resault = float(value_list[i - 2]) - float(value_list[i - 1])
                    elif val == '*':
                        resault = float(value_list[i - 2]) * float(value_list[i - 1])
                    elif val == '/':
                        resault = float(value_list[i - 2]) / float(value_list[i - 1])
                    elif val == '//':
                        resault = float(value_list[i - 2]) // float(value_list[i - 1])
                    elif val == '%':
                        resault = float(value_list[i - 2]) % float(value_list[i - 1])
                    elif val == '^':
                        resault = float(value_list[i - 2]) ** float(value_list[i - 1])

                    value_list.pop(i)
                    value_list.pop(i-1)
                    value_list.pop(i-2)
                    b = i-2
                    value_list.insert(b, resault)
                    if len(value_list) == 1:
                        resal = float(value_list[0])
                    else:
                        flag = True



    #print(resal)
    return resal


if __name__ == '__main__':
    #str = (input(':'))
    calc(input(':'))