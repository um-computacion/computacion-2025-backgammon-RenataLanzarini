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
        """Devuelve un texto descriptivo del estado actual."""
        tablero_str = " ".join(self.tablero)       
         print("Tablero inicial listo para jugar") 
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

    def pausar(self):
        """Cambia el estado del juego a 'pausado'."""
        self.estado = "pausado"

    def finalizar(self):
        """Cambia el estado del juego a 'finalizado'."""
        self.estado = "finalizado"

    def en_juego(self) -> bool:
        """Devuelve True si el juego está en curso."""
        return self.estado == "jugando"      
