def leer(nombre):
  archivo = open(nombre, 'r')
  contenido = archivo.read()
  archivo.close()
  return contenido

def convertirALista(contenido):
  contenido = contenido.split('\n')
  i = 0
  while i < len(contenido):
    contenido[i] = contenido[i].split(' ')
    j = 0
    while j < len(contenido[i]):
      contenido[i][j] = int(contenido[i][j])
      j = j + 1
    i = i + 1
  return contenido
  
def mover(matriz):
  i = 0
  while i < len(matriz) :
    j = 0
    while j < len(matriz[i]):
      aux = matriz[j][i]
      matriz[j][i] = matriz[i][j]
      matriz[i][j] = aux
      j = j + 1
    i = i + 1
  return matriz

def convertirAString(contenido):
  texto = ''
  i = 0
  while i < len(contenido):
    j = 0
    aux = ''
    while j < len(contenido[i]):
      caracter = contenido[i][j]
      aux = aux + str(caracter) + ' ' 
      j = j + 1
    i = i + 1
    texto = texto + aux.strip(' ')
    texto = texto + '\n'
  return texto.strip('\n')

def escribirArchivo(nombre,contenido):
  archivo = open(nombre, 'w')
  archivo.write(contenido)
  archivo.close()
  return 1

# ENTRADA
entrada = leer('4matrizEntrada.txt')

# PROCESAMIENTO
entrada = convertirALista(entrada)
entrada = mover(entrada)
entrada = convertirAString(entrada)

# SALIDA
i = escribirArchivo('matrizSalida.txt',entrada)
if i == 1 :
  print('El archivo se escribió con éxito')
else :
  print('No debería estar leyendo este print')

#c