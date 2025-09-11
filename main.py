import sys
from core.game import BackgammonJuego
from cli.cli import ejecutar_cli
from pygame_ui.pygame_ui import ejecutar_pygame_ui

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py [cli|ui]")
        sys.exit(1)

    opcion = sys.argv[1].lower()

    if opcion == "cli":
        print("Iniciando Backgammon en modo CLI...")
        ejecutar_cli()
    elif opcion == "ui":
        print("Iniciando Backgammon en modo Pygame UI...")
        ejecutar_pygame_ui()
    else:
        print("Opción inválida. Usa 'cli' o 'ui'.")

if __name__ == "__main__":
    # Inicializa el juego (opcional por ahora, puede ampliarse después)
    juego = BackgammonJuego()
    print("El juego Backgammon ha iniciado")

    # Llama a main() para seleccionar modo de ejecución
    main()