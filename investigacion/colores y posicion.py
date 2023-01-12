import os
import colorama
from colorama import Fore, Back, Style, Cursor
from string import printable

MINY, MAXY = 1, 24
MINX, MAXX = 1, 80

# set of printable ASCII characters, including a space.
CHARS = ' ' + printable.strip()

PASSES = 1000

# def pos(x,y):
#     return "\033[" + str(x) + ";" + str(y) + "H"

# def clear():
#     if (os.name == "posix"):
#         os.system("clear")
#     else:
#         os.system("cls")

def main():
    #clear()
    colorama.init()
    pos = lambda y, x: Cursor.POS(x, y)
    print(colorama.ansi.clear_screen())
    print(Fore.RED + pos(10, 10) + "Holas")
    print('\033[39m')

if __name__ == '__main__':
    main()