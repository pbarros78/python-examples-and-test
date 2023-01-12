def strangeMerge(x,y):
   z = []
   i = 0
   j = 0
   while i < len(x) :
      while j < len(y):
         z.append(y[j])
         j = j + 1
      z.append(x[i])
      i = i + 1
   return z


lista1 = [6, 3, 5, 3, 2, 3]
lista2 = [4, 5, 5, 1, 1, 3]

res = strangeMerge(lista1,lista2)

print(res)

