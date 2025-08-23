import random

class Dados:
    def __init__(self):
        self.__ultima_tirada__= []

    def tirar(self) -> list[int]:
        a = random.randint(1, 6)
        b = random.randint(1, 6) 
        self.__ultima_tirada__ = [a, b] if a != b else [a, a, a, a]
        return self.__ultima_tirada__
