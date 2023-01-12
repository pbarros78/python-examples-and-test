'''
Dado un arreglo de números enteros, se debe ordenar utilizando algún algoritmo
de ordenamiento:
'''

# swap = intercambiar => cambia el orden de los valores de 2 variables (a y b)
# La variable a tomará el valor de la variable b y la varible b tomará el valor
# de la variable a para ello se necesita de una tercera variable que guarde el
# valor de una de éstas.
def swap(a, b):
    temporal = a
    a = b
    b = temporal
    return a, b

# Igual que de arriba, pero enfocado a arreglos (devuelve el arreglo con los
# valores cambiados), el de arriba sólo devuelve los valores cambiados
def swap_arreglo(arreglo, indice_1, indice_2):
    temporal = arreglo[indice_1]
    arreglo[indice_1] = arreglo[indice_2]
    arreglo[indice_2] = temporal

# Ordenamiento Burbuja:
# Funciona revisando cada elemento de la lista/arreglo con el siguiente
# intercambiándolos si están orden equivocado.
# https://es.wikipedia.org/wiki/Ordenamiento_de_burbuja
# Ordenamiento Burbuja usando while
def burbuja_while(a):
    # Hago una copia del arreglo original a, para poder modificar la copia y NO
    # el original, así se podría usar para otras operaciones
    a2 = list(a)
    # Obtengo el largo (real) del arreglo y le resto 1 porque los índices de los
    # arreglos/listas comienzan en 0, no en 1.
    largo = len(a2) - 1
    i = 0
    while i < largo:
        j = 0
        while j < largo - i:
            if (a2[j] > a2[j + 1]):
                # Para usar la función swap, se debe pasar el arreglo en un
                # índice, y el arreglo en el otro índice
                #a2[j], a2[j + 1] = swap(a2[j], a2[j + 1])
                # Uso el swap de arreglo para no devolver/tomar los valores
                swap_arreglo(a2, j, j + 1)
            j += 1
        i += 1
    return a2

# Ordenamiento Burbuja usando for
def burbuja_for(a):
    a2 = list(a)
    largo = len(a2) - 1
    for i in range(largo):
        for j in range(largo - i):
            if (a2[j] > a2[j + 1]):
                swap_arreglo(a2, j, j + 1)
    return a2

# Ordenamiento de Selección:
# Su funcionamiento es el siguiente:
# - Buscar el mínimo elemento de la lista
# - Intercambiarlo con el primero
# - Buscar el siguiente mínimo en el resto de la lista
# - Intercambiarlo con el segundo
# Y en general:
# - Buscar el mínimo elemento entre una posición i y el final de la lista
# - Intercambiar el mínimo con el elemento de la posición i
# https://es.wikipedia.org/wiki/Ordenamiento_por_selecci%C3%B3n
def seleccion(a):
    a2 = list(a)
    largo = len(a2)
    for i in range(largo):
        # Tomamos el índice del primer valor (arreglo en índice i) como el más pequeño
        menor_en_indice = i
        # Acá se recorren los valores a la derecha
        for j in range(i + 1, largo):
            if (a2[j] < a2[menor_en_indice]):
                menor_en_indice = j
        # Intercambia el valor menor encontrado en j, con el menor del índice i
        swap_arreglo(a2, menor_en_indice, i)
    return a2

# Ordenamiento de Inserción:
# Funciona de manera más natural para un ser humano, este toma el siguiente
# elemento de una lista y lo va comparando con los anteriores, similar a como
# orenaríamos un mazo de cartas.
# https://es.wikipedia.org/wiki/Ordenamiento_por_inserci%C3%B3n
def insercion(a):
    a2 = list(a)
    largo = len(a2)
    for i in range(1, largo):
        # Tomamos el valor del primer índice (i) como el menor
        valor_a_insertar = a2[i]
        # Guardamos en j el índice del elemento anterior
        j = i - 1
        # Movemos todos los elementos del arreglo hacia adelante (derecha) si
        # son mayores que el elemento a insertar
        while j >= 0 and a2[j] > valor_a_insertar:
            a2[j + 1] = a2[j]
            j -= 1
        # Insertamos el valor
        a2[j + 1] = valor_a_insertar
    return a2

# arreglo original
arreglo = [5, 9, 10, 3, 1, 7, 8, 2, 0]

print("Arreglo sin ordenar:", arreglo)
arreglo2 = burbuja_while(arreglo)
print("Arreglo ordenado con burbuja_while:", arreglo2)
print()
print("Arreglo sin ordenar:", arreglo)
arreglo3 = burbuja_for(arreglo)
print("Arreglo ordenado con burbuja_for:", arreglo3)
print()
print("Arreglo sin ordenar:", arreglo)
arreglo4 = seleccion(arreglo)
print("Arreglo ordenado con seleccion:", arreglo4)
print()
print("Arreglo sin ordenar:", arreglo)
arreglo4 = insercion(arreglo)
print("Arreglo ordenado con insercion:", arreglo4)
