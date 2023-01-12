from datetime import datetime

def ingreso_caracteres(texto = '', opciones = []):
    valor = None
    valido = False
    if len(opciones) > 0:
        lista_opciones = []
        for item in opciones:
            lista_opciones.append(item.upper())
    while (valido == False):
        valor = input(texto).upper()
        if (len(lista_opciones) > 0 and lista_opciones.count(valor) > 0) or (len(lista_opciones) == 0):
            valido = True
        else:
            print("El valor que ingresó no es válido")
    return valor

def ingreso_numeros(texto = ''):
    valor = None
    valido = False
    while (valido == False):
        valor = input(texto)
        if valor.isdigit():
            valor = int(valor)
            valido = True
        else:
            print("El valor que ingresó no es válido")
    return valor

def ingreso_rango_numeros(texto = '', rango = []):
    valor = None
    valido = False
    while (valido == False):
        valor = input(texto).upper()
        if valor.isdigit():
            if len(rango) > 0 and (int(valor) >= rango[0] and int(valor) <= rango[1]):
                    valor = int(valor)
                    valido = True
            elif len(rango) == 0:
                valor = int(valor)
                valido = True
        if valido == False:
            print("El valor que ingresó no es válido")
    return valor

def ingreso_fecha(texto):
    valor = None
    valido = False
    while (valido == False):
        valor = input(texto)
        try:
            valor = datetime.strptime(valor, "%d/%m/%Y")
            valor = valor.strftime("%d/%m/%Y")
            valido = True
        except:
            print("El valor que ingresó no es válido")
    return valor
    