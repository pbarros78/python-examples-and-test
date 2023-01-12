from geopy.geocoders import Nominatim  # esta es la api que ofrece openstreetmap
from geopy import distance
import pandas as pd
from json import load
from urllib.request import urlopen
from tabulate import tabulate

from ..pantallas import usuario
from .utilidades import pausa, limpia_pantalla, obtener_ruta
from .validadores import ingreso_rango_numeros

FILENAME = obtener_ruta("lugares.csv")

def ubicacion_gps(perfil):
    texto = usuario.obtener_perfil(perfil)
    limpia_pantalla()
    print(texto)
    try:
        print("Buscando...")
        data = load(urlopen("http://ipinfo.io/json"))
        lat = data['loc'].split(',')[0]
        lon = data['loc'].split(',')[1]
        print("Ubicación registrada con éxito\n")
        return float(lat), float(lon)
    except:
        print("Error de conexión, asegúrese que se encuentra conectado a internet")
        return


def ubicacion_usuario(perfil):
    texto = usuario.obtener_perfil(perfil)
    limpia_pantalla()
    print(texto)
    print("Ingrese coordenadas")
    print()
    lat = input("Ingrese Latitud(ej.:-33.45045219095): ")
    lon = input("Ingrese Longitud(ej.:-70.67952327127): ")
    try:
        lat = float(lat)
        lon = float(lon)

    except:
        print("Coordenadas no válidas")
        return
    else:
        if (-90 < lat < 90) and (-180 < lon < 180) and localizador.reverse((lat, lon)) != None:
            print("Ubicación registrada con éxito\n")
            return lat, lon
        print("Coordenadas fuera de rangoo o ubicacion sin identificar")
        return


def ubicacion_manual(perfil):
    texto = usuario.obtener_perfil(perfil)
    limpia_pantalla()
    print(texto)
    print("La ubicación sin usar coordenadas puede contener: \n")
    print("- Dirección(ej.:Matucana, Estación Central, Región Metropolitana, Chile)")
    print("- Codigo postal Por Comuna(ej.:9160000)")
    print("- Alguna referencia específica(ej.:Usach)")
    print()
    u = input("Ingrese ubicación: ")
    try:
        ubicacion = localizador.geocode(u)
        lat = ubicacion.latitude
        lon = ubicacion.longitude
        print("Ubicación registrada con éxito\n")
        return lat, lon
    except:
        print("Lugar no encontrado o sin conexión")
        return


def eleccion_ubicacion(perfil, localizacion=None):
    salir = False
    while salir == False:
        texto = usuario.obtener_perfil(perfil)
        limpia_pantalla()
        print(texto)
        print()
        texto2 = "Ingrese su ubicación mediante una de las siguientes opciones:\n"
        print(texto2)
        print("1) Ubicación por geolocalizacion de IP")
        print("2) Ingresar coordenadas directamente")
        print("3) Ingresar una ubicación sin usar coordenadas")
        print("   -------------------------------------------")
        print("4) Volver atrás")
        print()
        if localizacion != None:
            print("Ubicación aproximada actual: ")
            print(localizador.reverse(localizacion))
            print()
        seleccion = ingreso_rango_numeros(
            "Ingrese su opción y presione ENTER para continuar: ", [1, 4])
        match seleccion:
            case 1:
                localizacion = ubicacion_gps(perfil)
            case 2:
                localizacion = ubicacion_usuario(perfil)
            case 3:
                localizacion = ubicacion_manual(perfil)
            case _:
                salir = True
        pausa()
    return localizacion


def ver_lugares(perfil, localizacion):
    if localizacion == None:
        print("Primero ingrese una ubicacion")
        pausa()
        return
    texto = usuario.obtener_perfil(perfil)
    limpia_pantalla()
    print(texto)
    df_lugares = lugares(localizacion)
    if df_lugares.empty:
        print("\nNo se encontraron lugares cercanos\n")
        pausa()
        return
    df_lugares = df_lugares.drop(["lat", "lon"], axis=1)
    df_lugares["distancia"] = df_lugares["distancia"].apply(round)
    df_lugares["distancia"] = df_lugares["distancia"].apply(str) + "m"
    print()
    print("Estos son los lugares más proximos a la ubicación ingresada, ordenados por distancia en forma ascendente")
    df_lugares = tabulate(df_lugares, showindex=False,
                          tablefmt="grid", headers="keys", maxcolwidths=[20, 40, 10, 10], disable_numparse=True)
    print(df_lugares)
    pausa()
    return


def distancia(lat, lon, c2):
    c1 = (lat, lon)
    return distance.distance(c1, c2).meters


def lugares(localizacion):
    df_lugares = pd.read_csv(FILENAME, sep=";")
    df_lugares["distancia"] = df_lugares.apply(
        lambda x: distancia(x["lat"], x["lon"], localizacion), axis=1)
    df_lugares = df_lugares.loc[df_lugares["distancia"]
                                < 1500].sort_values("distancia")
    return df_lugares

localizador = Nominatim(user_agent="Salud y Bienestar")
