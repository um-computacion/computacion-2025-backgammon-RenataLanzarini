import pygame
from core.game import BackgammonJuego
from assets import resource

class BackgammonUI:
    def __init__(self):
        pygame.init()
        self.juego = BackgammonJuego()
        # usar constantes en lugar de valores mágicos
        self.pantalla = pygame.display.set_mode(
            (resource.ANCHO_VENTANA, resource.ALTO_VENTANA)
        )
        pygame.display.set_caption(resource.TITULO_VENTANA)

    def iniciar(self):
        # usar constante de color BLANCO
        self.pantalla.fill(resource.BLANCO)
        pygame.display.flip()
        print("Backgammon (pygame UI) iniciado")

def ejecutar_pygame_ui():
    ui = BackgammonUI()
    ui.iniciar()  