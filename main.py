main.py
import numpy as np
import random
import time
from demo_modus import demo_modus



if __name__ == "__main__":
    print("🎮 Willkommen bei Schiffe Versenken!")
    print("Wähle einen Modus:")
    print("1. Spieler gegen Computer")
    print("2. Demoversion (Simulation)")

    wahl = input("Deine Wahl (1/2): ")

    if wahl == "1":
        main()
    elif wahl == "2":
        demo_modus()
    else:
        print("Ungültige Eingabe. Programm wird beendet.")


##4.main.py
from variables import GRID_SIZE, SHIPS
from clases import Tablero
from funciones import schuss, ist_verloren
from colorama import Fore, Style
print(Fore.RED + "Daneben!" + Style.RESET_ALL)
print(Fore.GREEN + "Treffer!" + Style.RESET_ALL)



def main():
    print("Willkommen zu Schiffe Versenken!")
    
    # Spieler und Computer-Tabellen erstellen
    spieler_tablero = Tablero("Spieler", GRID_SIZE)
    computer_tablero = Tablero("Computer", GRID_SIZE)

    # Schiffe platzieren
    spieler_tablero.platzieren_schiffe(SHIPS)
    computer_tablero.platzieren_schiffe(SHIPS)

    # Spiel starten
    while True:
        print("\nDein Spielfeld:")
        spieler_tablero.anzeigen()
        
        print("\nComputerfeld (verdeckt):")
        computer_tablero.anzeigen(verborgen=True)

        # Spielerzug
        print("\nDein Zug:")
        while True:
            try:
                x = int(input("Zeile eingeben (0-9): "))
                y = int(input("Spalte eingeben (0-9): "))
                if 0<= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                    break
                else:
                    print("Ungültige Eingabe, die Koordinaten sind ausserhalb des Spielfeldes!")
            except ValueError:
                print("Bitte gültige Zahl eingeben!")

        schuss(computer_tablero, x, y)
        
        if ist_verloren(computer_tablero):
            print("Herzlichen Glückwunsch! Du hast gewonnen!")
            break

        # Computerzug
        print("\nZug des Computers...")
        while True:
            x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if schuss(spieler_tablero, x, y):
                break
        
        if ist_verloren(spieler_tablero):
            print("Der Computer hat gewonnen. Versuch es noch einmal!")
            break

if __name__ == "__main__":
    main()
