ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())
cx = int(input())
cy = int(input())

# Определяем координаты векторов
ab = (bx - ax, by - ay)
ac = (cx - ax, cy - ay)

ba = (ax - bx, ay - by)
bc = (cx - bx, cy - by)

ca = (ax - cx, ay - cy)
cb = (bx - cx, by - cy)

# Проверка на нулевые веутора
if  (ab[0] == 0 and ab[1] == 0) or (ac[0] == 0 and ac[1] == 0) or \
    (ba[0] == 0 and ba[1] == 0) or (bc[0] == 0 and bc[1] == 0) or \
    (ca[0] == 0 and ca[1] == 0) or (cb[0] == 0 and cb[1] == 0):
    print('no')
else:
    # Находим скалярные произведения ненулевых векторов
    a = ab[0] * ac[0] + ab[1] * ac[1]
    b = ba[0] * bc[0] + ba[1] * bc[1]
    c = ca[0] * cb[0] + ca[1] * cb[1]

    if a == 0 or b == 0 or c == 0:
        print('yes')
    else:
        print('no')













