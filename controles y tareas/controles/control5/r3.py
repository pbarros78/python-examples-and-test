def segundo_misterio(n,x,y):
   i = x
   c = ''
   while i < y :
      c = c + n[i]
      i = i + 1
   return c
      
def primer_misterio(n):
   if len(n) <= 2 :
      return n
   else:
      val = len(n)//2
      a = n[val]
      arriba = segundo_misterio(n,0,val)
      abajo = segundo_misterio(n,val+1,len(n))
      b = primer_misterio(arriba)
      c = primer_misterio(abajo)
      return a+c+b
      
data = 'west-debraberg'

c = primer_misterio(data)
print(c)

#bergabrtde-esw