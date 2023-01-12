#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Patricio Barros
# Created Date: 01/11/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" EN: Class to manipule the console that emulates the c# Console class with
    extras
    It can use colors, error messages, clear console, etc. """
""" ES: Clase para manejo de la consola que emula la clase Console de C# con
    algunos agregados extras.
    Puede usar colores, mensajes de error, limpiar consola, etc. """
# ---------------------------------------------------------------------------
# Imports
# pip install colorama
# ---------------------------------------------------------------------------
import os
import colorama
from colorama import Fore, Back, Style
# ---------------------------------------------------------------------------

class Consoles:
    """Clase para manejo de la consola. Puede usar colores, mensajes de error, limpiar consola, etc.
    """

    FORE = Fore
    STYLE = Style
    BACK = Back

    TextStyle = STYLE.RESET_ALL
    ForeColor = FORE.RESET
    BackgroundColor = BACK.RESET

    def __init__(self) -> None:
        colorama.init(autoreset=True)

    def Clear(self):
        """Limpia la pantalla y resetea los estilos
        """
        if (os.name == "posix"):
            os.system("clear")
        else:
            os.system("cls")
        self.ResetStyles()

    def ResetStyles(self):
        """Resetea los estilos
        """
        self.TextStyle = self.STYLE.RESET_ALL
        self.ForeColor = self.FORE.RESET
        self.BackgroundColor = self.BACK.RESET
        print(self.STYLE.RESET_ALL + self.FORE.RESET + self.BACK.RESET, end = "")

    def Write(self, text: str = ""):
        """Escribe un texto y deja el cursor a la derecha.

        Args:
            text (str, optional): Texto a escribir en consola.
        """
        print(self.TextStyle + self.ForeColor + self.BackgroundColor + text, end = "")

    def WriteLine(self, text: str = ""):
        """Escribe un texto y salta a la siguiente línea.

        Args:
            text (str, optional): Texto a escribir en consola.
        """
        print(self.TextStyle + self.ForeColor + self.BackgroundColor + text)
        
    def Error(self, text: str = ""):
        """Escribe un texto con un símbolo de error en rojo delante.

        Args:
            text (str, optional): Texto a escribir en consola.
        """
        self.ResetStyles()
        print(Fore.RED + "[X] " + Fore.RESET + text)
        
    def Info(self, text: str = ""):
        """Escribe un texto con un símbolo de información en azúl delante.

        Args:
            text (str, optional): Texto a escribir en consola.
        """
        self.ResetStyles()
        print(Fore.BLUE + "[!] " + Fore.RESET + text)
        
    def Warning(self, text: str = ""):
        """Escribe un texto con un símbolo de exclamación en amarillo delante.

        Args:
            text (str, optional): Texto a escribir en consola.
        """
        self.ResetStyles()
        print(Fore.YELLOW + "[!] " + Fore.RESET + text)

Console = Consoles()
"""Clase para manejo de la consola. Puede usar colores, mensajes de error, limpiar consola, etc.
"""
