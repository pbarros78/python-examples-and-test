from ..funciones import calculos, usuarios, utilidades, validadores, coordenadas, rutinas, avances
from . import administrador


def sexo_desc(sexo):
    if sexo.upper() == "M":
        return "Mujer"
    else:
        return "Hombre"


def nivel_desc(nivel):
    nivel = int(nivel)
    list_nivel = [
        "Principiante.",
        "Intermedio.",
        "Avanzado."
    ]
    return list_nivel[nivel - 1]


def ingreso_usuario(lista_usuarios):
    if len(lista_usuarios) == 0:
        print("ERROR: No existen usuarios!. Registre un usuario para poder ingresar.")
        utilidades.pausa()
        return lista_usuarios

    utilidades.limpia_pantalla()
    print("Ingreso del Usuario")
    print("===================")
    print()

    usuario = input("Usuario: ")
    if usuarios.valida_usuario_existe(usuario, lista_usuarios) == -1:
        print("ERROR: Usuario no existe!, intente registrarse.")
        utilidades.pausa()
        return lista_usuarios

    contrasena = input("Contraseña: ")
    perfil = usuarios.valida_ingreso(usuario, contrasena, lista_usuarios)
    if perfil == -1:
        print("ERROR: Usuario o contraseña inválidos!.")
        utilidades.pausa()
        return lista_usuarios

    lista_usuarios = perfil_usuario(perfil, lista_usuarios)
    return lista_usuarios


