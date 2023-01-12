#1
#a=====================================
val = '10011010'

acum = 0
i = 1
while i < len(val):
    aux = 2 ** (len(val) - i)
    num = int(val[i]) * aux
    acum = acum + num
    i = i + 1

if int(val[0]) != 1:
    acum = acum * -1

print('a', acum)
#b======================================
val = '10011010'

acum = 0
i = 1
while i < len(val):
    num = int(val[i]) * 2 ** i
    acum = acum + num
    i = i + 1

if int(val[0]) != 1:
    acum = acum * -1

print('b', acum)
#c======================================
val = '10011010'

acum = 0
i = 1
while i < len(val):
    aux = 2 ** (len(val) - i)
    num = int(val[i]) * aux
    acum = acum + num
    i = i + 1

if int(val[0]) == 1:
    acum = acum * -1

print('c', acum)
#d======================================
val = '10011010'

acum = 0
i = 1
while i < len(val):
    aux = 2 ** (len(val) - i - 1)
    num = int(val[i]) * aux
    acum = acum + num
    i = i + 1

if int(val[0]) == 1:
    acum = acum * -1

print('d', acum)
#e======================================
val = '10011010'

acum = 0
i = 1
while i < len(val):
    num = int(val[i]) * 2 ** i
    acum = acum + num
    i = i + 1

if int(val[0]) == 1:
    acum = acum * -1

print('d', acum)

