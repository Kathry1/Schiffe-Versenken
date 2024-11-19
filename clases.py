import numpy as np
import random

class Tablero:
    def __init__(self, jugador_id, dimension):
        self.jugador_id = jugador_id
        self.dimension = dimension
        self.tablero = np.full((dimension, dimension), "~")  # "~" für Wasser
        self.impactos = np.full((dimension, dimension), "~")  # "X" für Treffer, "O" für Fehlschuss
        self.barcos = []

    def platzieren_schiffe(self, schiffe):
        for länge, anzahl in schiffe:
            for _ in range(anzahl):
                while True:
                    x = random.randint(0, self.dimension - 1)
                    y = random.randint(0, self.dimension - 1)
                    richtung = random.choice(["H", "V"])  # Horizontal oder Vertikal
                    if self.kann_schiff_platzieren(x, y, länge, richtung):
                        self.setze_schiff(x, y, länge, richtung)
                        break

    def kann_schiff_platzieren(self, x, y, länge, richtung):
        if richtung == "H" and y + länge <= self.dimension:
            return all(self.tablero[x, y + i] == "~" for i in range(länge))
        if richtung == "V" and x + länge <= self.dimension:
            return all(self.tablero[x + i, y] == "~" for i in range(länge))
        return False

    def setze_schiff(self, x, y, länge, richtung):
        if richtung == "H":
            for i in range(länge):
                self.tablero[x, y + i] = "S"
        else:
            for i in range(länge):
                self.tablero[x + i, y] = "S"
        self.barcos.append((x, y, länge, richtung))

    def anzeigen(self, verborgen=False):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if verborgen and self.tablero[i, j] == "S":
                    print("~", end=" ")
                else:
                    print(self.tablero[i, j], end=" ")
            print()
