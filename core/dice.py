import random

class Dados:
    """Clase que gestiona los dados del juego."""
    
    def __init__(self):
        """Inicializa los dados sin valores."""
        self.__ultima_tirada__ = []

    def tirar(self) -> list[int]:
        """
        Tira dos dados de 6 caras.
        Si ambos valores son iguales (dobles), devuelve 4 valores iguales.
        """
        a = random.randint(1, 6)
        b = random.randint(1, 6) 
        self.__ultima_tirada__ = [a, b] if a != b else [a, a, a, a]
        return self.__ultima_tirada__

    @property
    def valores(self) -> list[int]:
        """Devuelve los valores de la última tirada."""
        return self.__ultima_tirada__