def strangeMerge(x,y):
   z = []
   i = 0
   j = 0
   while i < len(x) or j < len(y):
      if j < len(y) :
         z.append(y[j])
         j = j + 1
      elif i < len(x) :
         z.append(x[i])
         i = i + 1
   return z

# ENTRADA
lista1 = [2, 1, 1, 1, 5]
lista2 = [2, 4, 3, 5, 6, 1]

# PROCESAMIENTO
res = strangeMerge(lista1,lista2)

# SALIDA
print("resp 6.a:", res)
