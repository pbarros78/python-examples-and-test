def cata1(n):
    if n == 0:
        return 1
    else:
        c = 1
        i = 1
        while i < n:
            c = int((2 * (2 * i + 1) * c) / (i + 2))
            i = i + 1
    return c

def cata2(n):
    if n == 0:
        return 1
    else:
        c = 0
        i = 0
        while i < n:
            c = c + cata2(i) * cata2(n - 1 - i)
            i = i + 1
    return c

print(cata1(0))
print(cata1(1))
print(cata1(2))
print(cata1(3))
print(cata1(4))
print(cata1(5))
print(cata1(6))
print()
print(cata2(0))
print(cata2(1))
print(cata2(2))
print(cata2(3))
print(cata2(4))
print(cata2(5))
print(cata2(6))
