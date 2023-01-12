
#Entrada

cant_filas = int(input("Ingrese la cantidad de filas: "))
cant_col = int(input("Ingrese la cantidad de columnas: "))

matriz =[]

i = 0
while i < cant_filas:

    fila = []
    j = 0
    while j < cant_col:

        num = int(input("Ingrese un numero: "))
        fila.append(num)
        j+=1
    matriz.append(fila)
    
    i+=1

fila =input("Ingrese los numeros de la fila separados por una coma y si desea terminar escriba 'FIN': ")

matriz2 = []

while fila.upper() != "FIN":

    lista = fila.split(",")

    i = 0
    while i < len(lista):
        lista[i] = int(lista[i])

        i+=1
    
    matriz2.append(lista)

    fila =input("Ingrese los numeros de la fila separados por una coma y si desea terminar escriba 'FIN': ")


#Procesamiento
print(matriz)
print(matriz2)
print()
matriz_final = []



fila1 = 0
while fila1 < len(matriz):

    col2=0
    nueva_fila = []
    #### Para los que estaban en clase preguntando ###
    #lo que les faltó es que los ciclos internos (los dos que vienen)
    #recorren los contadores al revés de lo que tenían
    #el siguiente while recorre col2 y el interno a col1
    # y no como lo tenían que era al contrario
    #solo les falto notar eso y el ejercicio terminaba
    while col2 < len(matriz[fila1]):
        
        col1= 0
        suma = 0
        
        
        while col1 < len(matriz2):
            
            suma += matriz[fila1][col1]*matriz2[col1][col2]
            
            col1+=1
        col2 +=1
        nueva_fila.append(suma)

    matriz_final.append(nueva_fila)
    fila1 +=1
    
#Salida

print(matriz_final)












