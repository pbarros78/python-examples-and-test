'''
Fuentes:
https://www.axahealthkeeper.com/blog/que-es-y-como-calcular-la-tasa-metabolica-basal/
https://www.um.es/lafem/Nutricion/DiscoLibro/01-Los%20fundamentos/Complementario/01_05-MetabolismoBasal-IMC.htm
https://es.calcuworld.com/salud/metabolismo-basal/
https://es.calcuworld.com/calculadora-nutricional/calculadora-de-calorias-harris-benedict/
https://www.calcuvio.com/metabolismo-basal
https://calculatodo.com/calcular-tasa-metabolica-basal-tmb
https://www.runtastic.com/blog/es/calculo-del-metabolismo-basal/

Para calcular el IMC: https://www.runtastic.com/blog/es/calculo-del-imc/

'''

# Funciones de cálculo de TMB (revisar cuál es mejor)
# ===================================================

# Mifflin-St.-Jeor
# TMB Mujer: (10 x peso en kg) + (6,25 x altura en cm) - (5 x edad) - 161
# TMB Hombre: (10 x peso en kg) + (6,25 x altura en cm) - (5 x edad) + 5
def TMB_Mifflin_Jeor(sexo, peso, altura, edad):
    tmb_mujer = [10, 6.25, 5, -161]
    tmb_hombre = [10, 6.25, 5, 5]
    if (sexo.upper() == "M"):
        tmb_seleccionado = tmb_mujer
    else:
        tmb_seleccionado = tmb_hombre
    resultado = (tmb_seleccionado[0] * peso) + (tmb_seleccionado[1] * altura) - (tmb_seleccionado[2] * edad) + tmb_seleccionado[3]
    return resultado

# Harris-Benedict (revisada)
# TMB Mujer: 447.593 + (9.247 x peso en kg) + (3.098 x altura en cm) - (4.330 x edad)
# TMB Hombre: 88.362 + (13.397 x peso en kg) + (4.799 x altura en cm) - (5.677 x edad)
def TMB_Harris_Benedict_R(sexo, peso, altura, edad):
    tmb_mujer = [447.593, 9.247, 3.098, 4.330]
    tmb_hombre = [88.362, 13.397, 4.799, 5.677]
    if (sexo.upper() == "M"):
        tmb_seleccionado = tmb_mujer
    else:
        tmb_seleccionado = tmb_hombre
    resultado = tmb_seleccionado[0] + (tmb_seleccionado[1] * peso) + (tmb_seleccionado[2] * altura) - (tmb_seleccionado[3] * edad)
    return resultado

# Harris-Benedict (revisión 2)
# TMB Mujer: 665 + (9,5 x peso en kg) + (1,8 x altura en cm) - (4,6 x edad)
# TMB Hombre: 66,4 + (13,75 x peso en kg) + (5 x altura en cm) - (6,7 x edad)
def TMB_Harris_Benedict_R2(sexo, peso, altura, edad):
    tmb_mujer = [665, 9.5, 1.8, 4.6]
    tmb_hombre = [66.5, 9.5, 1.8, 4.6]
    if (sexo.upper() == "M"):
        tmb_seleccionado = tmb_mujer
    else:
        tmb_seleccionado = tmb_hombre
    resultado = tmb_seleccionado[0] + (tmb_seleccionado[1] * peso) + (tmb_seleccionado[2] * altura) - (tmb_seleccionado[3] * edad)
    return resultado

def TMB_Actividad(tmb, actividad):
    # Si no haces nada de ejercicio y trabajas sentado: TMB x 1,2
    # Si realizas ejercicio ligero dos dias por semana: TMB x 1,375
    # Si haces ejercicio moderado, unos cuatro dias por semana: TMB x 1,55
    # Si hacer deporte regular seis dias a la semana: TMB x 1,725
    # Si eres deportista de elite o entrenas muy intenso cada dia: TMB x 1,9
    tmb_actividad = [1.2, 1.375, 1.55, 1.725, 1.9]
    return tmb * tmb_actividad[actividad - 1]

# Programa
# ===================================================

# Zona de ingreso de variables
# ===================================================

# Ingreso de Sexo (con validaciones)
bien_ingresado = False
while (bien_ingresado == False):
    sexo = input("Ingrese M si es mujer o H si es Hombre: ")
    if sexo.upper() == "M" or sexo.upper() == "H":
        bien_ingresado = True
    else:
        print("El valor que ingresó no es válido")

# Ingreso de Peso (con validaciones)
bien_ingresado = False
while (bien_ingresado == False):
    peso = input("Ingrese su peso en kg (sin décimas): ")
    if peso.isdigit():
        peso = int(peso)
        bien_ingresado = True
    else:
        print("El valor que ingresó no es válido")

# Ingreso de Altura (con validaciones)
bien_ingresado = False
while (bien_ingresado == False):
    altura = input("Ingrese su altura en cm (sin décimas),1 ejemplo: 163: ")
    if altura.isdigit() and int(altura) >= 30 and int(altura) <= 210:
        altura = int(altura)
        bien_ingresado = True
    else:
        print("El valor que ingresó no es válido")

# Ingreso de Edad (con validaciones)
bien_ingresado = False
while (bien_ingresado == False):
    edad = input("Ingrese su edad (en años): ")
    if edad.isdigit():
        edad = int(edad)
        bien_ingresado = True
    else:
        print("El valor que ingresó no es válido")

# Ingreso de Actividad (con menú y validaciones)
print("Seleccione su nivel de actividad")
print("1) No haces nada de ejercicio y trabajas sentado.")
print("2) Realizas ejercicio ligero dos dias por semana.")
print("3) Haces ejercicio moderado, unos cuatro dias por semana.")
print("4) Hacer deporte regular seis dias a la semana.")
print("5) Eres deportista de elite o entrenas muy intenso cada dia.")

bien_ingresado = False
while (bien_ingresado == False):
    actividad = input("Ingrese el número que indica su nivel: ")
    if actividad.isdigit() and int(actividad) >= 1 and int(actividad) <= 5:
        actividad = int(actividad)
        bien_ingresado = True
    else:
        print("El valor que ingresó no es válido")

# Zona de cálculos
# ===================================================

resultado_1 = round(TMB_Mifflin_Jeor(sexo, peso, altura, edad), 2)
resultado_2 = round(TMB_Harris_Benedict_R(sexo, peso, altura, edad), 2)
resultado_3 = round(TMB_Harris_Benedict_R2(sexo, peso, altura, edad), 2)

print("Estimación de TMB según 3 cálculos")
print("Cálculo según Mifflin-St. Jeor:", resultado_1, "Kcal/día para mantenerte")
print("Cálculo según Harris-Benedict (revisada):", resultado_2, "Kcal/día para mantenerte")
print("Cálculo según Harris-Benedict (revisión 2):", resultado_3, "Kcal/día para mantenerte")

resultado_1 = round(TMB_Actividad(resultado_1, actividad), 2)
resultado_2 = round(TMB_Actividad(resultado_2, actividad), 2)
resultado_3 = round(TMB_Actividad(resultado_3, actividad), 2)

print("Estimación de TMB según actividad")
print("Cálculo según Mifflin-St. Jeor:", resultado_1, "Kcal/día para mantenerte")# <= usar esta
print("Cálculo según Harris-Benedict (revisada):", resultado_2, "Kcal/día para mantenerte")
print("Cálculo según Harris-Benedict (revisión 2):", resultado_3, "Kcal/día para mantenerte")
