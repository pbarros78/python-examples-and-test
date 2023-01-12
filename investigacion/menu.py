#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Patricio Barros
# Created Date: 01/11/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" EN: Class to create menu kind screen with numbers selection """
""" ES: Clase para crear pantallas tipo menú con seleccion por número """
# ---------------------------------------------------------------------------
# Imports
# console module it's make by me
# Require colorama import (install: pip install colorama)
# ---------------------------------------------------------------------------
from console import Console
from typing import Callable
# ---------------------------------------------------------------------------

class Menu:
    """Clase para crear pantallas tipo menú con seleccion por número

    Returns:
        Menu: Instancia de la clase Menu
    """

    class MenuItem:
        """Elemento para menú
        """
        Description: str = ""
        """Texto del elemento
        """
        Callback: Callable = None
        """Función a llamar cuando se seleccione el elemento
        """
        
        def __init__(self, description: str = "-", callback: Callable = None) -> None:
            """Elemento de menú

            Args:
                description (str): Descripcion del elemento
                callback (function): Función a llamar cuando se seleccione el elemento
            """
            self.Description = description
            self.Callback = callback

    Title: str = ""
    """Título del Menú (Opcional). Defecto ""
    """
    __List: list[MenuItem] = []
    __TitleColor = Console.FORE.YELLOW
    
    def __getMaxLength(self) -> int:
        length = 0
        for item in self.__List:
            if len(item.Description) > length:
                length = len(item.Description)
        return length
                
    def __LasItem(self):
        return len(self.__List)
    
    def __Exit(self):
        return True
    
    def __init__(self) -> None:
        pass
    
    def __Draw(self):
        if len(self.Title) > 0:
            Console.TextStyle = Console.STYLE.BRIGHT
            Console.ForeColor = self.__TitleColor
            Console.WriteLine(self.Title)
            Console.WriteLine("═"*len(self.Title))
            Console.ResetStyles()
            Console.WriteLine()
        
        Console.TextStyle = Console.STYLE.BRIGHT
        for item in self.__List:
            if item.Description != '-':
                Console.WriteLine(item.Description)
            else:
                texto = "─" * self.__getMaxLength()
                Console.TextStyle = Console.STYLE.DIM
                Console.WriteLine(texto)
                Console.TextStyle = Console.STYLE.BRIGHT

        Console.WriteLine()
        Console.TextStyle = Console.STYLE.DIM
        Console.Write("Escriba una opción y presione")
        Console.TextStyle = Console.STYLE.BRIGHT
        Console.Write(" ENTER ")
        Console.TextStyle = Console.STYLE.DIM
        Console.Write("para continuar: ")
        Console.ResetStyles()
        
    def __SelectMenu(self):
        menu = input()
        if menu.isdigit():
            intMenu = int(menu) - 1
            if intMenu < self.__LasItem():
                if self.__List[intMenu].Description != "-" and self.__List[intMenu].Callback != None:
                    result = self.__List[intMenu].Callback()
                    return bool(result)
                else:
                    return False
            else:
                return False
    
    def AddItem(self, description: str= "-", callback: Callable = None):
        """Agrega un elemento al menú

        Args:
            description (str, optional): Texto del menú. Para crear un separador debe escribir un guión (-). Defecto "-".
            callback (callable, optional): Función a ejecutar al seleccionar el menú. Defecto None
        """
        if description != "-":
            self.__List.append(self.MenuItem(f"{self.__LasItem() + 1}) {description}", callback))
        else:
            self.__List.append(self.MenuItem())
    
    def Show(self):
        """Muestra el menú con sus opciones
        """
        try:
            if self.__LasItem() <= 0:
                raise Exception("¡No existen menus!, intenta agregar al menos un menú.")
            self.AddItem()
            self.AddItem("Salir", self.__Exit)
            exit = False

            while exit == False:
                Console.Clear()
                
                self.__Draw()
                exit = self.__SelectMenu()
        except Exception as error:
            Console.Error(str(error))
