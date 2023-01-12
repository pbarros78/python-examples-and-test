# Función para calcular la Tasa Metabólica Basal (TMB)
def calculo_tmb(sexo, peso, estatura, edad, actividad = 0):
    # Mifflin-St.-Jeor
    # TMB Mujer: (10 x peso en kg) + (6,25 x altura en cm) - (5 x edad) - 161
    # TMB Hombre: (10 x peso en kg) + (6,25 x altura en cm) - (5 x edad) + 5
    tmb_mujer = [10, 6.25, 5, -161]
    tmb_hombre = [10, 6.25, 5, 5]

    # Si no haces nada de ejercicio y trabajas sentado: TMB x 1,2
    # Si realizas ejercicio ligero dos dias por semana: TMB x 1,375
    # Si haces ejercicio moderado, unos cuatro dias por semana: TMB x 1,55
    # Si hacer deporte regular seis dias a la semana: TMB x 1,725
    # Si eres deportista de elite o entrenas muy intenso cada dia: TMB x 1,9
    tmb_actividad = [1.2, 1.375, 1.55, 1.725, 1.9]

    if sexo.upper() == "N" or sexo.upper() == "" or peso == 0 or estatura == 0:
        return 0

    if (sexo.upper() == "M"):
        tmb_seleccionado = tmb_mujer
    else:
        tmb_seleccionado = tmb_hombre
    resultado_tmb = (tmb_seleccionado[0] * peso) + (tmb_seleccionado[1] * estatura) - (tmb_seleccionado[2] * edad) + tmb_seleccionado[3]
    resultado_tmb = round(resultado_tmb, 2)
    
    if actividad != 0:
        tmb = resultado_tmb * tmb_actividad[actividad - 1]
    else:
        tmb = resultado_tmb

    return tmb

# Función para calcular el Indice de Masa Corporal (IMC) para Adultos
def calculo_imc(peso, estatura):
    # Clasificación del Instituto Nacional del Corazón, Pulmón y Sangre. EE.UU.	IMC (kg/mts.2)
    # Bajo peso         <= 18.4
    # Normal            18.5 - 24.9
    # Sobrepeso         25.0 - 29.9
    # Obesidad clase 1  30.0 - 34.9
    # Obesidad clase 2  35.0 - 39.9
    # Obesidad clase 3  >= 40.0
    if peso == 0 or estatura == 0:
        return 0
    if estatura > 99:
        estatura = estatura / 100
    imc = round(peso / (estatura ** 2), 2)
    
    return imc

# Función para calcular el Indice de Masa Corporal (IMC) para Adultos con clasificacion
def calculo_imc_det(peso, estatura):
    # Clasificación del Instituto Nacional del Corazón, Pulmón y Sangre. EE.UU.	IMC (kg/mts.2)
    # Bajo peso         <= 18.4
    # Normal            18.5 - 24.9
    # Sobrepeso         25.0 - 29.9
    # Obesidad clase 1  30.0 - 34.9
    # Obesidad clase 2  35.0 - 39.9
    # Obesidad clase 3  >= 40.0
    if peso == 0 or estatura == 0:
        return "0%"
    if estatura > 99:
        estatura = estatura / 100
    imc = calculo_imc(peso, estatura)
    
    imc = str(imc) + "% = " + imc_letras(imc)
    
    return imc

def actividad_letras(actividad):
    actividad = int(actividad)
    list_actividad = [
        "No haces nada de ejercicio y trabajas sentado.",
        "Realizas ejercicio ligero dos dias por semana.",
        "Haces ejercicio moderado, unos cuatro dias por semana.",
        "Haces deporte regular seis dias a la semana.",
        "Eres deportista de elite o entrenas muy intenso cada dia."
    ]
    return list_actividad[actividad - 1]

def imc_letras(imc):
    texto = ""
    if imc <= 18.4:
        texto = "Bajo peso."
    elif imc <= 24.9:
        texto = "Normal."
    elif imc <= 29.9:
        texto = "Sobrepeso."
    elif imc <= 34.9:
        texto = "Obesidad clase 1."
    elif imc <= 39.9:
        texto = "Obesidad clase 1."
    else:
        texto = "Obesidad clase 3."
    return texto