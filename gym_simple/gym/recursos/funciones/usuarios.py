from .utilidades import existe_archivo, obtener_ruta
import pandas as pd

FILENAME = obtener_ruta("perfiles.csv")


def valida_ingreso(usuario, contrasena, lista_usuarios):
    perfil = valida_usuario_existe(usuario, lista_usuarios)
    if perfil == -1 or lista_usuarios[perfil]["Contrasena"].upper() != contrasena.upper():
        return -1
    return perfil


def valida_usuario_existe(usuario, lista_usuarios):
    for linea in lista_usuarios:
        if linea['Usuario'].upper() == usuario.upper():
            return lista_usuarios.index(linea)
    return -1


def carga_usuarios():
    lista_usuarios = []
    if not existe_archivo(FILENAME):
        lista_usuarios = pd.DataFrame(
            [['admin', 'admin123', 'Administrador',
                '', '01/01/2000', 'N', 0, 0, 0, '']],
            columns=[
                'Usuario',
                'Contrasena',
                'Nombre',
                'Apellido',
                'Fecha_Nacimiento',
                'Sexo',
                'Peso',
                'Estatura',
                'Nivel_Actividad',
                'Fecha_Registro'
            ]).to_dict('records')
        guarda_usuarios(lista_usuarios)
    else:
        lista_usuarios = pd.read_csv(FILENAME, sep=";").to_dict('records')

    return lista_usuarios


def guarda_usuarios(lista_usuarios):
    pd.DataFrame(lista_usuarios).to_csv(
        FILENAME, index=False, header=True, sep=";")
    return lista_usuarios
