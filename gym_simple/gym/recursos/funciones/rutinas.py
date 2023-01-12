from .utilidades import existe_archivo, obtener_ruta, dia_letras
import pandas as pd

FILENAME =  obtener_ruta("rutinas.csv")

def obtener_rutinas_por_nivel(nivel, lista_rutinas):
    df_dias = pd.DataFrame([
        {"dias": 1, "dia": "Lun"},
        {"dias": 2, "dia": "Mar"},
        {"dias": 3, "dia": "Mie"},
        {"dias": 4, "dia": "Jue"},
        {"dias": 5, "dia": "Vie"},
        {"dias": 6, "dia": "Sab"},
        {"dias": 7, "dia": "Dom"}
    ])
    df_rutinas = pd.DataFrame(lista_rutinas)
    rutina = df_rutinas[df_rutinas["nivel"] == nivel]
    rutina = rutina.join(df_dias.set_index("dias"), on="dias")
    rutina = rutina[["grupo_muscular", "descripcion", "repeticiones", "series", "descanso", "dia"]].sort_values(by=["grupo_muscular", "dia"])
    rutinas = rutina.to_dict('records')
    return rutinas

def carga_rutinas():
    lista_rutinas = []
    if not existe_archivo(FILENAME):
        print("ERROR: No hay rutinas registradas.")
    else:
        lista_rutinas = pd.read_csv(FILENAME, sep=";").to_dict('records')

    return lista_rutinas

def guarda_rutinas(lista_rutinas):
    pd.DataFrame(lista_rutinas).to_csv(FILENAME, index=False, header=True, sep=";")
    return lista_rutinas

