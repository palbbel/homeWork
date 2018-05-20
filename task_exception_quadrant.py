def get_quadrant_number(x, y):
    if x ==0 or y == 0:
        raise ValueError

    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    print('{}'.format(get_quadrant_number(x, y)))