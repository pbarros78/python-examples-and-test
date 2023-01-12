def leer(nombre):
  cont = []
  archivo = open(nombre,'r')
  lista = archivo.read().split('\n')
  i = 0
  while i < len(lista):
    e = lista[i].split(' ')
    cont = cont + e 
    i = i + 1
  archivo.close()
  return cont

def selec(lista):
  ele1 = len(lista[0])
  ele2 = len(lista[0])
  salida = ['','']
  i = 0
  while i < len(lista):
    if len(lista[i]) < ele1 :
      ele1 = len(lista[i])
      salida[0] = lista[i]
    if len(lista[i]) > ele2 :
      salida[1] = lista[i]
      ele2 = len(lista[i])
    i = i + 1
  return salida

def jer(lista,letra):
  fin = ''
  vocales = 'aeiou'
  i = 0
  while i < len(lista):
    j = 0
    pal = lista[i]
    while j < len(pal):
      if pal[j] not in vocales :
        pos = len(pal) % len(vocales)
        v = vocales[pos]
        fin = fin + pal[j] + v
      else :
        fin = fin + letra + pal[j]
      j = j + 1
    i = i + 1      
  return fin

# BLOQUE PRINCIPAL
# ENTRADA
consonantes = 'bcdfghjklmnpqrstvwxyz'
nombres = leer('2nombres.txt')

# PROCESAMIENTO
if nombres[0][0] in consonantes :
  letra = nombres[0][0]
else :
  posicion = len(nombres[0]) % 21
  letra = consonantes[posicion]


resultado = selec(nombres)
salida = jer(resultado, letra)

# SALIDA
print(salida)

#LalaluralaFurulanuculesucula