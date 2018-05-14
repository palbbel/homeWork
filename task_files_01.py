n = int(input())
p = int(input())

with open('data.txt') as f:
    list_line = f.read().split(' ')

with open('out-1.txt', 'w') as f1:
    with open('out-2.txt', 'w') as f2:
        for val in list_line:
            val = int(val)
            if val % n == 0:
                f1.write('{}{}'.format(val, ' '))
            f2.write('{}{}'.format(val ** p, ' '))


