from core.game import BackgammonJuego

class BackgammonCLI:
    def __init__(self):
        self.juego = BackgammonJuego()

    def iniciar(self):
        """Inicia el juego desde la CLI y entra en un loop mínimo de comandos."""
        print("🎲 Bienvenido a Backgammon (CLI) 🎲")
        self.juego.iniciar()
        print("El juego ha comenzado. ¡Buena suerte!")
        self.mostrar_estado()

        while True:
            cmd = input("> ").strip().lower()
            if cmd in ("salir", "exit", "q"):
                self.salir()
                break
            if cmd == "estado":
                self.mostrar_estado()
                continue
            if cmd == "reiniciar":
                self.reiniciar_juego()
                continue
            if cmd == "tirar":
                vals = self.juego.tirar_dados()
                print(f"Dados: {vals}  Movimientos: {self.juego.movimientos_disponibles()}")
                continue
            if cmd.startswith("mover"):
                parts = cmd.split()
                if len(parts) != 3:
                    print("Uso: mover <origen> <destino>")
                    continue
                try:
                    origen = int(parts[1])
                    destino = int(parts[2])
                except ValueError:
                    print("Origen y destino deben ser enteros.")
                    continue
                ok = self.juego.aplicar_movimiento(origen, destino)
                if ok:
                    print("Movimiento aplicado.")
                    self.mostrar_estado()
                else:
                    print("Movimiento inválido.")
                continue
            print("Comandos: tirar | mover <origen> <destino> | estado | reiniciar | salir")

    def mostrar_estado(self):
        """Muestra el estado actual del juego."""
        print(self.juego.descripcion())

    def reiniciar_juego(self):
        """Reinicia el juego y muestra confirmación."""
        self.juego.reiniciar()                      
        print("🔄 El juego se reinició correctamente")  
        self.mostrar_estado()                       

    def salir(self):
        """Sale del juego mostrando un mensaje de despedida."""
        print("Gracias por jugar Backgammon. ¡Hasta pronto!")

def ejecutar_cli():
    cli = BackgammonCLI()
    cli.iniciar()git