def dec2bin(number):
    value = convert_dec(number, 2)
    return value


def dec2oct(number):
    value = convert_dec(number, 8)
    return value


def dec2hex(number):
    value = convert_dec(number, 16)
    return value


def bin2dec(number):
    value = convert2dec(number, 2)
    return value


def oct2dec(number):
    value = convert2dec(number, 8)
    return value


def hex2dec(number):
    value = convert2dec(number, 16)
    return value


def convert_dec(number, bit_capacity):
    value = ''
    while number >= 1:
        remainder = (number % bit_capacity)
        if bit_capacity == 16:
            if len(str(remainder)) > 1:
                remainder = map_hex(str(remainder))
        number = (number // bit_capacity)

        value = value + str(remainder)

    value = str(value)[::-1]
    return value


def convert2dec(number, bit_capacity):
    value = 0
    string_number = str(number)
    len_number = len(string_number)
    for i in list(range(len_number)):
        if string_number[i].isalpha():
            int_number = int(map_hex(str(string_number[i])))
        else: int_number = int(string_number[i])

        value += int_number * bit_capacity ** (len_number-int(i)-1)

    return value


def map_hex(val):
    dict = {'a': '10',
            'b': '11',
            'c': '12',
            'd': '13',
            'e': '14',
            'f': '15',
            '10': 'a',
            '11': 'b',
            '12': 'c',
            '13': 'd',
            '14': 'e',
            '15': 'f'
            }
    return dict.get(val)


