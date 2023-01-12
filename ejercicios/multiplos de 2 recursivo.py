def multiplos(n):
    if n == 0:
        print("Multiplo de 2 x", n, "=", n * 2)
    else:
        print("Multiplo de 2 x", n, "=", n * 2)
        multiplos(n - 1)

def multiplos_2(n):
    print("Multiplo de 2 x", n, "=", n * 2)
    if n > 0:
        multiplos_2(n - 1)

print("Multiplos con función recursiva normal")
print("======================================")
multiplos(20)

print("\nMultiplos con función recursiva simplificada")
print("============================================")
multiplos_2(20)
