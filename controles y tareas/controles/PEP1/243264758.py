# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: C-3
# PROFESOR DE TEORÍA: Alejandro Cisterna Villalobos
# PROFESOR DE LABORATORIO: José Gonzalez
# 
# AUTOR 
# NOMBRE: Arina Bilan
# RUT: 24.326.475-8
# CARRERA: Ingeniería Cicil en Informática
# El programa hace un registro del tiempo de las vueltas de un piloto, muestra un resumen con el mejor y peor tiempo, y las calificaciones que sacaría según el registro de la competencia anterior.

# Antecedente: Hice pruebas de comparaciones (>, <, ==) con strings con el formato indicado (mm:ss,ms) y funcionaron, por lo tanto no vi necesario convertir las entradas a otro formato.
# Restricciones, se presume que no demorará más de 99:59,999 una vuelta, no acepta más de ese tiempo

# Registros/records de la competencia anterior
registro_oro = '05:47,914'
registro_plata = '06:01,013'
registro_bronce = '06:03,607'

vueltas = int(input('Ingrese la cantidad de vueltas al circuito: '))

# Lista para guardar los tiempos
tiempo_vuelta = []
i = 0
while i < vueltas:
    # Esto es para validar la entrada
    correcto = True

    # Concatenación de texto para el ingreso de valores, el i + 1 es para que no empiece desde cero (visualmente)
    texto = 'Ingrese el tiempo de la vuelta ' + str(i + 1) + ' en formato mm:ss,ms (ej:07:40,123): '
    tiempo = input(texto)
    
    # Validaciones del formato
    if len(tiempo) < 8:
        correcto = False
    else:
        # Revisa si lleva :
        if tiempo[1] != ':':
            if tiempo[2] != ':':
                correcto = False
        else: # Si lleva : pero ingreso sólo un dígito en minutos, se agrega un 0 para las comparaciones
            tiempo = '0' + tiempo
        
        # Revisa si lleva ,
        if tiempo[5] != ',':
            correcto = False
        
        # Revisa segundos y milisegundos
        if correcto:
            partes = tiempo.split(':')
            minutos = partes[0]
            seg_ms = partes[1]
            partes_2 = seg_ms.split(',')
            segundos = partes_2[0]
            milisegundos = partes_2[1]
            if int(segundos) > 59:
                correcto = False
            if int(milisegundos) > 999:
                correcto = False

    if correcto == False:
        print('¡El formato ingresado no es válido!, ingrese el formato mm:ss,ms (ej:07:40,123)')
    else:
        tiempo_vuelta.append(tiempo)
        i += 1
print()

# Aparece en el PDF de Listas
tiempo_vuelta.sort()

# Variables a las que se le asignará los valores menores y mayores de los tiempos
# Como la lista se ordenó (sort), el primer registro es el menor
tiempo_menor = tiempo_vuelta[0]
# Y el último es el mayor
tiempo_mayor = tiempo_vuelta[len(tiempo_vuelta) - 1]

# Variables a las que se les irá sumando las medallas según los registros anteriores
cant_oro = 0
cant_plata = 0
cant_bronce = 0

i = 0
while i < vueltas:
    if tiempo_vuelta[i] <= registro_oro:
        cant_oro += 1
    elif tiempo_vuelta[i] <= registro_plata:
        cant_plata += 1
    elif tiempo_vuelta[i] <= registro_bronce:
        cant_bronce += 1
    i += 1

print('Mejor tiempo: ', tiempo_menor)
print('Peor tiempo: ', tiempo_mayor)
print()
print('Records campeonato anterior:')
print('Oro:', registro_oro)
print('Plata:', registro_plata)
print('Bronce:', registro_bronce)
print()
print('Medallas obtenidas:')
print('Oro:', cant_oro)
print('Plata:', cant_plata)
print('Bronce:', cant_bronce)
print()

print('Tiempos ordenados:')
i = 0
while i < vueltas:
    print(tiempo_vuelta[i])
    i += 1
