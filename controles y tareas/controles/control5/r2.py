def jeroglifico(n):
   if n == 0 or n == 1:
      resultado = 1
   else:
      resultado = 1 + jeroglifico(n//2)
   return resultado



datos = [4, 14, 25]

i = 0
c = 1
while i<len(datos):
   m = jeroglifico(datos[i])
   c = c * m
   i = i + 2
   
print(c)

#15