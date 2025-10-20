class Jugador:
    def __init__(self, nombre: str, color: str):
        self.nombre = nombre
        self.color = color
        self._fichas_restantes = 15  

    def fichas_restantes(self) -> int:
        return self._fichas_restantes

    def perder_ficha(self):
        if self._fichas_restantes > 0:
            self._fichas_restantes -= 1


