import pygame
from core.game import BackgammonJuego

class BackgammonUI:
    def __init__(self):
        pygame.init()
        self.juego = BackgammonJuego()
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Backgammon - Interfaz Gráfica")

    def iniciar(self):
        self.pantalla.fill((255, 255, 255))
        pygame.display.flip()
        print("Backgammon (pygame UI) iniciado")

def ejecutar_pygame_ui():
    ui = BackgammonUI()
    ui.iniciar()      