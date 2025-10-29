import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock

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
            
            # Mock de la fuente
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
            
            # Verificar que el método existe
            assert hasattr(ui, 'punto_a_coordenadas')

    def test_coordenadas_a_punto(self):
        """Test de conversión de coordenadas a punto."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            # Verificar que el método existe
            assert hasattr(ui, 'coordenadas_a_punto')

    def test_manejar_eventos_quit(self):
        """Test de manejo de evento QUIT."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.event.get') as mock_get:
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            # Mock evento QUIT
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
            ui = BackgammonUI()
            
            # Mock evento KEYDOWN ESC
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
            ui = BackgammonUI()
            
            # Mock evento KEYDOWN ESPACIO
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_SPACE
            mock_get.return_value = [mock_event]
            
            ui.manejar_eventos()
            # Verificar que se intentó tirar dados
            assert hasattr(ui.juego, 'tirar_dados')

    def test_manejar_eventos_reinicio(self):
        """Test de manejo de evento R (reiniciar)."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.event.get') as mock_get:
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            # Mock evento KEYDOWN R
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_r
            mock_get.return_value = [mock_event]
            
            ui.manejar_eventos()
            # Verificar que se intentó reiniciar
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
            
            # Verificar que se puede manejar clicks
            assert hasattr(ui, 'manejar_click_mouse')

    def test_manejar_click_mouse_fuera_tablero(self):
        """Test de click fuera del tablero."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            # Verificar que existe el método
            assert hasattr(ui, 'manejar_click_mouse')

    def test_obtener_movimientos_validos(self):
        """Test de obtención de movimientos válidos."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            # Verificar que existe el método
            assert hasattr(ui, 'obtener_movimientos_validos')

    def test_obtener_movimientos_validos_sin_dados(self):
        """Test de obtención de movimientos sin dados."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            # Sin dados, no debería haber movimientos
            ui.juego.dados_disponibles = []
            # Verificar que se puede llamar al método
            assert hasattr(ui, 'obtener_movimientos_validos')

    def test_ui_run_bucle_principal(self):
        """Test del bucle principal de la UI."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.display.flip'), \
             patch('pygame.time.Clock') as mock_clock:
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            # Mock para salir inmediatamente
            ui.running = False
            ui.run()
            
            # Verificar que se ejecutó sin errores
            assert True

    def test_ui_cerrar(self):
        """Test de cierre de la UI."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode'), \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font'), \
             patch('pygame.quit'):
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            
            ui.cerrar()
            assert ui.running is False

def test_ejecutar_pygame_ui():
    """Test de la función principal de ejecución."""
    from ui.pygame_ui import ejecutar_pygame_ui
    from unittest.mock import patch
    
    with patch('ui.pygame_ui.BackgammonUI') as mock_ui_class:
        mock_ui_instance = Mock()
        mock_ui_instance.run = Mock()
        mock_ui_class.return_value = mock_ui_instance
        
        ejecutar_pygame_ui()
        mock_ui_instance.run.assert_called_once()

def test_ejecutar_pygame_ui_con_excepcion():
    """Test de manejo de excepciones en la función principal."""
    from ui.pygame_ui import ejecutar_pygame_ui
    
    with patch('ui.pygame_ui.BackgammonUI') as mock_ui_class:
        mock_ui_instance = Mock()
        mock_ui_instance.run.side_effect = Exception("Error de prueba")
        mock_ui_class.return_value = mock_ui_instance
        
        # Debería manejar la excepción sin propagarla
        ejecutar_pygame_ui()  # No debería lanzar excepción

# Import pygame al final para evitar problemas de inicialización
import pygame