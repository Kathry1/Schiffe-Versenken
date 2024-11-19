#clases.py
import numpy as np

class Tablero:
    def __init__(self, jugador_id, dimension):
        self.jugador_id = jugador_id
        self.dimension = dimension
        self.tablero = np.full((dimension, dimension), "~")
        self.impactos = np.full((dimension, dimension), "~")
        self.barcos = []

    def platzieren_schiffe(self, schiffe):
        # Schiffe zufällig platzieren (Platzhalter für die Funktion)
        pass

    def anzeigen(self, verborgen=False):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if verborgen and self.tablero[i, j] == "S":
                    print("~", end=" ")
                else:
                    print(self.tablero[i, j], end=" ")
            print()
