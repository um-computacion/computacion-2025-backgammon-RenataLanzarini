from core.board import Tablero
from core.dice import Dados
from core.player import Jugador

class BackgammonJuego:
    """Clase principal que controla el flujo general del Backgammon."""

    def __init__(self):
        """Inicializa el juego en estado 'inicial' con tablero, jugadores y dados."""
        self.estado = "inicial"
        self.turno = 1
        self.tablero = Tablero()
        self.jugador_x = Jugador("Jugador 1", "X")
        self.jugador_o = Jugador("Jugador 2", "O")
        self.dados = Dados()

    def iniciar(self):
        """Cambia el estado del juego a 'jugando'."""
        self.estado = "jugando"

    def pausar(self):
        """Cambia el estado del juego a 'pausado'."""
        self.estado = "pausado"

    def finalizar(self):
        """Cambia el estado del juego a 'finalizado'."""
        self.estado = "finalizado"

    def reiniciar(self):
        """Reinicia el juego al estado inicial y turno 1."""
        self.estado = "inicial"
        self.turno = 1
        self.tablero.reset()

    def en_juego(self) -> bool:
        """Devuelve True si el juego está en curso."""
        return self.estado == "jugando"

    def descripcion(self) -> str:
        """Devuelve un texto descriptivo del estado actual, tablero y dados."""
        tablero_str = " | ".join(str(self.tablero.fichas_en(i)) for i in range(24))
        dados_str = ", ".join(map(str, self.dados.valores))
        jugador = self.jugador_x.nombre if self.turno == 1 else self.jugador_o.nombre
        return (
            f"Estado: {self.estado}\n"
            f"Turno actual: {jugador} (Jugador {self.turno})\n"
            f"Dados: [{dados_str}]\n"
            f"Tablero: {tablero_str}"
        )

    def cambiar_turno(self):
        """Alterna entre jugador 1 y 2."""
        self.turno = 2 if self.turno == 1 else 1

    def jugador_actual(self) -> int:
        """Devuelve el número del jugador en turno."""
        return self.turno

    def tirar_dados(self) -> list[int]:
        """Lanza los dados y devuelve los valores obtenidos."""
        return self.dados.tirar()

    def movimientos_disponibles(self) -> list[int]:
        """Devuelve los puntos donde hay fichas que pueden moverse."""
        return self.tablero.puntos_ocupados()

    def colocar_ficha(self, indice: int, ficha: str):
        """Coloca una ficha en el punto indicado si es válido."""
        if self.tablero.punto_valido(indice):
            self.tablero._puntos[indice].append(ficha)

    def es_movimiento_valido(self, origen: int, destino: int) -> bool:
        """
        Verifica que el movimiento sea legal:
        - Ambas posiciones deben ser válidas.
        - El punto de origen no debe estar vacío.
        - La ficha en origen debe pertenecer al jugador actual.
        """
        if not (self.tablero.punto_valido(origen) and self.tablero.punto_valido(destino)):
            return False
        if self.tablero.esta_vacio(origen):
            return False
        ficha_origen = self.tablero.ficha_en(origen)
        ficha_jugador = "X" if self.turno == 1 else "O"
        return ficha_origen == ficha_jugador

    def aplicar_movimiento(self, origen: int, destino: int) -> bool:
        """
        Aplica un movimiento si es válido.
        Devuelve True si se realizó el movimiento.
        """
        if self.es_movimiento_valido(origen, destino):
            self.tablero.mover_ficha(origen, destino)
            print(f"Ficha movida de {origen} a {destino}")
            return True
        print("Movimiento inválido.")
        return False