def fibonacci(n):
    x, y = 1, 1
    while n:
        yield x
        x, y = y, x + y
        n -= 1

if __name__ == '__main__':
    n = int(input())
    for i in fibonacci(n):
        print(i)
