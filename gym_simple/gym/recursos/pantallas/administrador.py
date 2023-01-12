from ..funciones import calculos, usuarios, utilidades, validadores

def perfil(perfil, lista_usuarios):
    salir = False
    while salir == False:
        utilidades.limpia_pantalla()
        print("Bienvenido(a) " + lista_usuarios[perfil]["Nombre"])
        print("====================")
        print("Pantalla de aministración del sistema")
        print("-" * 80)
        print()
        
        print("1) Ver Rutinas")
        print("2) Registrar Rutinas")
        print("3) Ver Lugares")
        print("4) Registrar Lugares")
        print("   -----------------")
        print("5) Desconectarse")
        print()

        seleccion = validadores.ingreso_rango_numeros("Ingrese su opción y presione ENTER para continuar: ", [1,5])
        match seleccion:
            case 1:
                print("Sin implementar (Ver Rutinas)")
                utilidades.pausa()
            case 2:
                print("Sin implementar (Registrar Rutinas)")
                utilidades.pausa()
            case 3:
                print("Sin implementar (Ver Lugares)")
                utilidades.pausa()
            case 4:
                print("Sin implementar (Registrar Lugares)")
                utilidades.pausa()
            case _:
                salir = True

    utilidades.pausa()
    return lista_usuarios
