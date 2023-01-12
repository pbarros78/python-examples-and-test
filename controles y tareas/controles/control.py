#1)
a = not (6 * 9) != (12 * 4) or (3 % 3) != (11 * 1) and (4 * 7) == (7 % 11)
b = not (10 // 11) == (9 //3) and (9 - 7) < (8 // 2) and not (-3 - 13) > (2 // 9)
print (a, b)

#2)
x = -2
y = 10
z = 8
res = x - (y // z)
if x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    res = res - x
if x % 2 != 0 or y % 2 != 0 or z % 2 != 0:
    res = res - x
if x % 3 != 0 and y % 3 != 0 and z % 3 != 0:
    res = res * y
if x % 3 != 0 or y % 3 != 0 or z % 3 != 0:
    res = res - y
if x % 5 != 0 and y % 5 != 0 and z % 5 != 0:
    res = res * z
if x % 5 != 0 or y % 5 != 0 or z % 5 != 0:
    res = res - z
print('res:', res)

#3)
num = 1110
acum = 0
i = 0
while num > 0:
    print("\ncon i =", i)
    c = num % 10
    print("c:", c)
    num = num // 10
    print("num:", num)
    acum = acum + c * 5 ** i
    print("acum:", acum)
    i = i + 1
print("res: ", acum)

#4)
num = 714718
i = 0
while num > 10:
    print("\ncon i =", i)
    aux = 0
    print("aux:", aux)
    while num > 0:
        i = i + 1
        print("i:", i)
        c = num % 10
        print("c:", c)
        num = num // 10
        print("num:", num)
        aux = aux + c
        print("aux:", aux)
    if aux >= 10:
        num = aux
        print("num:", num)
print(aux)

#5)
num = 7416
i = 0
while num > 0:
    print("\ncon i =", i)
    print("i % 5 = ", i % 5)
    if i % 5 == 0:
        num = num - 3
    else:
        num = num // 4
    print("num:", num)
    i = i + 1
print(i)

#6)
num = 513006
acum = 0
c = 0
while num > 0:
    num = num // 10
    print("\nnum:", num)
    c = num % 10
    print("c:", c)
    acum = acum * 10 + c
    print("acum:", acum)
print('res:', acum)
