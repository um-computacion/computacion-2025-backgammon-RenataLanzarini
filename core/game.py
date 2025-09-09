class BackgammonJuego:
    """Clase principal que controla el flujo general del Backgammon."""

    def __init__(self):
        """Inicializa el juego en estado 'inicial' con turno 1."""
        self.estado = "inicial"
        self.turno = 1

    def iniciar(self):
        """Cambia el estado del juego a 'jugando'."""
        self.estado = "jugando"

    def descripcion(self) -> str:
        """
        Devuelve un texto descriptivo del estado actual.
        """
        return f"Estado: {self.estado}, turno: {self.turno}"


