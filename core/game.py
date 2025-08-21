
class BackgammonJuego:
    def __init__(self):
        self.__estado__="inicial"
        self.__turno__=1

    def iniciar(self):
        self.__estado__="jugando"
