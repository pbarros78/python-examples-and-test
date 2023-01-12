def Fact(n):
    if n == 0:
        return 1
    else:
        f = n * Fact(n - 1)
        return f

def Fact_5():
    for i in range(5):
        print("Factorial de", i, "=", Fact(i))

print("================== Fact(n)")
n = 3
print("Factorial de", n, "=", Fact(n))

print()
print("================== Fact(hasta 5)")
Fact_5()