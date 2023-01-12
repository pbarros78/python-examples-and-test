def rep(car):
  i = 0
  alf = 'abcdefghijklmnopqrstuvwxyz'
  while i < len(alf):
    if car == alf[i] :
      pos = (i + 1) % len(alf)
      return alf[pos]
    i = i + 1
  return '_'


def proc(text):
  i = 0
  nText = ''
  while i < len(text):
    nText = nText + rep(text[i])
    i = i + 1
  return nText

entrada = 'egypt'

proceso = proc(entrada)

print("resp 2:", proceso)
				