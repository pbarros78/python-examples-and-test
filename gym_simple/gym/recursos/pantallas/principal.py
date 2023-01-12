from ..funciones import usuarios, utilidades, validadores
from . import usuario

nombre_app = ""

def ingreso(lista_usuarios):
    return usuario.ingreso_usuario(lista_usuarios)

def registro(lista_usuarios):
    return usuario.registro_usuario(lista_usuarios)

def principal():
    salir = False
    Lista_Usuarios = usuarios.carga_usuarios()
    print(Lista_Usuarios)
    utilidades.pausa()

    while salir == False:
        utilidades.limpia_pantalla()
        texto = "Bienvenido a " + nombre_app
        print(texto)
        print("="*len(texto))
        print()
        
        print("1) Ingreso")
        print("2) Registrarse")
        print("   -----------")
        print("3) Salir")
        print()

        seleccion = validadores.ingreso_rango_numeros("Ingrese su opción y presione ENTER para continuar: ", [1,3])
        match seleccion:
            case 1:
                Lista_Usuarios = ingreso(Lista_Usuarios)
            case 2:
                Lista_Usuarios = registro(Lista_Usuarios)
            case _:
                salir = True
    
    usuarios.guarda_usuarios(Lista_Usuarios)
    utilidades.pausa("salir")
