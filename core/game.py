from core.board import Tablero
from core.dice import Dados
from core.player import Jugador

class BackgammonJuego:
    """Clase principal que controla el flujo general del Backgammon."""

    def __init__(self):
        """Inicializa el juego en estado 'inicial' con tablero y jugadores."""
        self.estado = "inicial"
        self.turno = 1
        self.tablero = Tablero()
        self.jugador_x = Jugador("Jugador 1", "X")
        self.jugador_o = Jugador("Jugador 2", "O")
        self.dados = Dados()

    def iniciar(self):
        """Cambia el estado del juego a 'jugando'."""
        self.estado = "jugando"

    def descripcion(self) -> str:
        """Devuelve un texto descriptivo del estado actual y tablero."""
        tablero_str = " | ".join(str(self.tablero.fichas_en(i)) for i in range(24))
        return f"Estado: {self.estado}, turno: {self.turno}\nTablero: {tablero_str}"

    def cambiar_turno(self):
        """Alterna entre turno 1 y 2."""
        self.turno = 2 if self.turno == 1 else 1

    def jugador_actual(self) -> int:
        """Devuelve el número del jugador en turno."""
        return self.turno

    def reiniciar(self):
        """Reinicia el juego al estado inicial y turno 1."""
        self.estado = "inicial"
        self.turno = 1
        self.tablero.reset()

    def pausar(self):
        """Cambia el estado del juego a 'pausado'."""
        self.estado = "pausado"

    def finalizar(self):
        """Cambia el estado del juego a 'finalizado'."""
        self.estado = "finalizado"

    def en_juego(self) -> bool:
        """Devuelve True si el juego está en curso."""
        return self.estado == "jugando"
