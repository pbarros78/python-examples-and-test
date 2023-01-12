def calc(text, base):
  i = 0
  vow = 'aeiou'
  cons = 'bcdefghijklmnopqrstuvwxyz'
  while i < len(text) :
    if text[i] in vow :
      base = base - -5
    elif text[i] in vow.upper():
      base = base + -5
    elif text[i] in cons :
      base = base - 7
    elif text[i] in cons.upper():
      base = base - 9
    else :
      base = base - -3
    i =  i + 1
  return base

text = 'erItreA'
base = 1

res = calc(text,base)

print("resp 4:", res)

				