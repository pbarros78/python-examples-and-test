# ╔═════════╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗
# ║ AppGym  ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╠═════════╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣
# ║         ║   ║   ║   ║   ║   ║   ║   ║   ║   ║
# ╚═════════╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝

# ┌─────────┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
# │ AppGym  │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# ├─────────┼───┼───┼───┼───┼───┼───┼───┼───┼───┤
# │         │   │   │   │   │   │   │   │   │   │
# └─────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┘

from enum import Enum
import os, sys

def clear():
    if (os.name == "posix"):
        os.system("clear")
    else:
        os.system("cls")

class TEXT_ALIGN(Enum):
    LEFT = 1,
    CENTER = 2,
    RIGHT = 3

class RECTANGLE(Enum):
    SIMPLE = 1,
    DOUBLE = 2

def cprint(x, y, text = ''):
    print("\033[" + str(y) + ";" + str(x) + "H" + str(text))

def rectangle(x, y, width, height, style = RECTANGLE.SIMPLE, text = ''):
    rec_simple = ['┌', '─', '┐', '│', '└', '┘']
    rec_double = ['╔', '═', '╗', '║', '╚', '╝']

    x2 = x + (width - 1)
    y2 = y + (height - 1)
    rec = rec_simple

    if style == RECTANGLE.DOUBLE:
        rec = rec_double

    cprint(x, y, rec[0])
    cprint(x2, y, rec[2])
    cprint(x, y2, rec[4])
    cprint(x2, y2, rec[5])
    cprint(x + 1, y, rec[1] * (x2 - 2))
    cprint(x + 1, y2, rec[1] * (x2 - 2))
    for i in range(height - 2):
        cprint(x, y + 1 + i, rec[3])
        cprint(x2, y + 1 + i, rec[3])

def rectangle_text(x, y, width, height, text = '', style = RECTANGLE.SIMPLE, text_align = TEXT_ALIGN.LEFT):
    xt = x + 1
    yt = ((y + height) // 2) + (y//2)
    if text_align == TEXT_ALIGN.CENTER:
        xt = x + width//2 - len(text)//2
    elif text_align == TEXT_ALIGN.RIGHT:
        xt = (x + width - 1) - len(text)

    rectangle(x, y, width, height, style)
    cprint(xt, yt, text)

clear()

texto = 'AppGym'

rectangle_text(1, 1, 80, 5, texto, RECTANGLE.DOUBLE)
rectangle_text(1, 6, 80, 5, texto, RECTANGLE.DOUBLE, TEXT_ALIGN.CENTER)
rectangle_text(1, 11, 80, 5, texto, RECTANGLE.DOUBLE, TEXT_ALIGN.RIGHT)

# rectangle_text(1, 1, 80, 5, texto, RECTANGLE.SIMPLE)
# rectangle_text(1, 6, 80, 5, texto, RECTANGLE.SIMPLE, TEXT_ALIGN.CENTER)
# rectangle_text(1, 11, 80, 5, texto, RECTANGLE.SIMPLE, TEXT_ALIGN.RIGHT)

cprint(1, 15)