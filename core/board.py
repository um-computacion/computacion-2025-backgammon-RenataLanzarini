class Tablero:
    def __init__(self):
        self.__puntos__=[[]for _ in range(24)]
    def contar_fichas(self) -> int:
        return sum(len(p)for p in self.__puntos__)
        