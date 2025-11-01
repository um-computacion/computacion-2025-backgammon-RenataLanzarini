"""Módulo de jugadores del Backgammon."""

class Jugador:
    """Representa un jugador del juego."""
    
    def __init__(self, nombre: str, color: str):
        """Inicializa un jugador con nombre y color."""
        self.nombre = nombre
        self.color = color
        self._fichas_restantes = 15

    def fichas_restantes(self) -> int:
        """Devuelve la cantidad de fichas restantes del jugador."""
        return self._fichas_restantes

    def perder_ficha(self):
        """Reduce en 1 la cantidad de fichas restantes (si es posible)."""
        if self._fichas_restantes > 0:
            self._fichas_restantes -= 1

    def __str__(self) -> str:
        """Representación en string del jugador."""
        return f"Jugador {self.nombre} ({self.color}) - {self._fichas_restantes} fichas"


