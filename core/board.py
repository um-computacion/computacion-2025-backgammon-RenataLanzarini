"""
Módulo Tablero del Backgammon.
Representa el tablero con 24 puntos y operaciones auxiliares.
"""

class Tablero:
    """Clase que representa el tablero de Backgammon."""

    def __init__(self):
        """Inicializa un tablero con 24 puntos vacíos y barras para fichas capturadas."""
        self._puntos = [[] for _ in range(24)]
        self.barra_x = []  # Fichas X capturadas
        self.barra_o = []  # Fichas O capturadas

    def configurar_inicial(self):
        """
        Configura el tablero con la posición inicial del Backgammon.
        
        Posiciones estándar:
        - Punto 0: 2 fichas X
        - Punto 5: 5 fichas O
        - Punto 7: 3 fichas O
        - Punto 11: 5 fichas X
        - Punto 12: 5 fichas O
        - Punto 16: 3 fichas X
        - Punto 18: 5 fichas X
        - Punto 23: 2 fichas O
        """
        self.reset()
        
        # Fichas del jugador X (blancas)
        for _ in range(2):
            self._puntos[0].append("X")
        for _ in range(5):
            self._puntos[11].append("X")
        for _ in range(3):
            self._puntos[16].append("X")
        for _ in range(5):
            self._puntos[18].append("X")
        
        # Fichas del jugador O (negras)
        for _ in range(2):
            self._puntos[23].append("O")
        for _ in range(5):
            self._puntos[12].append("O")
        for _ in range(3):
            self._puntos[7].append("O")
        for _ in range(5):
            self._puntos[5].append("O")

    def contar_fichas_jugador(self, color: str) -> int:
        """Cuenta cuántas fichas de un color específico hay en el tablero."""
        total = 0
        for punto in self._puntos:
            total += sum(1 for ficha in punto if ficha == color)
        return total

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
        """Vacía todas las fichas del tablero y las barras."""
        self._puntos = [[] for _ in range(24)]
        self.barra_x = []
        self.barra_o = []

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

    def colocar_ficha(self, indice: int, ficha: str):
        """Coloca una ficha en el punto indicado."""
        if not self.punto_valido(indice):
            raise ValueError(f"Índice {indice} fuera de rango")
        self._puntos[indice].append(ficha)

    def quitar_ficha(self, indice: int) -> str | None:
        """Quita y devuelve la ficha superior de un punto."""
        if self.esta_vacio(indice):
            return None
        return self._puntos[indice].pop()

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

    def __str__(self) -> str:
        """Representación en string del tablero."""
        return " | ".join(str(len(p)) for p in self._puntos)

    def capturar_ficha(self, indice: int):
        """
        Captura la ficha en el punto indicado y la mueve a la barra.
        Solo se puede capturar si hay exactamente 1 ficha en el punto.
        """
        if not self.punto_valido(indice):
            raise ValueError(f"Índice {indice} fuera de rango")
        if len(self._puntos[indice]) != 1:
            raise ValueError("Solo se puede capturar un punto con 1 ficha")
        
        ficha = self._puntos[indice].pop()
        if ficha == "X":
            self.barra_x.append(ficha)
        else:
            self.barra_o.append(ficha)

    def tiene_fichas_en_barra(self, color: str) -> bool:
        """Verifica si un jugador tiene fichas en la barra."""
        if color == "X":
            return len(self.barra_x) > 0
        else:
            return len(self.barra_o) > 0

    def sacar_de_barra(self, color: str) -> str:
        """Saca una ficha de la barra del color especificado."""
        if color == "X":
            if len(self.barra_x) > 0:
                return self.barra_x.pop()
        else:
            if len(self.barra_o) > 0:
                return self.barra_o.pop()
        raise ValueError(f"No hay fichas {color} en la barra")

    def fichas_en_barra(self, color: str) -> int:
        """Devuelve la cantidad de fichas de un color en la barra."""
        if color == "X":
            return len(self.barra_x)
        else:
            return len(self.barra_o)