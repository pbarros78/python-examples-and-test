def swap1(c):
  dig = '9876543210'
  c = dig[int(c)] * 2
  c = int(c) // 10
  c = str(c)
  return c

def swap2(c) :
  c = int(c)
  c = c ** 2
  c = c // 10
  c = str(c)
  return c

def scramble(num):
  lista = list(num)
  i = len(lista) - 1
  j = 0
  while i > 0 and j < len(lista):
    aux = swap2(lista[j])
    lista[j] = swap1(lista[i])
    lista[i] = aux
    
    j = j + 1
    i = i // 2
  return lista

def consolidate(lista):
  i = 0
  txt = ''
  while i < len(lista):
    txt = txt + lista[i]
    i = i + 1

  return txt

entrada = '74558494'

entrada = scramble(entrada)

entrada = consolidate(entrada)

print("resp 3:", entrada)
				