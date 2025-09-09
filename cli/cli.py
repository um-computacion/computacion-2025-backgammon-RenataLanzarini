from core.game import BackgammonJuego

class BackgammonCLI:
    def __init__(self):
        self.juego = BackgammonJuego()

    def iniciar(self):
        print("Bienvenido a Backgammon (CLI). El juego está listo.")