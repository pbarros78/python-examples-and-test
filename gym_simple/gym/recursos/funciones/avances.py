from .utilidades import existe_archivo, obtener_ruta
import pandas as pd

FILENAME =  obtener_ruta("avances.csv")

def carga_avances(usuario):
    lista_avances = []
    if not existe_archivo(FILENAME):
        lista_avances = pd.DataFrame(
            [],
            columns=[
                'usuario',
                'peso',
                'actividad',
                'nivel',
                'cumplimiento',
                'fecha_avance'
            ]).to_dict('records')
        guarda_avances(lista_avances)
    else:
        lista_avances = pd.read_csv(FILENAME, sep=";")#.to_dict('records')
        lista_avances = lista_avances[lista_avances["usuario"] == usuario].to_dict('records')

    return lista_avances

def guarda_avances(lista_avances):
    pd.DataFrame(lista_avances).to_csv(FILENAME, index=False, header=True, sep=";")
    return lista_avances

