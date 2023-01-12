def strangeMerge(x,y):
   z = []
   i = 0
   while i < len(x) :
      j = 0
      foo = False
      while j < len(y):
         if y[j] == x[i] :
            foo = True
         j = j + 1
      if foo and x[i] not in z :
         z.append(x[i])
      i = i + 1
   return z


lista1 = [6, 3, 5, 3, 2, 3]

lista2 = [4, 5, 5, 1, 1, 3]

res = strangeMerge(lista1,lista2)

print("resp 5.b:", res)
