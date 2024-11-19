#funciones.py
import numpy as np
def schuss(tablero, x, y):
    if tablero.tablero[x, y] == "S":
        print("Treffer! 🚢")
        tablero.tablero[x, y] = "X"
        tablero.impactos[x, y] = "X"
        return True
    elif tablero.tablero[x, y] == "~":
        print("Daneben! 🌊")
        tablero.tablero[x, y] = "O"
        tablero.impactos[x, y] = "O"
        return False
    else:
        print("Hier wurde bereits geschossen.")
        return False

def ist_verloren(tablero):
    return not np.any(tablero.tablero == "S")
