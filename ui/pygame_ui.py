"""Módulo de interfaz gráfica con Pygame - Con sistema de dados correcto."""
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
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Backgammon - Juego Completo")
        self.clock = pygame.time.Clock()
        
        self.juego = BackgammonJuego()
        self.juego.iniciar()
        self.running = True
        self.mensaje = "Jugador 1: Presiona ESPACIO para tirar dados"
        self.fuente = pygame.font.Font(None, 36)
        self.fuente_pequena = pygame.font.Font(None, 24)
        
        # Estado de selección
        self.ficha_seleccionada = None
        self.movimientos_validos = []
        self.juego_terminado = False
        self.dados_tirados = False
    
    def dibujar_tablero(self):
        """Dibuja el tablero de Backgammon."""
        self.screen.fill((30, 30, 30))
        pygame.draw.rect(self.screen, MARRON_CLARO, (50, 100, 700, 400))
        
        # Barra central
        pygame.draw.rect(self.screen, NEGRO, (395, 100, 10, 400))
        
        # Puntos
        for i in range(12):
            x = 50 + i * 58
            if i >= 6: x += 58
            
            # Superior
            pygame.draw.polygon(self.screen, MARRON_OSCURO, [
                (x, 100), (x + 58, 100), (x + 29, 300)
            ])
            # Inferior
            pygame.draw.polygon(self.screen, MARRON_OSCURO, [
                (x, 500), (x + 58, 500), (x + 29, 300)
            ])
            
            # Números
            texto = self.fuente_pequena.render(str(i + 1), True, BLANCO)
            self.screen.blit(texto, (x + 25, 310))
            self.screen.blit(texto, (x + 25, 530))
    
    def dibujar_fichas(self):
        """Dibuja todas las fichas."""
        for punto_idx, fichas in enumerate(self.juego.tablero._puntos):
            for i, ficha in enumerate(fichas):
                x, y = self.punto_a_coordenadas(punto_idx, i)
                color = ROJO if ficha == "X" else AZUL
                
                pygame.draw.circle(self.screen, color, (x, y), 12)
                pygame.draw.circle(self.screen, NEGRO, (x, y), 12, 1)
                
                # Resaltar ficha seleccionada
                if punto_idx == self.ficha_seleccionada and i == len(fichas) - 1:
                    pygame.draw.circle(self.screen, AMARILLO, (x, y), 16, 2)
    
    def dibujar_movimientos_validos(self):
        """Dibuja destinos válidos."""
        for destino in self.movimientos_validos:
            x, y = self.punto_a_coordenadas(destino, 0)
            pygame.draw.circle(self.screen, VERDE, (x, y), 20, 2)
    
    def punto_a_coordenadas(self, punto, indice):
        """Convierte punto lógico a coordenadas de pantalla."""
        if punto < 12:
            # Lado superior
            punto_visual = 11 - punto
            x = 50 + punto_visual * 58 + 29
            y = 300 - (indice * 18) - 25
            if punto >= 6: x += 58
        else:
            # Lado inferior
            punto_visual = punto - 12
            x = 50 + punto_visual * 58 + 29
            y = 300 + (indice * 18) + 25
            if punto_visual >= 6: x += 58
        return (x, y)
    
    def coordenadas_a_punto(self, x, y):
        """Convierte coordenadas de mouse a punto lógico."""
        if not (50 <= x <= 750 and 100 <= y <= 500):
            return None
        
        es_superior = y < 300
        columna = (x - 50) // 58
        if columna >= 6:
            columna -= 1
            
        if es_superior:
            return 11 - columna
        else:
            return columna + 12
    
    def obtener_movimientos_validos(self, origen):
        """Obtiene movimientos válidos desde un punto."""
        movimientos = []
        
        # Solo buscar movimientos si hay dados disponibles
        if not self.juego.dados_disponibles:
            return movimientos
            
        # Verificar todos los puntos posibles como destino
        for destino in range(24):
            if destino != origen and self.juego.es_movimiento_valido(origen, destino):
                movimientos.append(destino)
        
        return movimientos
    
    def dibujar_dados(self):
        """Dibuja los dados disponibles."""
        if hasattr(self.juego, 'dados_disponibles') and self.juego.dados_disponibles:
            texto = self.fuente.render(f"Dados: {self.juego.dados_disponibles}", True, VERDE)
            self.screen.blit(texto, (600, 50))
            
            # Dibujar dados gráficos
            for i, dado in enumerate(self.juego.dados_disponibles):
                x = 600 + i * 60
                y = 100
                pygame.draw.rect(self.screen, BLANCO, (x, y, 50, 50))
                pygame.draw.rect(self.screen, NEGRO, (x, y, 50, 50), 2)
                texto_dado = self.fuente.render(str(dado), True, NEGRO)
                self.screen.blit(texto_dado, (x + 18, y + 10))
        else:
            # Mostrar que no hay dados
            texto = self.fuente.render("Sin dados", True, GRIS)
            self.screen.blit(texto, (600, 50))
    
    def dibujar_estado(self):
        """Dibuja el estado del juego."""
        # Si el juego terminó, mostrar pantalla de victoria
        if self.juego_terminado:
            # Fondo semi-transparente
            s = pygame.Surface((800, 600), pygame.SRCALPHA)
            s.fill((0, 0, 0, 200))
            self.screen.blit(s, (0, 0))
            
            # Mensaje de victoria
            victoria = self.fuente.render("¡JUEGO TERMINADO!", True, NARANJA)
            ganador = self.fuente.render(f"Ganador: Jugador {self.ganador}", True, AMARILLO)
            reiniciar = self.fuente_pequena.render("Presiona R para jugar otra vez", True, BLANCO)
            
            self.screen.blit(victoria, (400 - victoria.get_width()//2, 250))
            self.screen.blit(ganador, (400 - ganador.get_width()//2, 300))
            self.screen.blit(reiniciar, (400 - reiniciar.get_width()//2, 350))
            return
        
        # Turno normal
        jugador = self.juego.jugador_actual()
        color_turno = ROJO if jugador == 1 else AZUL
        nombre_jugador = f"Jugador {jugador}"
        turno = self.fuente.render(f"Turno: {nombre_jugador}", True, color_turno)
        self.screen.blit(turno, (50, 50))
        
        # Mensaje principal
        mensaje = self.fuente.render(self.mensaje, True, AMARILLO)
        self.screen.blit(mensaje, (50, 520))
        
        # Estado de dados
        if not self.dados_tirados:
            estado_dados = self.fuente_pequena.render("Presiona ESPACIO para tirar dados", True, VERDE)
        else:
            estado_dados = self.fuente_pequena.render(f"Dados disponibles: {len(self.juego.dados_disponibles)}", True, AMARILLO)
        self.screen.blit(estado_dados, (50, 550))
        
        # Ficha seleccionada
        if self.ficha_seleccionada is not None:
            seleccion = self.fuente_pequena.render(
                f"Ficha seleccionada en punto {self.ficha_seleccionada + 1}", 
                True, AMARILLO
            )
            self.screen.blit(seleccion, (50, 580))
        
        # Controles
        controles = [
            "Controles:",
            "ESPACIO - Tirar dados", 
            "Click - Seleccionar/mover ficha",
            "R - Reiniciar",
            "ESC - Salir"
        ]
        for i, texto in enumerate(controles):
            control = self.fuente_pequena.render(texto, True, BLANCO)
            self.screen.blit(control, (500, 200 + i * 25))
    
    def manejar_click_mouse(self, x, y):
        """Maneja la selección y movimiento de fichas."""
        if self.juego_terminado:
            return
            
        # Verificar que se tiraron dados primero
        if not self.dados_tirados:
            self.mensaje = "Primero tira dados con ESPACIO"
            return
            
        punto = self.coordenadas_a_punto(x, y)
        if punto is None:
            return
        
        print(f"Click en punto: {punto}")
        
        # Si ya hay ficha seleccionada, intentar mover
        if self.ficha_seleccionada is not None:
            if punto in self.movimientos_validos:
                try:
                    # Realizar movimiento (esto debería consumir un dado)
                    movimiento_exitoso = self.juego.aplicar_movimiento(self.ficha_seleccionada, punto)
                    
                    if movimiento_exitoso:
                        self.mensaje = f"Jugador {self.juego.jugador_actual()}: Movido {self.ficha_seleccionada + 1} → {punto + 1}"
                        
                        # Verificar victoria
                        if self.juego.hay_ganador():
                            self.ganador = self.juego.jugador_actual()
                            self.juego_terminado = True
                            self.mensaje = f"¡Jugador {self.ganador} gana!"
                            return
                        
                        # Verificar si se acabaron los dados
                        if not self.juego.dados_disponibles:
                            # Cambiar turno
                            jugador_anterior = self.juego.jugador_actual()
                            self.juego.cambiar_turno()
                            self.dados_tirados = False
                            nuevo_jugador = self.juego.jugador_actual()
                            self.mensaje = f"Turno cambiado: Jugador {nuevo_jugador}"
                            self.ficha_seleccionada = None
                            self.movimientos_validos = []
                        else:
                            self.mensaje = f"Movimiento exitoso. Dados restantes: {self.juego.dados_disponibles}"
                            
                    else:
                        self.mensaje = "Movimiento inválido"
                        
                except Exception as e:
                    self.mensaje = f"Error: {str(e)}"
            
            # Resetear selección
            self.ficha_seleccionada = None
            self.movimientos_validos = []
            return
        
        # Seleccionar nueva ficha (solo si hay dados disponibles)
        if not self.juego.dados_disponibles:
            self.mensaje = "No hay dados disponibles para mover"
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
                    self.mensaje = f"Ficha seleccionada. Movimientos válidos: {len(self.movimientos_validos)}"
                else:
                    self.mensaje = "No hay movimientos válidos desde esta ficha con los dados actuales"
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
                    
                    # Tirar dados solo si no hay dados disponibles
                    if not self.juego.tiene_dados_disponibles():
                        dados = self.juego.tirar_dados()
                        self.dados_tirados = True
                        jugador = self.juego.jugador_actual()
                        self.mensaje = f"Jugador {jugador}: Dados {dados}. Selecciona una ficha."
                    else:
                        self.mensaje = f"Usa los dados disponibles primero: {self.juego.dados_disponibles}"
                        
                elif event.key == pygame.K_r:
                    # Reiniciar juego
                    self.juego.reiniciar()
                    self.mensaje = "Juego reiniciado. Jugador 1: Presiona ESPACIO para tirar dados."
                    self.ficha_seleccionada = None
                    self.movimientos_validos = []
                    self.juego_terminado = False
                    self.dados_tirados = False
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Click izquierdo
                    x, y = event.pos
                    self.manejar_click_mouse(x, y)
    
    def run(self):
        """Bucle principal."""
        print("✅ Backgammon UI iniciada correctamente")
        print("🎮 Controles: ESPACIO (tirar dados), Click (seleccionar/mover), R (reiniciar), ESC (salir)")
        
        while self.running:
            self.manejar_eventos()
            self.dibujar_tablero()
            self.dibujar_movimientos_validos()
            self.dibujar_fichas()
            self.dibujar_dados()
            self.dibujar_estado()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        print("🎲 Juego terminado")

def ejecutar_pygame_ui():
    ui = BackgammonUI()
    ui.run()

if __name__ == "__main__":
    ejecutar_pygame_ui()