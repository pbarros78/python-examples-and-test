# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN
# SECCIÓN DEL CURSO: C-3
# PROFESOR DE TEORÍA: Alejandro Cisterna Villalobos
# PROFESOR DE LABORATORIO: José Gonzalez
# 
# AUTOR 
# NOMBRE: Arina Bilan
# RUT: 24.326.475-8
# CARRERA: Ingeniería Cicil en Informática

'''
El programa genera 2 archivos para María Carting: María Carting DePelos, uno de los resultados
por país de los participantes que terminaron todas las vueltas y otro con los 10 mejores
competidores
'''

# Importacion de módulos
import os
import pandas as pd
import numpy as np

# Definicion de Constantes
# No hay

# Definicion de Funciones
def leer_archivo_csv(archivo):
    df = pd.read_csv("./" + archivo + ".csv", sep=";")
    return df

def guardar_archivo(archivo, datos):
    datos.to_csv("./" + archivo + ".csv", index=False, sep=";")
    return datos

def exist(target):
    return os.path.exists(target)

def create_dir(target):
    if exist(target) == False:
        os.mkdir(target)

# Bloque principal
# Definicion de variables
paises = []

# Entrada
archivo_participantes = "Participantes"
archivo_tiempos = "Tiempos"
archivo_resultados_pais = "resultados"
archivo_ganadores = "ganadores"

participantes = leer_archivo_csv(archivo_participantes)
tiempos = leer_archivo_csv(archivo_tiempos)

# Procesamiento
vueltas_completas = tiempos[tiempos.vuelta == 5]

registros = tiempos[tiempos.identificador.isin(vueltas_completas['identificador'].tolist())]
tiempos = pd.merge(participantes, registros, on='identificador')
# print(tiempos)
# tiempos = tiempos.groupby(['apodo', 'correo']).agg({'tiempo': 'sum'})
# print(tiempos)

#print(participantes)
paises = participantes["pais"].unique()
for pais in paises:
    # if apodo == '' or (apodo != last_apodo):
    #     pass
    apodo = ''
    last_apodo = ''
    correo = ''
    archivo = ''
    resultado = tiempos[tiempos.pais == pais].drop(['pais', 'identificador', 'vuelta'], axis=1)
    for item in resultado:
        apodo = item['apodo']
        if apodo != last_apodo:
            pass
        
    # print(resultado.groupby(['apodo', 'correo']).agg([{ 'tiempo', lambda x: x.sum() }]))
    
    #resultado.to_csv("./resultados_" + str(pais) + ".csv", index=False, sep=';')
    
