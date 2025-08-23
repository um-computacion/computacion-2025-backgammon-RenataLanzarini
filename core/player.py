class Jugador:
    def __init__(self, nombre: str, color: str):
        self.__nombre__= nombre
        self.__color__= color
        self.__fichas_restantes__= 15 #para iniciar con 15

    def fichas_restantes(self) -> int:
        return __fichas_restantes__

    def perder_ficha(self):
        if self.__fichas_restantes__ > 0:
            self.__fichas_restantes__-= 1


