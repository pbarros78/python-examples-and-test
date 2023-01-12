def pop(lista):
  i = 0
  nLista = []
  while i < len(lista):
    if lista[i] >= lista[len(lista)//2] :
      x = lista.pop(i)
      nLista.append(x)
    else :
      i = i + 1
  return nLista

def weirdCalc(lista):
  i = 0
  acum = 0
  while i < len(lista):
    if i % 2 == 0 :
      acum = acum + lista[i]
    else :
      acum = acum + lista[i] // 10
    i = i + 1

  return acum

entrada = [93, 59, 63, 98, 50, 45, 39, 73, 77, 58]

aux = pop(entrada)

calc = weirdCalc(aux)

print("resp 1:", calc)
