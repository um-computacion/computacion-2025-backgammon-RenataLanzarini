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
        """
        Devuelve True si un punto del tablero está vacío.
        """
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
      