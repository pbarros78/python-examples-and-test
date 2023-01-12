def swap_a(data):
  i = 0
  while i < len(data):
    j = 0
    while j < len(data[i]):
      k = len(data)
      if j < k // 2 :
        aux = data[i][j]
        data[i][j] = data[i][k-j-1]
        data[i][k-j-1] = aux
      j = j + 1
    i = i + 1
  return data

def swap_b(data):
  i = 0
  while i < len(data):
    j = 0
    while j < len(data[i]):
      if i < j :
        aux = data[j][i]
        data[j][i] = data[i][j]
        data[i][j] = aux
      j = j + 1
    i = i + 1
  return data

def swap_c(data):
  i = 0
  while i < len(data):
    j = 0
    while j < len(data[i]):
      if i > j :
        data[i][j] = data[j][i]
      j = j + 1
    i = i + 1
  return data

def swap_d(data):
  i = 0
  while i < len(data) :
    j = 0
    while j < len(data[i]):
      aux = data[j][i]
      data[j][i] = data[i][j]
      data[i][j] = aux
      j = j + 1
    i = i + 1
  return data

def swap_e(data):
  i = 0
  while i < len(data):
    j = 0
    while j < len(data[i]):
      if i < j :
        data[i][j] = data[j][i]
      j = j + 1
    i = i + 1
  return data

def swap_f(data):
  i = 0
  while i < len(data):
    j = 0
    while j < len(data[i]):
      k = len(data)
      if i < k // 2 :
        aux = data[i][j]
        data[i][j] = data[k-i-1][j]
        data[k-i-1][j] = aux
      j = j + 1
    i = i + 1
  return data

def read(nomArch):
  arch = open(nomArch, 'r')
  content = arch.read()
  arch.close()
  return content

def toList(data):
  data = data.split('\n')
  i = 0
  while i < len(data):
    data[i] = data[i].split(' ')
    j = 0
    while j < len(data[i]):
      data[i][j] = int(data[i][j])
      j = j + 1
    i = i + 1
  return data
  
# AQUÍ DEBERÍA IR swap()

def toString(data):
  text = ''
  i = 0
  while i < len(data):
    j = 0
    aux = ''
    while j < len(data[i]):
      e = data[i][j]
      aux = aux + str(e) + ' ' 
      j = j + 1
    i = i + 1
    text = text + aux.strip(' ')
    text = text + '\n'
  return text.strip('\n')

def write(nomArch,content):
  arch = open(nomArch, 'w')
  arch.write(content)
  arch.close()
  return 0

# ENTRADA
aux = read('3inFile.txt')

# PROCESAMIENTO
aux = toList(aux)
aux1 = swap_b(aux)
aux2 = toString(aux1)

# SALIDA
write('outFile.txt',aux2)

#b