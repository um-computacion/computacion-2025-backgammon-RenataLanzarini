from core.board import Tablero
from core.dice import Dados
from core.player import Jugador

class BackgammonJuego:
    """Clase principal que controla el flujo general del Backgammon."""

    def __init__(self):
        """Inicializa el juego en estado 'inicial' con tablero, jugadores y dados."""
        self.__estado__ = "inicial"
        self.__turno__ = 1
        self.__tablero__ = Tablero()
        self.__jugador_x__ = Jugador("Jugador 1", "X")
        self.__jugador_o__ = Jugador("Jugador 2", "O")
        self.__dados__ = Dados()
        self.__dados_disponibles__ = []

    @property
    def estado(self):
        return self.__estado__
    
    @estado.setter
    def estado(self, valor):
        self.__estado__ = valor
    
    @property
    def turno(self):
        return self.__turno__
    
    @turno.setter
    def turno(self, valor):
        self.__turno__ = valor
    
    @property
    def tablero(self):
        return self.__tablero__
    
    @property
    def jugador_x(self):
        return self.__jugador_x__
    
    @property
    def jugador_o(self):
        return self.__jugador_o__
    
    @property
    def dados(self):
        return self.__dados__
    
    @property
    def dados_disponibles(self):
        return self.__dados_disponibles__
    
    @dados_disponibles.setter
    def dados_disponibles(self, valor):
        self.__dados_disponibles__ = valor

    def iniciar(self):
        """Cambia el estado del juego a 'jugando'."""
        self.__estado__ = "jugando"

    def pausar(self):
        """Cambia el estado del juego a 'pausado'."""
        self.__estado__ = "pausado"

    def finalizar(self):
        """Cambia el estado del juego a 'finalizado'."""
        self.__estado__ = "finalizado"

    def reiniciar(self):
        """Reinicia el juego al estado inicial y turno 1."""
        self.__estado__ = "inicial"
        self.__turno__ = 1
        self.__tablero__.configurar_inicial()
        self.__dados_disponibles__ = []

    def en_juego(self) -> bool:
        """Devuelve True si el juego está en curso."""
        return self.__estado__ == "jugando"

    def descripcion(self) -> str:
        """Devuelve un texto descriptivo del estado actual, tablero y dados."""
        tablero_str = " | ".join(str(self.__tablero__.fichas_en(i)) for i in range(24))
        dados_str = ", ".join(map(str, self.__dados__.valores))
        dados_disp_str = ", ".join(map(str, self.__dados_disponibles__))
        jugador = self.__jugador_x__.nombre if self.__turno__ == 1 else self.__jugador_o__.nombre
        return (
            f"Estado: {self.__estado__}\n"
            f"Turno actual: {jugador} (Jugador {self.__turno__})\n"
            f"Dados: [{dados_str}]\n"
            f"Dados disponibles: [{dados_disp_str}]\n"
            f"Tablero: {tablero_str}"
        )

    def cambiar_turno(self):
        """Alterna entre jugador 1 y 2 y limpia los dados disponibles."""
        self.__turno__ = 2 if self.__turno__ == 1 else 1
        self.__dados_disponibles__ = []

    def jugador_actual(self) -> int:
        """Devuelve el número del jugador en turno."""
        return self.__turno__

    def tirar_dados(self) -> list[int]:
        """Lanza los dados y devuelve los valores obtenidos."""
        valores = self.__dados__.tirar()
        self.__dados_disponibles__ = valores.copy()
        return valores

    def movimientos_disponibles(self) -> list[int]:
        """Devuelve los puntos donde hay fichas que pueden moverse."""
        return self.__tablero__.puntos_ocupados()

    def colocar_ficha(self, indice: int, ficha: str):
        """Coloca una ficha en el punto indicado si es válido."""
        if self.__tablero__.punto_valido(indice):
            self.__tablero__._puntos[indice].append(ficha)

    def puede_reingresar_desde_barra(self, destino: int) -> tuple[bool, int]:
        """
        Verifica si se puede reingresar desde la barra al punto destino.
        Retorna (puede_reingresar, dado_necesario)
        """
        ficha_jugador = "X" if self.__turno__ == 1 else "O"
        
        # Verificar que el jugador tenga fichas en la barra
        if not self.__tablero__.tiene_fichas_en_barra(ficha_jugador):
            return (False, 0)
        
        # Validar destino
        if not self.__tablero__.punto_valido(destino):
            return (False, 0)
        
        # Calcular dado necesario según el jugador
        if self.__turno__ == 1:  # Jugador X
            # X reingresa en puntos 0-5 (home board)
            if destino > 5:
                return (False, 0)
            dado_necesario = destino + 1  # punto 0 = dado 1, punto 5 = dado 6
        else:  # Jugador O
            # O reingresa en puntos 18-23 (home board)
            if destino < 18:
                return (False, 0)
            dado_necesario = 24 - destino  # punto 23 = dado 1, punto 18 = dado 6
        
        # Verificar que el dado esté disponible
        if dado_necesario not in self.__dados_disponibles__:
            return (False, 0)
        
        # Validar que el destino no esté bloqueado (2+ fichas enemigas)
        if self.__tablero__.fichas_en(destino) >= 2:
            ficha_destino = self.__tablero__.ficha_en(destino)
            if ficha_destino != ficha_jugador:
                return (False, 0)
        
        return (True, dado_necesario)

    def es_movimiento_valido(self, origen: int, destino: int) -> bool:
        """
        Verifica que el movimiento sea legal según las reglas de Backgammon.
        """
        ficha_jugador = "X" if self.__turno__ == 1 else "O"
        
        # CASO 1: Reingreso desde la barra (origen = punto donde está)
        # Si el jugador tiene fichas en la barra, DEBE reingresar primero
        if self.__tablero__.tiene_fichas_en_barra(ficha_jugador):
            # Solo puede mover si está reingresando desde el punto correspondiente
            puede, _ = self.puede_reingresar_desde_barra(destino)
            return puede and origen == -1  # -1 indica que viene de la barra
        
        # CASO 2: Movimiento normal desde el tablero
        # Validar origen
        if not self.__tablero__.punto_valido(origen):
            return False
        if self.__tablero__.esta_vacio(origen):
            return False
        
        ficha_origen = self.__tablero__.ficha_en(origen)
        if ficha_origen != ficha_jugador:
            return False
        
        # Validar destino
        if not self.__tablero__.punto_valido(destino):
            return False
        
        # Calcular distancia según dirección del jugador
        if self.__turno__ == 1:  # Jugador X
            # X mueve hacia adelante (incrementa índice)
            distancia = destino - origen
        else:  # Jugador O
            # O mueve hacia atrás (decrementa índice)
            distancia = origen - destino
        
        # La distancia debe ser positiva y coincidir con un dado disponible
        if distancia <= 0 or distancia not in self.__dados_disponibles__:
            return False
        
        # Validar que el destino no esté bloqueado (2+ fichas enemigas)
        if self.__tablero__.fichas_en(destino) >= 2:
            ficha_destino = self.__tablero__.ficha_en(destino)
            if ficha_destino != ficha_jugador:
                return False
        
        return True

    def aplicar_movimiento(self, origen: int, destino: int) -> bool:
        """
        Aplica un movimiento si es válido.
        Maneja capturas y reingreso desde la barra.
        
        Args:
            origen: Índice del punto origen (0-23), o -1 si es desde la barra
            destino: Índice del punto destino (0-23)
        
        Returns:
            True si el movimiento se aplicó exitosamente, False en caso contrario
        """
        ficha_jugador = "X" if self.__turno__ == 1 else "O"
        
        # CASO 1: Reingreso desde la barra
        if origen == -1 or self.__tablero__.tiene_fichas_en_barra(ficha_jugador):
            puede, dado_necesario = self.puede_reingresar_desde_barra(destino)
            
            if not puede:
                return False
            
            # Verificar si hay que capturar en el destino
            if self.__tablero__.fichas_en(destino) == 1:
                ficha_destino = self.__tablero__.ficha_en(destino)
                if ficha_destino != ficha_jugador:
                    self.__tablero__.capturar_ficha(destino)
            
            # Sacar ficha de la barra y colocarla en el destino
            ficha = self.__tablero__.sacar_de_barra(ficha_jugador)
            self.__tablero__._puntos[destino].append(ficha)
            
            # Consumir el dado usado
            self.__dados_disponibles__.remove(dado_necesario)
            
            return True
        
        # CASO 2: Movimiento normal
        if not self.es_movimiento_valido(origen, destino):
            return False
        
        # Calcular distancia
        if self.__turno__ == 1:
            distancia = destino - origen
        else:
            distancia = origen - destino
        
        # Verificar si hay que capturar en el destino
        if self.__tablero__.fichas_en(destino) == 1:
            ficha_destino = self.__tablero__.ficha_en(destino)
            if ficha_destino != ficha_jugador:
                self.__tablero__.capturar_ficha(destino)
        
        # Mover la ficha
        self.__tablero__.mover_ficha(origen, destino)
        
        # Consumir el dado usado
        self.__dados_disponibles__.remove(distancia)
        
        return True

    def tiene_dados_disponibles(self) -> bool:
        """Devuelve True si hay dados disponibles para usar."""
        return len(self.__dados_disponibles__) > 0

    def verificar_ganador(self) -> str | None:
        """
        Verifica si hay un ganador.
        Un jugador gana cuando saca todas sus fichas del tablero.
        """
        fichas_x = self.__tablero__.contar_fichas_jugador("X")
        fichas_o = self.__tablero__.contar_fichas_jugador("O")
        
        fichas_x += self.__tablero__.fichas_en_barra("X")
        fichas_o += self.__tablero__.fichas_en_barra("O")
        
        if fichas_x == 0:
            return "X"
        if fichas_o == 0:
            return "O"
        
        return None

    def hay_ganador(self) -> bool:
        """Devuelve True si hay un ganador."""
        return self.verificar_ganador() is not None
    
    def obtener_movimientos_validos_desde_barra(self, jugador: str) -> list[int]:
        """
        Obtiene los puntos válidos para reingresar una ficha desde la barra.
        
        Args:
            jugador: "X" o "O"
        
        Returns:
            Lista de puntos donde el jugador puede reingresar
        """
        if jugador != ("X" if self.__turno__ == 1 else "O"):
            return []
        
        if not self.__tablero__.tiene_fichas_en_barra(jugador):
            return []
        
        movimientos = []
        
        for dado in self.__dados_disponibles__:
            if jugador == "X":
                punto_destino = dado - 1  # Dado 1 -> punto 0, dado 6 -> punto 5
                if 0 <= punto_destino <= 5:
                    puede, _ = self.puede_reingresar_desde_barra(punto_destino)
                    if puede:
                        movimientos.append(punto_destino)
            else:  # Jugador O
                punto_destino = 24 - dado  # Dado 1 -> punto 23, dado 6 -> punto 18
                if 18 <= punto_destino <= 23:
                    puede, _ = self.puede_reingresar_desde_barra(punto_destino)
                    if puede:
                        movimientos.append(punto_destino)
        
        return list(set(movimientos))  # Eliminar duplicados
