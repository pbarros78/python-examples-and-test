from menu import *

def Login():
    print("Ingreso de Usuarios\n\nPresione ENTER para continuar...")
    input()

def Register():
    print("Registro de Usuarios\n\nPresione ENTER para continuar...")
    input()

menus = Menu()
menus.Title = "Bienvenido"
menus.AddItem("Ingreso", Login)
menus.AddItem("Registrarse", Register)

menus.Show()
