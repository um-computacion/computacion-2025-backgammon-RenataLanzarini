from core.game import BackgammonJuego

class BackgammonCLI:
    def __init__(self):
        self.juego = BackgammonJuego()

    def iniciar(self):
        """Inicia el juego desde la CLI."""
        print("🎲 Bienvenido a Backgammon (CLI) 🎲")
        self.juego.iniciar()                  
        print("El juego ha comenzado. ¡Buena suerte!")
        self.mostrar_estado()                    

    
    def mostrar_estado(self):
        """Muestra el estado actual del juego."""
        print(self.juego.descripcion())

    def reiniciar(self):
        """Reinicia el juego desde la CLI."""
        self.juego.reiniciar()
        print("El juego se reinició.")

    def salir(self):
        """Sale del juego mostrando un mensaje de despedida."""
        print("Gracias por jugar Backgammon. ¡Hasta pronto!")

def ejecutar_cli():
    cli = BackgammonCLI()
    cli.iniciar()