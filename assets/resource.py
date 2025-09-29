"""
Módulo Resource para gestionar recursos del juego Backgammon.
"""

class Recurso:
    """Clase que representa un recurso del juego."""

    def __init__(self, nombre: str, ruta: str):
        self.nombre = nombre
        self.ruta = ruta

    def descripcion(self) -> str:
        """
        Devuelve una cadena con información del recurso.
        """
        return f"Recurso: {self.nombre}, ruta: {self.ruta}"

# 🎨 Colores básicos (RGB)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# 🖥️ Configuración de la ventana pygame
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TITULO_VENTANA = "Backgammon - Interfaz Gráfica"

# 🎲 Configuración del juego
NUM_PUNTOS = 24   # cantidad de puntos en el tablero
FICHAS_POR_JUGADOR = 15

# ⚙️ Configuración extendida de la ventana (nuevo)
FPS = 60
COLOR_FONDO = BLANCO
ICONO_VENTANA = "assets/icon.png"