from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
from os.path import exists

def calcula_edad(fecha_nacimiento):
    edad = None

    try:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        return int(edad.years)
    except:
        return edad

def obtener_fecha_actual():
    return datetime.now().strftime("%d/%m/%Y")

def pausa(texto = "continuar"):
    input(f"Presione ENTER para {texto}...")

def existe_archivo(archivo):
    return exists(archivo)
    
def limpia_pantalla():
    if (os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")

def obtener_ruta(archivo):
    return os.path.join(os.getcwd(), "recursos", "datos", archivo)

def dia_letras(dia):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    return dias[int(dia) - 1]