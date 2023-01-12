def misterio(a, b):
   if b == 0:
      return 0
   elif a == 0:
      return 1
   else:
      return misterio(a-1, b-1)


datos = [12, 33, 41, 37, 22, 29, 18, 45, 48, 36, 31, 7]
resp=[]

i = 0
c = ''
while i<len(datos)-1:
   m = misterio(datos[i], datos[i+1])
   c = str(m) +  c
   i = i + 1
   
print(c)

#00011010011