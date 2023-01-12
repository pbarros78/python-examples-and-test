def Sum(n):
    if n == 0:
        return n
    else:
        sum = n + Sum(n -1)
    return sum

print(Sum(5))
