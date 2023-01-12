# Se ingresa un string (cadena de texto) con números separados por espacio (" ")
numeros_en_string = input("Ingrese una serie de números separados por espacio: ")

# Con for
# split separa el texto por lo que indica el parámetro (valor) dentro de split
# En este caso el texto (números) por espacio y crea una lista o arreglo con
# cada valor que no sea espacio
lista_numeros_en_string = numeros_en_string.split(" ")
# Recorremos la lista hasta su largo
for i in range(len(lista_numeros_en_string)):
    # Preguntamos si el valor de la lista en la posición i es un número
    if lista_numeros_en_string[i].isdigit():
        # Si es un número (pero está como string) se convierte en entero para poder elevarlo
        # al cuadrado, y después nuevamente se convierte a texto y se asigna a la lista en
        # su posición i (se reemplaza el valor)
        lista_numeros_en_string[i] = str(int(lista_numeros_en_string[i]) ** 2)
        # Se podría hacer también de la siguiente forma:
        # numero = int(lista_numeros_en_string[i]) ** 2
        # resultado_string = str(numero)
        # lista_numeros_en_string[i] = resultado_string

# Unimos con join la lista y le decimos en que entre cada valor le ponga una coma y espacio (, )
print(', '.join(lista_numeros_en_string))

# Con while
lista_numeros_en_string = numeros_en_string.split(" ")
i = 0
while i < len(lista_numeros_en_string):
    if lista_numeros_en_string[i].isdigit():
        lista_numeros_en_string[i] = str(int(lista_numeros_en_string[i]) ** 2)
    i = i + 1

print(', '.join(lista_numeros_en_string))

# Sin split ni join ni lista - con while
# Usaremos un string para guardar los valores
lista_numeros_en_string = ""
i = 0
while i < len(numeros_en_string):
    # Preguntamos si el valor del texto en la posición i no es espacio
    if numeros_en_string[i] != " ":
        # Preguntamos si el valor del texto está dentro del rango de números (48 al 57 en la tabla ascii)
        # https://www.tecnologia-informatica.com/que-es-codigo-ascii/#:~:text=El%20ASCII%20es%20un%20c%C3%B3digo,a%20uno%20de%20estos%20c%C3%B3digos.
        if numeros_en_string[i] >= '0' and numeros_en_string[i] <= '9':
            # Hacemos la operación y la asignamos a la variable numero
            numero = int(numeros_en_string[i]) ** 2
            # Si la posicón i > 0, agregamos el coma y espacio (no es el primer número)
            if i > 0:
                lista_numeros_en_string = lista_numeros_en_string + ", " + str(numero)
            # Si es la posición 0, no se agrega coma y espacio
            else:
                lista_numeros_en_string = lista_numeros_en_string + str(numero)
    i = i + 1

print(lista_numeros_en_string)
