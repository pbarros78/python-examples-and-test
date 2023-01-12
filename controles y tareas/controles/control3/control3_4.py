ciudad = 'seoul'

i = 0
res = ''
l = len(ciudad)
while i < len(ciudad) // 2 + 1:
   c = l - i - 1
   res = res + ciudad[i]
   res = res + ciudad[c]
   i = i + 1
# Recuerde que el print imprime sin comillas
# y que las mayúsculas y minúsculas son caracteres
# distintos
print(res)
#sleuoo
				