def misteriosa(n,m,i):     
   if i >= 0 :
      if n[i] < m[i] :
         aux = n[i]
         n[i] = m[i]
         m[i] = aux
      return misteriosa(n,m,i-1)
   return [n,m]
   
data1 = [8, 16, -10, -20, 22]
data2 = [11, -1, -2, 12, 17]

aux = misteriosa(data1, data2, len(data1)-1)

data1 = aux[0]
data2 = aux[1]

i = 0
c = 0
while i < len(data2):
   m = data2[i]
   c = c + m
   i = i + 1
   
print(c)

#-6