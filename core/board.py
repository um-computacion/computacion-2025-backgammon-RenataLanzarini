"""
Módulo Tablero del Backgammon.
Representa el tablero con 24 puntos y operaciones auxiliares.
"""

class Tablero:
    """Clase que representa el tablero de Backgammon."""

    def __init__(self):
        """Inicializa un tablero con 24 puntos vacíos."""
        self._puntos = [[] for _ in range(24)]

    def contar_fichas(self) -> int:
        """Devuelve la cantidad total de fichas en el tablero."""
        return sum(len(p) for p in self._puntos)

    def esta_vacio(self, indice: int) -> bool:
        """Devuelve True si un punto del tablero está vacío."""
        return len(self._puntos[indice]) == 0

    def puntos_ocupados(self) -> list[int]:
        """Devuelve los índices de puntos que tienen al menos una ficha."""
        return [i for i, p in enumerate(self._puntos) if p]

    def reset(self):
        """Vacía todas las fichas del tablero."""
        self._puntos = [[] for _ in range(24)]

    def __len__(self):
        """Permite usar len(tablero) para obtener la cantidad total de fichas."""
        return self.contar_fichas()

    def fichas_en(self, indice: int) -> int:
        """Devuelve cuántas fichas hay en un punto específico."""
        return len(self._puntos[indice])

    def ficha_en(self, indice: int) -> str | None:
        """Devuelve la ficha superior de un punto o None si está vacío."""
        if self.esta_vacio(indice):
            return None
        return self._puntos[indice][-1]

    def punto_valido(self, indice: int) -> bool:
        """Verifica si el índice corresponde a un punto válido del tablero."""
        return 0 <= indice < len(self._puntos)

    def tablero_vacio(self) -> bool:
        """Devuelve True si no hay fichas en ningún punto del tablero."""
        return self.contar_fichas() == 0

    def mover_ficha(self, origen: int, destino: int):
        """Mueve una ficha desde un punto de origen a uno de destino."""
        if self.esta_vacio(origen):
            raise ValueError("No hay fichas en el punto de origen")
        ficha = self._puntos[origen].pop()
        self._puntos[destino].append(ficha)

    def limpiar_punto(self, indice: int):
        """Elimina todas las fichas de un punto específico."""
        self._puntos[indice] = []

    def total_puntos(self) -> int:
        """Devuelve la cantidad total de puntos del tablero (24)."""
        return len(self._puntos)
