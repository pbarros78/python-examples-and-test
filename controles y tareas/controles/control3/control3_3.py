s1 = '+'
s2 = '*'
n = 6

res = ''
i = 0
while i < n :
   j = 0
   while j < n - i:
      if j % 2 == 0 :
         res = res + s1
      else :
         res = res + s2
      j = j + 1
   res = res + '\n'
   i = i + 1

print(res)

				