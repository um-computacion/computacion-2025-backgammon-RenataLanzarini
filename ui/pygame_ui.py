"""Módulo de interfaz gráfica con Pygame - Números dentro del tablero."""
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

class BackgammonUI:
    """Interfaz gráfica de Backgammon con Pygame."""
    
    def __init__(self):
        """Inicializa la interfaz gráfica."""
        pygame.init()
        
        # Dimensiones
        self.__ANCHO__ = 900
        self.__ALTO__ = 700
        
        self.screen = pygame.display.set_mode((self.__ANCHO__, self.__ALTO__))
        pygame.display.set_caption("Backgammon - Juego Completo")
        self.clock = pygame.time.Clock()
        
        # Dimensiones del tablero (más alto para incluir números)
        self.__MARGEN__ = 20
        self.__TABLERO_ANCHO__ = self.__ANCHO__ - (2 * self.__MARGEN__)
        self.__TABLERO_ALTO__ = 460  # Aumentado para números
        self.__TABLERO_X__ = self.__MARGEN__
        self.__TABLERO_Y__ = 80
        
        # Dimensiones de puntos (triángulos más pequeños para dejar espacio a números)
        self.__ANCHO_PUNTO__ = self.__TABLERO_ANCHO__ / 13
        self.__ALTO_PUNTO__ = 180  # Triángulos más cortos
        
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
                y_inicio = self.__TABLERO_Y__ + 25  # Dejar espacio para número arriba
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
                y_base = self.__TABLERO_Y__ + self.__TABLERO_ALTO__ - 25  # Dejar espacio para número abajo
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
                if punto_idx == self.ficha_seleccionada and i == len(fichas) - 1:
                    pygame.draw.circle(self.screen, AMARILLO, (int(x), int(y)), self.__RADIO_FICHA__ + 4, 3)
    
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
    
    def obtener_movimientos_validos(self, origen):
        """Obtiene movimientos válidos desde un punto."""
        movimientos = []
        
        if not self.juego.dados_disponibles:
            return movimientos
            
        for destino in range(24):
            if destino != origen and self.juego.es_movimiento_valido(origen, destino):
                movimientos.append(destino)
        
        return movimientos
    
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
        
        turno_texto = self.fuente.render(f"Turno: Jugador {jugador}", True, color_turno)
        self.screen.blit(turno_texto, (col1_x, y_base))
        
        # Estado de dados
        if not self.dados_tirados:
            estado = self.fuente_pequena.render("Presiona ESPACIO", True, VERDE)
        else:
            estado = self.fuente_pequena.render(f"Dados: {len(self.juego.dados_disponibles)}", True, AMARILLO)
        self.screen.blit(estado, (col1_x, y_base + 28))
        
        # Mensaje (dividido si es muy largo)
        if len(self.mensaje) > 32:
            msg_parte1 = self.mensaje[:32]
            msg_parte2 = self.mensaje[32:64]
            msg1 = self.fuente_pequena.render(msg_parte1, True, AMARILLO)
            msg2 = self.fuente_pequena.render(msg_parte2, True, AMARILLO)
            self.screen.blit(msg1, (col1_x, y_base + 50))
            self.screen.blit(msg2, (col1_x, y_base + 68))
        else:
            mensaje_render = self.fuente_pequena.render(self.mensaje, True, AMARILLO)
            self.screen.blit(mensaje_render, (col1_x, y_base + 50))
        
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
            ("R: Reiniciar", BLANCO),
            ("ESC: Salir", BLANCO),
        ]
        
        for i, (texto, color) in enumerate(controles):
            control = self.fuente_pequena.render(texto, True, color)
            self.screen.blit(control, (col3_x, y_base + 25 + i * 20))
    
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
            
        punto = self.coordenadas_a_punto(x, y)
        if punto is None:
            return
        
        # Si ya hay ficha seleccionada, intentar mover
        if self.ficha_seleccionada is not None:
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
            jugador_num = self.juego.jugador_actual()
            jugador_actual = "X" if jugador_num == 1 else "O"
            
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
                        self.mensaje = f"Dados: {dados}. Selecciona ficha."
                    else:
                        self.mensaje = f"Usa dados: {self.juego.dados_disponibles}"
                        
                elif event.key == pygame.K_r:
                    self.juego.reiniciar()
                    self.mensaje = "Presiona ESPACIO para tirar dados"
                    self.ficha_seleccionada = None
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
        print("🎮 Controles: ESPACIO (dados), Click (mover), R (reiniciar), ESC (salir)")
        
        while self.running:
            self.manejar_eventos()
            self.dibujar_tablero()
            self.dibujar_movimientos_validos()
            self.dibujar_fichas()
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