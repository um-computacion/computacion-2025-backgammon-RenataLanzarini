import pygame
from core.game import BackgammonJuego

class BackgammonUI:
    def __init__(self): 
        pygame.init() 
        self.__juego__ = BackgammonJuego()
        self.__pantalla__= pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Backgammon - Interfaz Grafica")


    def iniciar(self):
        self.__pantalla__.fill((255, 255,255))
        pygame.display.flip()
        print("Backgammon (pygame UI) iniciado")
        