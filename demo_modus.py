import random
from variables import GRID_SIZE, SHIPS
from clases import Tablero
from funciones import schuss, ist_verloren

def demo_modus():
    print("🎮 Willkommen im Demomodus von 'Hundir la Flota'!")
    print("Hier wird das Spiel automatisch simuliert.\n")
    
    # Spielfelder für Spieler und Computer erstellen
    spieler_tablero = Tablero("Spieler", GRID_SIZE)
    computer_tablero = Tablero("Computer", GRID_SIZE)

    # Schiffe auf beiden Spielfeldern platzieren
    spieler_tablero.platzieren_schiffe(SHIPS)
    computer_tablero.platzieren_schiffe(SHIPS)

    # Spielverlauf automatisch durchführen
    while True:
        # Zeige den aktuellen Stand der Spielfelder
        print("\nDein Spielfeld:")
        spieler_tablero.anzeigen()

        print("\nComputerfeld (verdeckt):")
        computer_tablero.anzeigen(verborgen=True)

        # Spieler schießt
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        print(f"\nSpieler schießt auf ({x}, {y})...")
        if schuss(computer_tablero, x, y):
            print("Treffer!")
        else:
            print("Daneben!")

        # Überprüfung: Hat der Spieler gewonnen?
        if ist_verloren(computer_tablero):
            print("\n🎉 Der Spieler hat im Demomodus gewonnen!")
            break

        # Computer schießt
        print("\nComputer ist dran...")
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        print(f"Computer schießt auf ({x}, {y})...")
        if schuss(spieler_tablero, x, y):
            print("Computer trifft!")
        else:
            print("Computer schießt daneben.")

        # Überprüfung: Hat der Computer gewonnen?
        if ist_verloren(spieler_tablero):
            print("\n💻 Der Computer hat im Demomodus gewonnen!")
            break

    print("\nDanke fürs Zuschauen! 🎮")

