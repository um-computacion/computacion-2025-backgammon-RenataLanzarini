"""Módulo de interfaz gráfica con Pygame."""
import pygame
from core.game import BackgammonJuego

class BackgammonUI:
    """Clase para la interfaz gráfica del juego."""
    
    def __init__(self):
        """Inicializa la interfaz de Pygame."""
        pygame.init()
        self.screen = None
        self.running = False
        self.juego = BackgammonJuego()
    
    def iniciar(self):
        """Inicia la interfaz gráfica."""
        self.running = True
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Backgammon")
    
    def cerrar(self):
        """Cierra la interfaz gráfica."""
        self.running = False
        if self.screen:
            pygame.quit()

def ejecutar_pygame_ui():
    """Función para ejecutar la interfaz gráfica."""
    ui = BackgammonUI()
    ui.iniciar()
    print("Interfaz gráfica iniciada (placeholder)")
    ui.cerrar()
