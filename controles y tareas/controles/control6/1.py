def read(fileName):
  file = open(fileName,'r')
  fin = []
  vow = 'aeiou'
  con = 'bcdfghjklmnpqrstvwxyz'
  for lin in file :
    text = ''
    for wor in lin :
      if wor in con:
        text = text + wor
      if wor.lower() in vow :
        text = text + wor
    fin.append(text.lower())
  file.close()
  return fin

def calc(array):
  res = 0
  vow = 'aeiou'
  con = 'bcdfghjklmnpqrstvwxyz'
  for text in array :
    for car in text :
      if car.lower() in vow :
        res = res + 1
      elif car.lower() in con :
        res = res - 1
      else : 
        res = res * 2
  return res

def scramble(array):
  newArr = []
  for text in array :
    newText = ''
    for car in text :
      if car.upper() not in newText :
        newText = newText + car
      elif car.lower() not in newText :
        newText = newText + car
    newArr.append(newText)
  return newArr

# BLOQUE PRINCIPAL
# ENTRADA
inp = read('1students.txt')
# PROCESAMIENTO
aux = scramble(inp)
res = calc(aux)
# SALIDA
print(res)

# -1