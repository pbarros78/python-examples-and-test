def ej1():
    i = 1
    while i < 10:
        i += 1
        print(i, end="")

def ej2():
    n = 5
    for i in range(n - 1):
        for j in range(n):
            print("*", end="")
        print()

def ej3():
    n = 5
    for i in range(n):
        for j in range(n):
            if i > j:
                print(" ", end="")
            else:
                print("*", end="")
        print()

def ej3_inv():
    n = 5
    for i in range(n, 0, -1):
        for j in range(n):
            if j < i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def tarea_a():
    n = 9
    for i in range(n - 1):
        for j in range(n):
            if i == n - 2:
                print("*", end="")
            else:
                if j == 0:
                    print("*", end="")
                if i > 0 and j == i:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

def tarea_b():
    n = 9
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print("*", end="")
            else:
                if j >= i and j <= n - 1 - i:
                    print("*", end="")
                elif i >= int(n / 2):
                    if j >= n - 1 - i and j <= i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
        print()

def tarea_c():
    n = 9
    for i in range(n):
        for j in range(n):
            if i == int(n / 2):
                print("*", end="")
            elif j == int(n / 2):
                print("*", end="")
            elif j == i or j == n - 1 - i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def tarea_4a():
    n = 7
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                print("*", end="")
            else:
                if j == 0 or j == n-1:
                    print("*", end="")
                elif j == i:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

def tarea_4b():
    n = 9
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                if j == int(n / 2):
                    print("*", end="")
                else:
                    print(" ", end="")
            else:
                if j >= i and j <= n - 1 - i:
                    print("*", end="")
                elif i >= int(n / 2):
                    if j >= n - 1 - i and j <= i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
        print()

#ej1()
#print()
#ej2()
#print()
#ej3()
#print()
#ej3_inv()
#print()
#tarea_a()
#print()
#tarea_b()
#print()
#tarea_c()
#print()
tarea_4a()
print()
#tarea_4b()