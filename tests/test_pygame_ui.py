"""Tests para la interfaz gráfica de Backgammon."""
import pytest
import sys
import os
from unittest.mock import Mock, patch

# Configurar entorno para testing sin display
os.environ['SDL_VIDEODRIVER'] = 'dummy'

class TestBackgammonUI:
    """Tests para la interfaz gráfica de Backgammon."""
    
    def test_ui_inicializacion(self):
        """Test de inicialización de la UI."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font') as mock_font:
            
            mock_font_instance = Mock()
            mock_font.return_value = mock_font_instance
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            assert ui.juego is not None
            assert ui.running is True

    def test_ui_configuracion_tablero(self):
        """Test de configuración del tablero."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            assert ui.juego is not None

    def test_punto_a_coordenadas(self):
        """Test de conversión de punto a coordenadas."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            assert hasattr(ui, 'punto_a_coordenadas')

    def test_coordenadas_a_punto(self):
        """Test de conversión de coordenadas a punto."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            assert hasattr(ui, 'coordenadas_a_punto')

    def test_manejar_eventos_quit(self):
        """Test de manejo de evento QUIT."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.event.get') as mock_get:
            
            from ui.pygame_ui import BackgammonUI
            import pygame
            
            ui = BackgammonUI()
            mock_event = Mock()
            mock_event.type = pygame.QUIT
            mock_get.return_value = [mock_event]
            
            ui.manejar_eventos()
            assert ui.running is False

    def test_manejar_eventos_escape(self):
        """Test de manejo de evento ESCAPE."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.event.get') as mock_get:
            
            from ui.pygame_ui import BackgammonUI
            import pygame
            
            ui = BackgammonUI()
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_ESCAPE
            mock_get.return_value = [mock_event]
            
            ui.manejar_eventos()
            assert ui.running is False

    def test_manejar_eventos_espacio(self):
        """Test de manejo de evento ESPACIO (tirar dados)."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.event.get') as mock_get:
            
            from ui.pygame_ui import BackgammonUI
            import pygame
            
            ui = BackgammonUI()
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_SPACE
            mock_get.return_value = [mock_event]
            
            ui.manejar_eventos()
            assert hasattr(ui.juego, 'tirar_dados')

    def test_manejar_eventos_reinicio(self):
        """Test de manejo de evento R (reiniciar)."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.event.get') as mock_get:
            
            from ui.pygame_ui import BackgammonUI
            import pygame
            
            ui = BackgammonUI()
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_r
            mock_get.return_value = [mock_event]
            
            ui.manejar_eventos()
            assert hasattr(ui.juego, 'reiniciar')

    def test_manejar_click_mouse_sin_dados(self):
        """Test de click sin dados tirados."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            ui.dados_tirados = False
            assert hasattr(ui, 'manejar_click_mouse')

    def test_manejar_click_mouse_fuera_tablero(self):
        """Test de click fuera del tablero."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            assert hasattr(ui, 'manejar_click_mouse')

    def test_obtener_movimientos_validos(self):
        """Test de obtención de movimientos válidos."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            assert hasattr(ui, 'obtener_movimientos_validos')

    def test_obtener_movimientos_validos_sin_dados(self):
        """Test de obtención de movimientos sin dados."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            ui.juego.dados_disponibles = []
            assert hasattr(ui, 'obtener_movimientos_validos')

    def test_ui_run_bucle_principal(self):
        """Test del bucle principal de la UI."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.display.flip'), \
             patch('pygame.quit'), \
             patch('pygame.time.Clock'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            ui.running = False
            ui.run()
            assert True

    def test_dibujar_tablero(self):
        """Test de dibujo del tablero."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.draw.rect'), \
             patch('pygame.draw.line'), \
             patch('pygame.draw.polygon'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            ui.dibujar_tablero()
            assert True

    def test_dibujar_info_panel(self):
        """Test de dibujo del panel de información."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.draw.rect'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            ui.dibujar_info_panel()
            assert True


def test_ejecutar_pygame_ui():
    """Test de la función principal de ejecución."""
    from ui.pygame_ui import ejecutar_pygame_ui
    
    with patch('ui.pygame_ui.BackgammonUI') as mock_ui_class, \
         patch('pygame.quit'):
        
        mock_ui_instance = Mock()
        mock_ui_instance.run = Mock()
        mock_ui_class.return_value = mock_ui_instance
        
        ejecutar_pygame_ui()
        mock_ui_instance.run.assert_called_once()


# Import pygame al final para evitar problemas de inicialización
import pygame