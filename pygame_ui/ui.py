"""Módulo de interfaz gráfica con Pygame - Reingreso desde barra corregido."""
import pygame
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.game import BackgammonJuego

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
AZUL = (0, 0, 200)
VERDE = (0, 150, 0)
MARRON_CLARO = (160, 120, 80)
MARRON_OSCURO = (100, 70, 40)
AMARILLO = (255, 255, 0)
NARANJA = (255, 165, 0)
GRIS = (128, 128, 128)
MORADO = (128, 0, 128)

class BackgammonUI:
    """Interfaz gráfica de Backgammon con Pygame."""
    
    def __init__(self):
        """Inicializa la interfaz gráfica."""
        pygame.init()
        
        # Dimensiones (más ancho para área de fichas fuera)
        self.__ANCHO__ = 980
        self.__ALTO__ = 700
        
        self.screen = pygame.display.set_mode((self.__ANCHO__, self.__ALTO__))
        pygame.display.set_caption("Backgammon - Juego Completo")
        self.clock = pygame.time.Clock()
        
        # Dimensiones del tablero (más alto para incluir números)
        self.__MARGEN__ = 20
        self.__TABLERO_ANCHO__ = 820
        self.__TABLERO_ALTO__ = 460
        self.__TABLERO_X__ = self.__MARGEN__
        self.__TABLERO_Y__ = 80
        
        # Dimensiones de puntos (triángulos más pequeños para dejar espacio a números)
        self.__ANCHO_PUNTO__ = self.__TABLERO_ANCHO__ / 13
        self.__ALTO_PUNTO__ = 180
        
        # Dimensiones de fichas
        self.__RADIO_FICHA__ = 13
        
        # Barra central
        self.__ANCHO_BARRA__ = int(self.__ANCHO_PUNTO__)
        
        # Área de información (debajo del tablero)
        self.__INFO_Y__ = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ + 5
        self.__INFO_ALTURA__ = self.__ALTO__ - self.__INFO_Y__ - 10
        
        self.juego = BackgammonJuego()
        self.juego.iniciar()
        self.running = True
        self.mensaje = "Presiona ESPACIO para tirar dados"
        self.fuente = pygame.font.Font(None, 24)
        self.fuente_pequena = pygame.font.Font(None, 18)
        self.fuente_titulo = pygame.font.Font(None, 38)
        
        # Estado de selección
        self.ficha_seleccionada = None
        self.barra_seleccionada = False
        self.movimientos_validos = []
        self.juego_terminado = False
        self.dados_tirados = False
    
    def dibujar_tablero(self):
        """Dibuja el tablero de Backgammon."""
        # Fondo
        self.screen.fill((30, 30, 30))
        
        # Tablero principal
        tablero_rect = pygame.Rect(
            self.__TABLERO_X__, 
            self.__TABLERO_Y__, 
            self.__TABLERO_ANCHO__, 
            self.__TABLERO_ALTO__
        )
        pygame.draw.rect(self.screen, MARRON_CLARO, tablero_rect)
        pygame.draw.rect(self.screen, NEGRO, tablero_rect, 3)
        
        # Línea central horizontal (en medio del tablero)
        linea_central_y = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ // 2
        pygame.draw.line(
            self.screen, 
            NEGRO, 
            (self.__TABLERO_X__, linea_central_y),
            (self.__TABLERO_X__ + self.__TABLERO_ANCHO__, linea_central_y),
            2
        )
        
        # Barra central
        barra_x = self.__TABLERO_X__ + (6 * self.__ANCHO_PUNTO__)
        pygame.draw.rect(
            self.screen, 
            NEGRO, 
            (barra_x, self.__TABLERO_Y__, self.__ANCHO_BARRA__, self.__TABLERO_ALTO__)
        )
        
        # Dibujar puntos (triángulos)
        self._dibujar_puntos()
    
    def _dibujar_puntos(self):
        """Dibuja los 24 puntos del tablero con números DENTRO."""
        for i in range(24):
            # Determinar posición
            if i < 12:
                # Puntos superiores (12-1 de izquierda a derecha)
                columna = 11 - i
                if columna >= 6:
                    x_base = self.__TABLERO_X__ + (columna + 1) * self.__ANCHO_PUNTO__
                else:
                    x_base = self.__TABLERO_X__ + columna * self.__ANCHO_PUNTO__
                
                # Triángulo apuntando hacia abajo (desde arriba)
                y_inicio = self.__TABLERO_Y__ + 25
                puntos_triangulo = [
                    (x_base, y_inicio),
                    (x_base + self.__ANCHO_PUNTO__, y_inicio),
                    (x_base + self.__ANCHO_PUNTO__ / 2, y_inicio + self.__ALTO_PUNTO__)
                ]
                # Número ARRIBA del triángulo
                y_numero = self.__TABLERO_Y__ + 8
            else:
                # Puntos inferiores (13-24 de izquierda a derecha)
                columna = i - 12
                if columna >= 6:
                    x_base = self.__TABLERO_X__ + (columna + 1) * self.__ANCHO_PUNTO__
                else:
                    x_base = self.__TABLERO_X__ + columna * self.__ANCHO_PUNTO__
                
                # Triángulo apuntando hacia arriba (desde abajo)
                y_base = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 25
                puntos_triangulo = [
                    (x_base, y_base),
                    (x_base + self.__ANCHO_PUNTO__, y_base),
                    (x_base + self.__ANCHO_PUNTO__ / 2, y_base - self.__ALTO_PUNTO__)
                ]
                # Número DEBAJO del triángulo (pero dentro del tablero)
                y_numero = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 12
            
            # Color alternado
            color = MARRON_OSCURO if i % 2 == 0 else MARRON_CLARO
            pygame.draw.polygon(self.screen, color, puntos_triangulo)
            pygame.draw.polygon(self.screen, NEGRO, puntos_triangulo, 1)
            
            # Número del punto DENTRO del tablero
            texto = self.fuente_pequena.render(str(i + 1), True, BLANCO)
            texto_rect = texto.get_rect(center=(x_base + self.__ANCHO_PUNTO__ / 2, y_numero))
            self.screen.blit(texto, texto_rect)
    
    def dibujar_fichas(self):
        """Dibuja todas las fichas."""
        for punto_idx, fichas in enumerate(self.juego.tablero._puntos):
            for i, ficha in enumerate(fichas):
                x, y = self.punto_a_coordenadas(punto_idx, i)
                color = ROJO if ficha == "X" else AZUL
                
                # Dibujar ficha
                pygame.draw.circle(self.screen, color, (int(x), int(y)), self.__RADIO_FICHA__)
                pygame.draw.circle(self.screen, NEGRO, (int(x), int(y)), self.__RADIO_FICHA__, 2)
                
                # Resaltar ficha seleccionada
                if not self.barra_seleccionada and punto_idx == self.ficha_seleccionada and i == len(fichas) - 1:
                    pygame.draw.circle(self.screen, AMARILLO, (int(x), int(y)), self.__RADIO_FICHA__ + 4, 3)
    
    def dibujar_fichas_barra(self):
        """Dibuja las fichas capturadas en la barra central."""
        # Posición de la barra (centro del tablero)
        barra_x = self.__TABLERO_X__ + (6 * self.__ANCHO_PUNTO__)
        barra_centro = int(barra_x + self.__ANCHO_BARRA__ / 2)
        
        # Dibujar fichas X en barra (parte superior de la barra)
        fichas_x_barra = len(self.juego.tablero.barra_x)
        for i in range(fichas_x_barra):
            y = self.__TABLERO_Y__ + 60 + (i * (self.__RADIO_FICHA__ * 2 + 3))
            pygame.draw.circle(self.screen, ROJO, (barra_centro, int(y)), self.__RADIO_FICHA__)
            pygame.draw.circle(self.screen, NEGRO, (barra_centro, int(y)), self.__RADIO_FICHA__, 2)
            
            # Resaltar si está seleccionada
            if self.barra_seleccionada and self.ficha_seleccionada == "X":
                pygame.draw.circle(self.screen, AMARILLO, (barra_centro, int(y)), self.__RADIO_FICHA__ + 4, 3)
        
        # Dibujar fichas O en barra (parte inferior de la barra)
        fichas_o_barra = len(self.juego.tablero.barra_o)
        for i in range(fichas_o_barra):
            y = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 60 - (i * (self.__RADIO_FICHA__ * 2 + 3))
            pygame.draw.circle(self.screen, AZUL, (barra_centro, int(y)), self.__RADIO_FICHA__)
            pygame.draw.circle(self.screen, NEGRO, (barra_centro, int(y)), self.__RADIO_FICHA__, 2)
            
            # Resaltar si está seleccionada
            if self.barra_seleccionada and self.ficha_seleccionada == "O":
                pygame.draw.circle(self.screen, AMARILLO, (barra_centro, int(y)), self.__RADIO_FICHA__ + 4, 3)
        
        # Contador de fichas en barra
        if fichas_x_barra > 0:
            texto = self.fuente_pequena.render(f"X: {fichas_x_barra}", True, BLANCO)
            self.screen.blit(texto, (barra_x + 5, self.__TABLERO_Y__ + 35))
        
        if fichas_o_barra > 0:
            texto = self.fuente_pequena.render(f"O: {fichas_o_barra}", True, BLANCO)
            self.screen.blit(texto, (barra_x + 5, self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 30))
    
    def dibujar_fichas_fuera(self):
        """Dibuja las fichas que han salido del tablero (bearing off)."""
        # Área a la derecha del tablero
        x_fuera = self.__TABLERO_X__ + self.__TABLERO_ANCHO__ + 50
        
        # Contar fichas fuera (15 - fichas en tablero - fichas en barra)
        fichas_x_tablero = self.juego.tablero.contar_fichas_jugador("X")
        fichas_x_barra = len(self.juego.tablero.barra_x)
        fichas_x_fuera = 15 - fichas_x_tablero - fichas_x_barra
        
        fichas_o_tablero = self.juego.tablero.contar_fichas_jugador("O")
        fichas_o_barra = len(self.juego.tablero.barra_o)
        fichas_o_fuera = 15 - fichas_o_tablero - fichas_o_barra
        
        # Dibujar área de fichas fuera
        area_rect = pygame.Rect(x_fuera - 25, self.__TABLERO_Y__, 70, self.__TABLERO_ALTO__)
        pygame.draw.rect(self.screen, (50, 50, 50), area_rect)
        pygame.draw.rect(self.screen, GRIS, area_rect, 2)
        
        # Dibujar título
        titulo = self.fuente_pequena.render("FUERA", True, BLANCO)
        self.screen.blit(titulo, (x_fuera - 18, self.__TABLERO_Y__ + 10))
        
        # Dibujar fichas X fuera (arriba)
        for i in range(min(fichas_x_fuera, 15)):
            y = self.__TABLERO_Y__ + 50 + (i * (self.__RADIO_FICHA__ * 2 + 2))
            pygame.draw.circle(self.screen, ROJO, (x_fuera, int(y)), self.__RADIO_FICHA__)
            pygame.draw.circle(self.screen, NEGRO, (x_fuera, int(y)), self.__RADIO_FICHA__, 2)
        
        # Contador de fichas X fuera
        if fichas_x_fuera > 0:
            texto = self.fuente_pequena.render(f"X: {fichas_x_fuera}/15", True, ROJO)
            self.screen.blit(texto, (x_fuera - 22, self.__TABLERO_Y__ + 30))
        
        # Dibujar fichas O fuera (abajo)
        for i in range(min(fichas_o_fuera, 15)):
            y = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 50 - (i * (self.__RADIO_FICHA__ * 2 + 2))
            pygame.draw.circle(self.screen, AZUL, (x_fuera, int(y)), self.__RADIO_FICHA__)
            pygame.draw.circle(self.screen, NEGRO, (x_fuera, int(y)), self.__RADIO_FICHA__, 2)
        
        # Contador de fichas O fuera
        if fichas_o_fuera > 0:
            texto = self.fuente_pequena.render(f"O: {fichas_o_fuera}/15", True, AZUL)
            self.screen.blit(texto, (x_fuera - 22, self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 25))
    
    def obtener_movimientos_validos_desde_barra(self, jugador):
        """Obtiene los puntos válidos para reingresar una ficha desde la barra."""
        return self.juego.obtener_movimientos_validos_desde_barra(jugador)
    
    def dibujar_movimientos_validos(self):
        """Dibuja destinos válidos con círculos verdes."""
        for destino in self.movimientos_validos:
            x, y = self.punto_a_coordenadas(destino, 0)
            pygame.draw.circle(self.screen, VERDE, (int(x), int(y)), self.__RADIO_FICHA__ + 6, 3)
    
    def punto_a_coordenadas(self, punto, indice):
        """Convierte punto lógico a coordenadas de pantalla."""
        if punto < 12:
            # Puntos superiores (12-1)
            columna = 11 - punto
            if columna >= 6:
                x = self.__TABLERO_X__ + (columna + 1) * self.__ANCHO_PUNTO__ + self.__ANCHO_PUNTO__ / 2
            else:
                x = self.__TABLERO_X__ + columna * self.__ANCHO_PUNTO__ + self.__ANCHO_PUNTO__ / 2
            
            # Empezar después del número y del borde del triángulo
            y = self.__TABLERO_Y__ + 35 + (indice * (self.__RADIO_FICHA__ * 2 + 2))
        else:
            # Puntos inferiores (13-24)
            columna = punto - 12
            if columna >= 6:
                x = self.__TABLERO_X__ + (columna + 1) * self.__ANCHO_PUNTO__ + self.__ANCHO_PUNTO__ / 2
            else:
                x = self.__TABLERO_X__ + columna * self.__ANCHO_PUNTO__ + self.__ANCHO_PUNTO__ / 2
            
            # Empezar antes del número y del borde del triángulo
            y_base = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 35
            y = y_base - (indice * (self.__RADIO_FICHA__ * 2 + 2))
        
        return (x, y)
    
    def coordenadas_a_punto(self, x, y):
        """Convierte coordenadas de mouse a punto lógico."""
        # Verificar que está dentro del tablero
        if not (self.__TABLERO_X__ <= x <= self.__TABLERO_X__ + self.__TABLERO_ANCHO__):
            return None
        if not (self.__TABLERO_Y__ <= y <= self.__TABLERO_Y__ + self.__TABLERO_ALTO__):
            return None
        
        # Determinar si está en mitad superior o inferior
        mitad_y = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ // 2
        es_superior = y < mitad_y
        
        # Calcular columna
        x_rel = x - self.__TABLERO_X__
        columna = int(x_rel / self.__ANCHO_PUNTO__)
        
        # Ajustar por la barra central
        if columna > 6:
            columna -= 1
        
        # Limitar columna
        if columna < 0 or columna > 11:
            return None
        
        # Calcular punto
        if es_superior:
            punto = 11 - columna
        else:
            punto = columna + 12
        
        return punto
    
    def click_en_barra(self, x, y):
        """Verifica si el click fue en la barra y retorna el jugador correspondiente."""
        barra_x = self.__TABLERO_X__ + (6 * self.__ANCHO_PUNTO__)
        
        # Verificar si está en el área de la barra
        if barra_x <= x <= barra_x + self.__ANCHO_BARRA__:
            # Mitad superior = X, mitad inferior = O
            mitad_y = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ // 2
            if y < mitad_y and len(self.juego.tablero.barra_x) > 0:
                return "X"
            elif y >= mitad_y and len(self.juego.tablero.barra_o) > 0:
                return "O"
        
        return None
    
    def obtener_movimientos_validos(self, origen):
        """Obtiene movimientos válidos desde un punto."""
        movimientos = []
        
        if not self.juego.dados_disponibles:
            return movimientos
            
        for destino in range(24):
            if destino != origen and self.juego.es_movimiento_valido(origen, destino):
                movimientos.append(destino)
        
        return movimientos
    
    def tiene_fichas_en_barra(self, jugador):
        """Verifica si el jugador tiene fichas en la barra."""
        if jugador == "X":
            return len(self.juego.tablero.barra_x) > 0
        else:
            return len(self.juego.tablero.barra_o) > 0
    
    def dibujar_info_panel(self):
        """Dibuja el panel de información debajo del tablero."""
        # Fondo del panel
        panel_rect = pygame.Rect(
            self.__MARGEN__,
            self.__INFO_Y__,
            self.__ANCHO__ - 2 * self.__MARGEN__,
            self.__INFO_ALTURA__
        )
        pygame.draw.rect(self.screen, (40, 40, 40), panel_rect)
        pygame.draw.rect(self.screen, GRIS, panel_rect, 2)
        
        # Dividir en 3 columnas
        col1_x = self.__MARGEN__ + 15
        col2_x = col1_x + 280
        col3_x = col2_x + 280
        y_base = self.__INFO_Y__ + 10
        
        # COLUMNA 1: Turno y Estado
        jugador = self.juego.jugador_actual()
        color_turno = ROJO if jugador == 1 else AZUL
        jugador_texto = "X" if jugador == 1 else "O"
        
        turno_texto = self.fuente.render(f"Turno: Jugador {jugador} ({jugador_texto})", True, color_turno)
        self.screen.blit(turno_texto, (col1_x, y_base))
        
        # Verificar si hay fichas en barra
        if self.tiene_fichas_en_barra(jugador_texto):
            alerta = self.fuente_pequena.render("¡Fichas en BARRA!", True, MORADO)
            self.screen.blit(alerta, (col1_x, y_base + 25))
        
        # Estado de dados
        if not self.dados_tirados:
            estado = self.fuente_pequena.render("Presiona ESPACIO", True, VERDE)
        else:
            estado = self.fuente_pequena.render(f"Dados: {len(self.juego.dados_disponibles)}", True, AMARILLO)
        self.screen.blit(estado, (col1_x, y_base + 48))
        
        # Mensaje (dividido si es muy largo)
        if len(self.mensaje) > 32:
            msg_parte1 = self.mensaje[:32]
            msg_parte2 = self.mensaje[32:64]
            msg1 = self.fuente_pequena.render(msg_parte1, True, AMARILLO)
            msg2 = self.fuente_pequena.render(msg_parte2, True, AMARILLO)
            self.screen.blit(msg1, (col1_x, y_base + 70))
            self.screen.blit(msg2, (col1_x, y_base + 88))
        else:
            mensaje_render = self.fuente_pequena.render(self.mensaje, True, AMARILLO)
            self.screen.blit(mensaje_render, (col1_x, y_base + 70))
        
        # COLUMNA 2: Dados
        dados_titulo = self.fuente.render("Dados:", True, VERDE if self.juego.dados_disponibles else GRIS)
        self.screen.blit(dados_titulo, (col2_x, y_base))
        
        if hasattr(self.juego, 'dados_disponibles') and self.juego.dados_disponibles:
            for i, dado in enumerate(self.juego.dados_disponibles):
                x_dado = col2_x + (i * 45)
                y_dado = y_base + 30
                
                # Dado
                pygame.draw.rect(self.screen, BLANCO, (x_dado, y_dado, 40, 40))
                pygame.draw.rect(self.screen, NEGRO, (x_dado, y_dado, 40, 40), 2)
                
                # Número
                texto_dado = self.fuente_titulo.render(str(dado), True, NEGRO)
                texto_rect = texto_dado.get_rect(center=(x_dado + 20, y_dado + 20))
                self.screen.blit(texto_dado, texto_rect)
        else:
            sin_dados = self.fuente_pequena.render("(ninguno)", True, GRIS)
            self.screen.blit(sin_dados, (col2_x, y_base + 35))
        
        # COLUMNA 3: Controles
        controles_titulo = self.fuente.render("Controles:", True, NARANJA)
        self.screen.blit(controles_titulo, (col3_x, y_base))
        
        controles = [
            ("ESPACIO: Tirar dados", BLANCO),
            ("CLICK: Seleccionar/mover", BLANCO),
            ("Click barra: Reingresar", MORADO),
            ("P: Pasar turno", AMARILLO),
            ("R: Reiniciar", BLANCO),
            ("ESC: Salir", BLANCO),
        ]
        
        for i, (texto, color) in enumerate(controles):
            control = self.fuente_pequena.render(texto, True, color)
            self.screen.blit(control, (col3_x, y_base + 25 + i * 16))
    
    def dibujar_estado(self):
        """Dibuja el estado del juego."""
        # Título principal
        titulo = self.fuente_titulo.render("BACKGAMMON", True, NARANJA)
        titulo_rect = titulo.get_rect(center=(self.__ANCHO__ // 2, 35))
        self.screen.blit(titulo, titulo_rect)
        
        # Si el juego terminó
        if self.juego_terminado:
            s = pygame.Surface((self.__ANCHO__, self.__ALTO__), pygame.SRCALPHA)
            s.fill((0, 0, 0, 200))
            self.screen.blit(s, (0, 0))
            
            victoria = self.fuente_titulo.render("¡JUEGO TERMINADO!", True, NARANJA)
            ganador = self.fuente_titulo.render(f"Ganador: Jugador {self.ganador}", True, AMARILLO)
            reiniciar = self.fuente.render("Presiona R para jugar otra vez", True, BLANCO)
            
            victoria_rect = victoria.get_rect(center=(self.__ANCHO__ // 2, self.__ALTO__ // 2 - 50))
            ganador_rect = ganador.get_rect(center=(self.__ANCHO__ // 2, self.__ALTO__ // 2 + 20))
            reiniciar_rect = reiniciar.get_rect(center=(self.__ANCHO__ // 2, self.__ALTO__ // 2 + 80))
            
            self.screen.blit(victoria, victoria_rect)
            self.screen.blit(ganador, ganador_rect)
            self.screen.blit(reiniciar, reiniciar_rect)
    
    def manejar_click_mouse(self, x, y):
        """Maneja la selección y movimiento de fichas."""
        if self.juego_terminado:
            return
            
        if not self.dados_tirados:
            self.mensaje = "Primero tira dados con ESPACIO"
            return
        
        jugador_num = self.juego.jugador_actual()
        jugador_actual = "X" if jugador_num == 1 else "O"
        
        # PRIORIDAD 1: Verificar si hay fichas en barra
        if self.tiene_fichas_en_barra(jugador_actual):
            # Si hay una ficha de barra seleccionada, intentar moverla
            if self.barra_seleccionada:
                punto = self.coordenadas_a_punto(x, y)
                if punto is not None and punto in self.movimientos_validos:
                    try:
                        # Reingresar desde la barra
                        movimiento_exitoso = self.reingresar_desde_barra(jugador_actual, punto)
                        
                        if movimiento_exitoso:
                            self.mensaje = f"Reingresado desde BARRA → {punto + 1}"
                            
                            if self.juego.hay_ganador():
                                self.ganador = self.juego.jugador_actual()
                                self.juego_terminado = True
                                return
                            
                            if not self.juego.dados_disponibles:
                                self.juego.cambiar_turno()
                                self.dados_tirados = False
                                self.mensaje = f"Turno: Jugador {self.juego.jugador_actual()}"
                        else:
                            self.mensaje = "No se pudo reingresar"
                    except Exception as e:
                        self.mensaje = f"Error: {str(e)}"
                    
                    self.barra_seleccionada = False
                    self.ficha_seleccionada = None
                    self.movimientos_validos = []
                    return
            
            # Intentar seleccionar ficha de la barra
            jugador_barra = self.click_en_barra(x, y)
            if jugador_barra == jugador_actual:
                self.barra_seleccionada = True
                self.ficha_seleccionada = jugador_actual
                self.movimientos_validos = self.obtener_movimientos_validos_desde_barra(jugador_actual)
                
                if self.movimientos_validos:
                    self.mensaje = f"Ficha de BARRA seleccionada. Reingresar en: {[p+1 for p in self.movimientos_validos]}"
                else:
                    self.mensaje = "No puedes reingresar. Puntos bloqueados."
                    self.barra_seleccionada = False
                    self.ficha_seleccionada = None
                return
            else:
                self.mensaje = "¡Primero debes reingresar las fichas de la BARRA!"
                return
        
        # PRIORIDAD 2: Movimientos normales (solo si no hay fichas en barra)
        punto = self.coordenadas_a_punto(x, y)
        if punto is None:
            return
        
        # Si ya hay ficha seleccionada, intentar mover
        if self.ficha_seleccionada is not None and not self.barra_seleccionada:
            if punto in self.movimientos_validos:
                try:
                    movimiento_exitoso = self.juego.aplicar_movimiento(self.ficha_seleccionada, punto)
                    
                    if movimiento_exitoso:
                        self.mensaje = f"Movido {self.ficha_seleccionada + 1} → {punto + 1}"
                        
                        if self.juego.hay_ganador():
                            self.ganador = self.juego.jugador_actual()
                            self.juego_terminado = True
                            return
                        
                        if not self.juego.dados_disponibles:
                            self.juego.cambiar_turno()
                            self.dados_tirados = False
                            self.mensaje = f"Turno: Jugador {self.juego.jugador_actual()}"
                    else:
                        self.mensaje = "Movimiento inválido"
                        
                except Exception as e:
                    self.mensaje = f"Error: {str(e)}"
            
            self.ficha_seleccionada = None
            self.movimientos_validos = []
            return
        
        # Seleccionar nueva ficha
        if not self.juego.dados_disponibles:
            self.mensaje = "No hay dados disponibles"
            return
            
        fichas = self.juego.tablero._puntos[punto]
        if fichas:
            ficha_superior = fichas[-1]
            
            if ficha_superior == jugador_actual:
                self.ficha_seleccionada = punto
                self.movimientos_validos = self.obtener_movimientos_validos(punto)
                
                if self.movimientos_validos:
                    self.mensaje = f"Ficha {punto + 1} seleccionada"
                else:
                    self.mensaje = "Sin movimientos válidos"
                    self.ficha_seleccionada = None
            else:
                self.mensaje = "No es tu ficha"
    
    def reingresar_desde_barra(self, jugador, punto_destino):
        """Reingresa una ficha desde la barra al tablero."""
        # Calcular qué dado se usa para este reingreso
        dado_usado = None
        
        if jugador == "X":
            dado_usado = punto_destino + 1
        else:
            dado_usado = 24 - punto_destino
        
        # Verificar que el dado esté disponible
        if dado_usado not in self.juego.dados_disponibles:
            return False
        
        # Verificar si hay una ficha del oponente para capturar
        fichas_en_destino = self.juego.tablero._puntos[punto_destino]
        oponente = "O" if jugador == "X" else "X"
        
        if fichas_en_destino and fichas_en_destino[0] == oponente and len(fichas_en_destino) == 1:
            if oponente == "X":
                self.juego.tablero.barra_x.append(oponente)
            else:
                self.juego.tablero.barra_o.append(oponente)
            fichas_en_destino.clear()
        
        # Mover la ficha de la barra al punto
        if jugador == "X":
            if self.juego.tablero.barra_x:
                self.juego.tablero.barra_x.pop()
                self.juego.tablero._puntos[punto_destino].append(jugador)
            else:
                return False
        else:
            if self.juego.tablero.barra_o:
                self.juego.tablero.barra_o.pop()
                self.juego.tablero._puntos[punto_destino].append(jugador)
            else:
                return False
        
        # Consumir el dado usado
        self.juego.dados_disponibles.remove(dado_usado)
        
        return True
    
    def manejar_eventos(self):
        """Maneja todos los eventos."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
                elif event.key == pygame.K_SPACE:
                    if self.juego_terminado:
                        return
                    
                    if not self.juego.tiene_dados_disponibles():
                        dados = self.juego.tirar_dados()
                        self.dados_tirados = True
                        
                        jugador_num = self.juego.jugador_actual()
                        jugador_actual = "X" if jugador_num == 1 else "O"
                        
                        if self.tiene_fichas_en_barra(jugador_actual):
                            self.mensaje = f"Dados: {dados}. ¡Debes reingresar fichas de la BARRA!"
                        else:
                            self.mensaje = f"Dados: {dados}. Selecciona ficha."
                    else:
                        self.mensaje = f"Usa dados: {self.juego.dados_disponibles}"
                
                elif event.key == pygame.K_p:
                    """Pasar turno si no hay movimientos posibles."""
                    if self.dados_tirados and not self.juego_terminado:
                        if len(self.juego.dados_disponibles) > 0:
                            # Verificar si realmente no hay movimientos
                            tiene_movimientos = False
                            jugador_num = self.juego.jugador_actual()
                            jugador_actual = "X" if jugador_num == 1 else "O"
                            
                            # Verificar reingreso desde barra
                            if self.tiene_fichas_en_barra(jugador_actual):
                                movs = self.obtener_movimientos_validos_desde_barra(jugador_actual)
                                tiene_movimientos = len(movs) > 0
                            else:
                                # Verificar movimientos normales
                                for punto in range(24):
                                    if not self.juego.tablero.esta_vacio(punto):
                                        if self.juego.tablero.ficha_en(punto) == jugador_actual:
                                            movs = self.obtener_movimientos_validos(punto)
                                            if len(movs) > 0:
                                                tiene_movimientos = True
                                                break
                            
                            if not tiene_movimientos:
                                # No hay movimientos posibles, pasar turno
                                self.juego.cambiar_turno()
                                self.dados_tirados = False
                                self.ficha_seleccionada = None
                                self.barra_seleccionada = False
                                self.movimientos_validos = []
                                self.mensaje = f"Turno pasado. Jugador {self.juego.jugador_actual()}"
                            else:
                                self.mensaje = "¡Aún puedes mover! No puedes pasar turno."
                        else:
                            self.mensaje = "Ya usaste todos los dados"
                    else:
                        self.mensaje = "Primero tira dados con ESPACIO"
                        
                elif event.key == pygame.K_r:
                    self.juego.reiniciar()
                    self.mensaje = "Presiona ESPACIO para tirar dados"
                    self.ficha_seleccionada = None
                    self.barra_seleccionada = False
                    self.movimientos_validos = []
                    self.juego_terminado = False
                    self.dados_tirados = False
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    self.manejar_click_mouse(x, y)
    
    def run(self):
        """Bucle principal."""
        print("✅ Backgammon UI iniciada correctamente")
        print("🎮 Controles:")
        print("   ESPACIO - Tirar dados")
        print("   CLICK   - Seleccionar/mover fichas")
        print("   P       - Pasar turno (si no hay movimientos)")
        print("   R       - Reiniciar juego")
        print("   ESC     - Salir")
        print("\n⚠️  REGLAS IMPORTANTES:")
        print("   - Si tienes fichas en la BARRA, debes reingresarlas primero")
        print("   - Solo puedes pasar turno si NO tienes movimientos válidos")
        
        while self.running:
            self.manejar_eventos()
            self.dibujar_tablero()
            self.dibujar_movimientos_validos()
            self.dibujar_fichas()
            self.dibujar_fichas_barra()     
            self.dibujar_fichas_fuera()       
            self.dibujar_info_panel()
            self.dibujar_estado()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        print("🎲 Juego terminado")

def ejecutar_pygame_ui():
    """Función principal para ejecutar la interfaz gráfica."""
    ui = BackgammonUI()
    ui.run()

if __name__ == "__main__":
    ejecutar_pygame_ui()