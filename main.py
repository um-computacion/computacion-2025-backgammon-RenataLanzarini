import sys
from core.game import BackgammonJuego

def main():
    """Punto de entrada principal del juego."""
    juego = BackgammonJuego()
    print("🎲 Bienvenido a Backgammon")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        opcion = sys.argv[1].lower()
        
        if opcion == "cli":
            print("Iniciando Backgammon en modo CLI...")
            try:
                from cli.cli import ejecutar_cli
                ejecutar_cli()
            except ImportError:
                print("Error: No se encontró el módulo cli.cli")
                print("Asegúrate de tener el archivo cli/cli.py")
        
        elif opcion == "ui":
            print("Iniciando Backgammon en modo Pygame UI...")
            try:
                from ui.pygame_ui import ejecutar_pygame_ui
                ejecutar_pygame_ui()
            except ImportError:
                print("Error: No se encontró el módulo ui.pygame_ui")
                print("Asegúrate de tener el archivo ui/pygame_ui.py")
        
        else:
            print("Opción inválida. Usa 'cli' o 'ui'.")
    
    else:
        # Modo por defecto: mostrar información del juego
        print("\nEl juego Backgammon ha iniciado correctamente ✅")
        print("\nEstado inicial del juego:")
        print(juego.descripcion())
        print("\nPara ejecutar el juego usa:")
        print("  python main.py cli   # Para interfaz de línea de comandos")
        print("  python main.py ui    # Para interfaz gráfica con Pygame")

if __name__ == "__main__":

    main()