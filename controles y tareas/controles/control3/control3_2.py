ciudad = 'lagos'
alfa = 'abcdefghijklmnopqrstuvwxyz'
cif = 3
i = 0
res = ''
while i < len(ciudad):
    # Index retorna el índice del elemento
    # en el string
    if ciudad[i] in alfa:
        p = alfa.index(ciudad[i])
        pos = (p + cif) % len(alfa)
        aux = alfa[pos]
    else:
        aux = '_'
    if i > cif:
        res = aux + res
    else:
        res = res + aux
    i = i + 1
    
    
# Recuerde que el print imprime sin comillas
# y que las mayúsculas y minúsculas son caracteres
# distintos
print(res)
#vodjr
				