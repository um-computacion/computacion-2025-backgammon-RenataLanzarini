"""
Módulo principal del Backgammon.
Contiene la clase BackgammonJuego que gestiona el estado del juego.
"""

class BackgammonJuego:
    """Clase principal que controla el flujo general del Backgammon."""

    def __init__(self):
        """Inicializa el juego en estado 'inicial' con turno 1."""
        self.__estado__ = "inicial"
        self.__turno__ = 1

    def iniciar(self):
        """Cambia el estado del juego a 'jugando'."""
        self.__estado__ = "jugando"

    def descripcion(self) -> str:
        """
        Devuelve un texto descriptivo del estado actual.
        """
        return f"Estado: {self.__estado__}, turno: {self.__turno__}"