def registro_usuario(lista_usuarios):
    utilidades.limpia_pantalla()
    print("Registro de Usuarios")
    print("====================")

    usuario = ""
    valida = False
    while valida == False:
        usuario = input("Ingrese un nombre de usuario: ")
        if lista_usuarios != None or len(lista_usuarios) > 0:
            perfil = usuarios.valida_usuario_existe(usuario, lista_usuarios)
            if perfil != -1:
                print("ERROR: Usuario ya existe!, intente otro nombre de usuario.")
            else:
                valida = True
        else:
            valida = True

    contrasena = input("Ingrese una contraseña: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    # agno_nacimiento = validadores.ingreso_fecha("Ingrese su fecha de nacimiento (ej.:28/08/1990): ")

    Usuario = {
        "Usuario": usuario,
        "Contrasena": contrasena,
        "Nombre": nombre,
        "Apellido": apellido,
        "Fecha_Nacimiento": "",
        "Sexo": "N",
        "Peso": 0,
        "Estatura": 0,
        "Nivel_Actividad": 0,
        "Fecha_Registro": ""
    }
    lista_usuarios.append(Usuario)
    usuarios.guarda_usuarios(lista_usuarios)
    print("¡Usuario registrado!.")
    utilidades.pausa()
    lista_usuarios = usuarios.carga_usuarios()

    return lista_usuarios


def obtener_perfil(perfil, detallado=False, con_cabecera=True):
    edad = utilidades.calcula_edad(perfil["Fecha_Nacimiento"])
    estatura = int(perfil["Estatura"])
    peso = int(perfil["Peso"])
    tmb = calculos.calculo_tmb(perfil["Sexo"], peso, estatura, edad)
    imc = calculos.calculo_imc_det(peso, estatura)
    sexo = sexo_desc(perfil["Sexo"])

    texto = ""
    if con_cabecera:
        texto = "Bienvenido(a) " + perfil["Nombre"] + " " + perfil["Apellido"]
        texto += "\n" + "=" * len(texto) + "\n"
    if perfil["Sexo"].upper() == "N":
        texto += "Sin detalles!\n"
        texto += "-" * 80
        return texto
    texto += "Sexo: " + sexo + "\t\t\t"
    texto += "Edad: " + str(edad) + " años\n"
    texto += "Peso: " + str(perfil["Peso"]) + " kg.\t\t\t"
    texto += "Estatura: " + str(estatura / 100) + " mt.\n"
    if detallado:
        texto += "\nIMC: " + imc + "\n"
        texto += "Nivel de actividad: " + \
            calculos.actividad_letras(perfil["Nivel_Actividad"]) + "\n"
        texto += "TMB: " + str(tmb) + " Kcal/día necesarias para mantenerse.\n"
        Nivel_Ejercicios = "Sin registrar."
        if not(perfil["Nivel_Ejercicios"] == "" or perfil["Nivel_Ejercicios"] == "0"):
            Nivel_Ejercicios = nivel_desc(perfil["Nivel_Ejercicios"])
        texto += "Nivel de ejercitamiento: " + Nivel_Ejercicios + "\n"
    if con_cabecera:
        texto += "-" * 80
    return texto


def perfil_usuario(perfil, lista_usuarios):
    if lista_usuarios[perfil]["Usuario"] == "admin":
        lista_usuarios = administrador.perfil(perfil, lista_usuarios)
        return lista_usuarios
    salir = False
    localizacion = None
    while salir == False:
        texto = obtener_perfil(lista_usuarios[perfil])

        utilidades.limpia_pantalla()
        print(texto)
        print()

        print("1) Ver detalles")
        if lista_usuarios[perfil]["Sexo"] == "N":
            print("2) Ingresar detalles")
        else:
            print("2) Modificar detalles")
        if localizacion == None:
            print("3) Ingresar ubicación")
        else:
            print("3) Modificar ubicación")
        print("4) Ver lugares")
        print("5) Ver rutinas")
        print("   ------------------")
        print("6) Desconectarse")
        print()

        seleccion = validadores.ingreso_rango_numeros(
            "Ingrese su opción y presione ENTER para continuar: ", [1, 6])
        match seleccion:
            case 1:
                ver_detalles_usuario(lista_usuarios[perfil])
            case 2:
                if lista_usuarios[perfil]["Sexo"] == "N":
                    lista_usuarios = registrar_detalles_usuario(
                        perfil, lista_usuarios)
                else:
                    lista_usuarios = modificar_detalles_usuario(
                        perfil, lista_usuarios)
            case 3:
                localizacion = coordenadas.eleccion_ubicacion(
                    lista_usuarios[perfil], localizacion)
            case 4:
                coordenadas.ver_lugares(lista_usuarios[perfil], localizacion)
            case 5:
                ver_rutinas(lista_usuarios[perfil])
            case _:
                salir = True

    utilidades.pausa()
    return lista_usuarios


def ver_detalles_usuario(perfil):
    texto = obtener_perfil(perfil, True)

    utilidades.limpia_pantalla()
    print(texto)
    utilidades.pausa()


def seleccion_nivel_actividad():
    print("\nSeleccione su nivel de actividad")
    print("1) " + calculos.actividad_letras(1))
    print("2) " + calculos.actividad_letras(2))
    print("3) " + calculos.actividad_letras(3))
    print("4) " + calculos.actividad_letras(4))
    print("5) " + calculos.actividad_letras(5))
    actividad = validadores.ingreso_rango_numeros(
        "Ingrese el número que indica su nivel (del 1 al 5): ", [1, 5])
    return actividad


def seleccion_nivel_ejercitamiento():
    print("\n¿En qué nivel de ejercitamiento te consideras estar?")
    print("Esto es para escoger tu rutina de ejercicios.")
    print("1) Principiante.")
    print("2) Intermedio.")
    print("3) Avanzado.")
    nivel = validadores.ingreso_rango_numeros(
        "Ingrese el número que indica su nivel (del 1 al 3): ", [1, 3])
    return nivel


def registrar_detalles_usuario(linea, lista_usuarios):
    perfil = lista_usuarios[linea]

    utilidades.limpia_pantalla()
    texto = "Detalles de " + perfil["Nombre"] + " " + perfil["Apellido"]
    print(texto)
    print("=" * len(texto))
    print()

    agno_nacimiento = validadores.ingreso_fecha(
        "Ingrese su fecha de nacimiento (ej.:28/08/1990): ")
    sexo = validadores.ingreso_caracteres(
        "Ingrese su sexo (M = Mujer, H = Hombre): ", ["m", "h"])
    peso = validadores.ingreso_numeros(
        "Ingrese su peso en kg (sin décimas, ej.: 60): ")
    estatura = validadores.ingreso_rango_numeros(
        "Ingrese su estatura en cm (sin décimas, ej.: 163): ", [30, 210])
    actividad = seleccion_nivel_actividad()
    nivel = seleccion_nivel_ejercitamiento()

    perfil["Fecha_Nacimiento"] = agno_nacimiento
    perfil["Sexo"] = sexo
    perfil["Peso"] = peso
    perfil["Estatura"] = estatura
    perfil["Nivel_Actividad"] = actividad
    perfil["Fecha_Registro"] = utilidades.obtener_fecha_actual()
    perfil["Nivel_Ejercicios"] = int(nivel)

    lista_usuarios[linea] = perfil
    usuarios.guarda_usuarios(lista_usuarios)
    print("¡Detalles guardados!")
    utilidades.pausa()
    return lista_usuarios


def modificar_detalles_usuario(linea, lista_usuarios):
    perfil = lista_usuarios[linea]
    peso_original = int(perfil["Peso"])
    actividad_original = int(perfil["Nivel_Actividad"])
    nivel_original = int(perfil["Nivel_Ejercicios"])

    salir = False
    while not salir:
        utilidades.limpia_pantalla()
        texto = "Detalles de " + perfil["Nombre"] + " " + perfil["Apellido"]
        print(texto)
        print("=" * len(texto))
        texto = obtener_perfil(perfil, True, False)
        print(texto, end="")
        print("-" * 80)

        print("\nSeleccione qué quiere modificar de su perfil")
        print("1) Peso")
        print("2) Nivel de actividad")
        print("3) Nivel de ejercitamiento")
        print("--------------------------")
        print("4) Guardar y salir")
        modificacion = validadores.ingreso_rango_numeros(
            "Ingrese el número que indica su nivel (del 1 al 4): ", [1, 4])

        peso = int(perfil["Peso"])
        actividad = perfil["Nivel_Actividad"]
        nivel = perfil["Nivel_Ejercicios"]
        if modificacion == 1:
            peso = validadores.ingreso_numeros(
                "Ingrese su peso en kg (sin décimas, ej.: 60): ")
        elif modificacion == 2:
            actividad = seleccion_nivel_actividad()
        elif modificacion == 3:
            nivel = seleccion_nivel_ejercitamiento()
        else:
            salir = True

        perfil["Peso"] = peso
        perfil["Nivel_Actividad"] = actividad
        perfil["Nivel_Ejercicios"] = int(nivel)

    # lista_rutinas = rutinas.carga_rutinas()
    # lista_rutinas_usuario = rutinas.obtener_rutinas_por_nivel(nivel, lista_rutinas)
    # print(lista_rutinas_usuario)
    # utilidades.pausa()

    lista_avances = avances.carga_avances(perfil["Usuario"])
    avance = {
        'usuario': perfil["Usuario"],
        'peso': peso_original,
        'actividad': actividad_original,
        'nivel': int(nivel_original),
        'cumplimiento': None,
        'fecha_avance': utilidades.obtener_fecha_actual()
    }
    lista_avances.append(avance)
    lista_avances = avances.guarda_avances(lista_avances)
    lista_usuarios = usuarios.guarda_usuarios(lista_usuarios)

    print("¡Detalles guardados!")
    utilidades.pausa()
    return lista_usuarios


def ver_rutinas(perfil):
    nivel = int(perfil["Nivel_Ejercicios"])
    if nivel == 0:
        print("Para ver las rutinas correspondientes a su nivel, primero debe registrar su nivel de ejercitamiento.")
        utilidades.pausa()
        return

    utilidades.limpia_pantalla()
    texto = "Rutinas para " + perfil["Nombre"] + " " + perfil["Apellido"]
    print(texto)
    print("=" * len(texto))
    texto = obtener_perfil(perfil, False, False)
    print(texto, end="")
    print("-" * 80)

    lista_rutinas = rutinas.carga_rutinas()
    lista_rutinas_usuario = rutinas.obtener_rutinas_por_nivel(
        nivel, lista_rutinas)

    headers = list(lista_rutinas_usuario[0].keys())
    print(f'\n{headers[1].capitalize(): <54}{headers[2][:5].capitalize() + ".": <7}{headers[3].capitalize(): <7}{headers[4].capitalize(): <9}{headers[5].capitalize()}')
    print("-" * 80)

    grupo = ""
    for r in lista_rutinas_usuario:
        if grupo != r["grupo_muscular"]:
            grupo = r["grupo_muscular"]
            print(grupo.capitalize().center(80, "_"))
        print(f'{r["descripcion"].capitalize(): <54}{r["repeticiones"]: <7}{r["series"]: <7}{str(r["descanso"]) + " min": <9}{r["dia"].capitalize()}')

    utilidades.pausa()


def registrar_avance(perfil, lista_usuarios):
    pass
