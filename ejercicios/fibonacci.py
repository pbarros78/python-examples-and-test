def Fib(n):
    if n <= 1:
        return n
    else:
        f0 = Fib(n - 2)
        f1 = Fib(n - 1)
    return f0 + f1

def Fib_10():
    for i in range(10):
        print("Fibonacci de", i, "=", Fib(i))

print("================== Fib(n)")
n = 7
print("Fibonacci de", n, "=", Fib(n))

print()
print("================== Fib(hasta 5)")
Fib_10()