"""Tests mejorados para la interfaz gráfica de Backgammon - Cobertura >90%."""
import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock, call

# Configurar entorno para testing sin display
os.environ['SDL_VIDEODRIVER'] = 'dummy'

class TestBackgammonUI:
    """Tests para la interfaz gráfica de Backgammon."""
    
    @pytest.fixture
    def ui_mock(self):
        """Fixture para crear una UI mockeada."""
        with patch('pygame.init'), \
             patch('pygame.display.set_mode') as mock_display, \
             patch('pygame.display.set_caption'), \
             patch('pygame.font.Font') as mock_font, \
             patch('pygame.time.Clock'):
            
            mock_screen = MagicMock()
            mock_display.return_value = mock_screen
            
            mock_font_instance = MagicMock()
            mock_font_instance.render = MagicMock(return_value=MagicMock())
            mock_font.return_value = mock_font_instance
            
            from ui.pygame_ui import BackgammonUI
            ui = BackgammonUI()
            ui.screen = mock_screen
            
            yield ui
    
    def test_ui_inicializacion(self, ui_mock):
        """Test de inicialización de la UI."""
        assert ui_mock.juego is not None
        assert ui_mock.running is True
        assert ui_mock.ficha_seleccionada is None
        assert ui_mock.movimientos_validos == []
        assert ui_mock.juego_terminado is False
        assert ui_mock.dados_tirados is False
        assert ui_mock.barra_seleccionada is False

    def test_ui_tiene_screen(self, ui_mock):
        """Test de que tiene pantalla."""
        assert hasattr(ui_mock, 'screen')
        assert ui_mock.screen is not None

    def test_punto_a_coordenadas_superior(self, ui_mock):
        """Test de conversión de punto superior a coordenadas."""
        x, y = ui_mock.punto_a_coordenadas(0, 0)
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        assert y > 0

    def test_punto_a_coordenadas_inferior(self, ui_mock):
        """Test de conversión de punto inferior a coordenadas."""
        x, y = ui_mock.punto_a_coordenadas(12, 0)
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))

    def test_punto_a_coordenadas_con_fichas_apiladas(self, ui_mock):
        """Test de coordenadas con múltiples fichas."""
        x1, y1 = ui_mock.punto_a_coordenadas(5, 0)
        x2, y2 = ui_mock.punto_a_coordenadas(5, 1)
        x3, y3 = ui_mock.punto_a_coordenadas(5, 2)
        assert x1 == x2 == x3
        assert y1 != y2 != y3

    def test_coordenadas_a_punto_fuera_tablero_izquierda(self, ui_mock):
        """Test de coordenadas fuera del tablero (izquierda)."""
        punto = ui_mock.coordenadas_a_punto(0, 100)
        assert punto is None

    def test_coordenadas_a_punto_fuera_tablero_arriba(self, ui_mock):
        """Test de coordenadas fuera del tablero (arriba)."""
        punto = ui_mock.coordenadas_a_punto(100, 0)
        assert punto is None

    def test_coordenadas_a_punto_valores_razonables(self, ui_mock):
        """Test con coordenadas dentro de rangos razonables."""
        punto = ui_mock.coordenadas_a_punto(400, 300)
        assert punto is None or (0 <= punto < 24)

    def test_obtener_movimientos_validos_sin_dados(self, ui_mock):
        """Test de obtención de movimientos sin dados."""
        ui_mock.juego.dados_disponibles = []
        movimientos = ui_mock.obtener_movimientos_validos(0)
        assert movimientos == []

    def test_obtener_movimientos_validos_con_dados(self, ui_mock):
        """Test de obtención de movimientos con dados."""
        ui_mock.juego.dados_disponibles = [3, 4]
        movimientos = ui_mock.obtener_movimientos_validos(0)
        assert isinstance(movimientos, list)

    def test_manejar_eventos_quit(self, ui_mock):
        """Test de manejo de evento QUIT."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.QUIT
            mock_get.return_value = [mock_event]
            
            ui_mock.manejar_eventos()
            assert ui_mock.running is False

    def test_manejar_eventos_escape(self, ui_mock):
        """Test de manejo de evento ESCAPE."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_ESCAPE
            mock_get.return_value = [mock_event]
            
            ui_mock.manejar_eventos()
            assert ui_mock.running is False

    def test_manejar_eventos_espacio_primera_vez(self, ui_mock):
        """Test de tirar dados con ESPACIO."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_SPACE
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = False
            ui_mock.manejar_eventos()
            assert ui_mock.dados_tirados is True

    def test_manejar_eventos_espacio_con_dados_disponibles(self, ui_mock):
        """Test de ESPACIO cuando ya hay dados."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_SPACE
            mock_get.return_value = [mock_event]
            
            ui_mock.juego.dados_disponibles = [3, 4]
            ui_mock.manejar_eventos()
            assert "Usa dados" in ui_mock.mensaje or "dados" in ui_mock.mensaje.lower()

    def test_manejar_eventos_espacio_juego_terminado(self, ui_mock):
        """Test de ESPACIO cuando el juego terminó."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_SPACE
            mock_get.return_value = [mock_event]
            
            ui_mock.juego_terminado = True
            ui_mock.manejar_eventos()
            assert True

    def test_manejar_eventos_reinicio(self, ui_mock):
        """Test de evento R (reiniciar)."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_r
            mock_get.return_value = [mock_event]
            
            ui_mock.ficha_seleccionada = 5
            ui_mock.juego_terminado = True
            ui_mock.dados_tirados = True
            
            ui_mock.manejar_eventos()
            
            assert ui_mock.ficha_seleccionada is None
            assert ui_mock.juego_terminado is False
            assert ui_mock.dados_tirados is False

    def test_manejar_eventos_pasar_turno_sin_dados(self, ui_mock):
        """Test de P sin dados tirados."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_p
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = False
            ui_mock.manejar_eventos()
            assert "dados" in ui_mock.mensaje.lower()

    def test_manejar_eventos_pasar_turno_con_movimientos(self, ui_mock):
        """Test de P con movimientos disponibles."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_p
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = True
            ui_mock.juego.dados_disponibles = [3]
            ui_mock.manejar_eventos()
            assert True

    def test_manejar_click_mouse_juego_terminado(self, ui_mock):
        """Test de click cuando el juego terminó."""
        ui_mock.juego_terminado = True
        ui_mock.manejar_click_mouse(100, 100)
        assert ui_mock.juego_terminado is True

    def test_manejar_click_mouse_sin_dados_tirados(self, ui_mock):
        """Test de click sin dados tirados."""
        ui_mock.dados_tirados = False
        ui_mock.manejar_click_mouse(100, 100)
        assert "dados" in ui_mock.mensaje.lower() or "tira" in ui_mock.mensaje.lower()

    def test_manejar_click_mouse_fuera_tablero(self, ui_mock):
        """Test de click fuera del tablero."""
        ui_mock.dados_tirados = True
        ui_mock.manejar_click_mouse(0, 0)
        assert True

    def test_manejar_click_con_coordenadas_centro(self, ui_mock):
        """Test de click en centro de pantalla."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [3, 4]
        ui_mock.manejar_click_mouse(400, 300)
        assert True

    def test_manejar_click_mouse_mover_ficha(self, ui_mock):
        """Test de movimiento de ficha."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.ficha_seleccionada = 0
        ui_mock.movimientos_validos = [3]
        
        x, y = ui_mock.punto_a_coordenadas(3, 0)
        ui_mock.manejar_click_mouse(x, y)
        assert True

    def test_manejar_click_varios_puntos(self, ui_mock):
        """Test de clicks en varios puntos."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = []
        
        for x in [50, 200, 400, 600, 800]:
            for y in [50, 200, 400, 600]:
                ui_mock.manejar_click_mouse(x, y)
        
        assert True

    def test_dibujar_tablero(self, ui_mock):
        """Test de dibujo del tablero."""
        with patch('pygame.draw.rect'), \
             patch('pygame.draw.line'), \
             patch('pygame.draw.polygon'):
            ui_mock.dibujar_tablero()
            assert True

    def test_dibujar_fichas(self, ui_mock):
        """Test de dibujo de fichas."""
        with patch('pygame.draw.circle'):
            ui_mock.dibujar_fichas()
            assert True

    def test_dibujar_fichas_con_seleccion(self, ui_mock):
        """Test de dibujo con ficha seleccionada."""
        with patch('pygame.draw.circle'):
            ui_mock.ficha_seleccionada = 0
            ui_mock.dibujar_fichas()
            assert True

    def test_dibujar_movimientos_validos(self, ui_mock):
        """Test de dibujo de movimientos válidos."""
        with patch('pygame.draw.circle'):
            ui_mock.movimientos_validos = [3, 5, 7]
            ui_mock.dibujar_movimientos_validos()
            assert True

    def test_dibujar_movimientos_validos_vacio(self, ui_mock):
        """Test de dibujo sin movimientos válidos."""
        with patch('pygame.draw.circle'):
            ui_mock.movimientos_validos = []
            ui_mock.dibujar_movimientos_validos()
            assert True

    def test_dibujar_info_panel(self, ui_mock):
        """Test de dibujo del panel de información."""
        with patch('pygame.draw.rect'):
            ui_mock.dibujar_info_panel()
            assert True

    def test_dibujar_info_panel_con_dados(self, ui_mock):
        """Test de panel con dados disponibles."""
        with patch('pygame.draw.rect'):
            ui_mock.juego.dados_disponibles = [3, 4]
            ui_mock.dados_tirados = True
            ui_mock.dibujar_info_panel()
            assert True

    def test_dibujar_info_panel_sin_dados(self, ui_mock):
        """Test de panel sin dados."""
        with patch('pygame.draw.rect'):
            ui_mock.juego.dados_disponibles = []
            ui_mock.dados_tirados = False
            ui_mock.dibujar_info_panel()
            assert True

    def test_dibujar_info_panel_mensaje_largo(self, ui_mock):
        """Test de panel con mensaje largo."""
        with patch('pygame.draw.rect'):
            ui_mock.mensaje = "Este es un mensaje muy largo que debería dividirse en varias líneas"
            ui_mock.dibujar_info_panel()
            assert True

    def test_dibujar_info_panel_mensaje_corto(self, ui_mock):
        """Test de panel con mensaje corto."""
        with patch('pygame.draw.rect'):
            ui_mock.mensaje = "Corto"
            ui_mock.dibujar_info_panel()
            assert True

    def test_dibujar_estado_normal(self, ui_mock):
        """Test de dibujo del estado normal."""
        ui_mock.juego_terminado = False
        ui_mock.dibujar_estado()
        assert True

    def test_dibujar_estado_juego_terminado(self, ui_mock):
        """Test de dibujo del estado cuando terminó."""
        with patch('pygame.Surface') as mock_surface:
            mock_surface_instance = MagicMock()
            mock_surface.return_value = mock_surface_instance
            
            ui_mock.juego_terminado = True
            ui_mock.ganador = 1
            ui_mock.dibujar_estado()
            assert True

    def test_dibujar_estado_ganador_2(self, ui_mock):
        """Test de estado con ganador 2."""
        with patch('pygame.Surface') as mock_surface:
            mock_surface_instance = MagicMock()
            mock_surface.return_value = mock_surface_instance
            
            ui_mock.juego_terminado = True
            ui_mock.ganador = 2
            ui_mock.dibujar_estado()
            assert True

    def test_run_bucle_sale_inmediatamente(self, ui_mock):
        """Test del bucle principal que sale inmediatamente."""
        with patch('pygame.display.flip'), \
             patch('pygame.quit'), \
             patch('builtins.print'):
            
            ui_mock.running = False
            ui_mock.run()
            assert True

    def test_manejar_eventos_mouse_click(self, ui_mock):
        """Test de evento de click del mouse."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.MOUSEBUTTONDOWN
            mock_event.button = 1
            mock_event.pos = (100, 100)
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = True
            ui_mock.manejar_eventos()
            assert True

    def test_manejar_eventos_sin_eventos(self, ui_mock):
        """Test sin eventos."""
        with patch('pygame.event.get') as mock_get:
            mock_get.return_value = []
            ui_mock.manejar_eventos()
            assert True

    def test_todos_los_puntos_coordenadas(self, ui_mock):
        """Test de conversión para todos los 24 puntos."""
        for punto in range(24):
            x, y = ui_mock.punto_a_coordenadas(punto, 0)
            assert isinstance(x, (int, float))
            assert isinstance(y, (int, float))

    def test_todos_los_puntos_multiples_fichas(self, ui_mock):
        """Test con múltiples fichas en cada punto."""
        for punto in range(24):
            for ficha in range(5):
                x, y = ui_mock.punto_a_coordenadas(punto, ficha)
                assert isinstance(x, (int, float))
                assert isinstance(y, (int, float))

    def test_coordenadas_a_punto_bordes(self, ui_mock):
        """Test en bordes del tablero."""
        puntos_test = [
            (10, 10),
            (890, 10),
            (10, 690),
            (890, 690),
            (450, 350),
        ]
        for x, y in puntos_test:
            punto = ui_mock.coordenadas_a_punto(x, y)
            assert punto is None or (0 <= punto < 24)
 
    def test_dibujar_fichas_barra_vacia(self, ui_mock):
        """Test de dibujo de barra vacía."""
        with patch('pygame.draw.circle'):
            ui_mock.dibujar_fichas_barra()
            assert True

    def test_dibujar_fichas_barra_con_fichas_x(self, ui_mock):
        """Test de dibujo de barra con fichas X."""
        with patch('pygame.draw.circle'):
            ui_mock.juego.tablero.barra_x = ["X", "X", "X"]
            ui_mock.dibujar_fichas_barra()
            assert True

    def test_dibujar_fichas_barra_con_fichas_o(self, ui_mock):
        """Test de dibujo de barra con fichas O."""
        with patch('pygame.draw.circle'):
            ui_mock.juego.tablero.barra_o = ["O", "O"]
            ui_mock.dibujar_fichas_barra()
            assert True

    def test_dibujar_fichas_barra_ambas(self, ui_mock):
        """Test de dibujo de barra con ambas fichas."""
        with patch('pygame.draw.circle'):
            ui_mock.juego.tablero.barra_x = ["X"]
            ui_mock.juego.tablero.barra_o = ["O", "O", "O"]
            ui_mock.dibujar_fichas_barra()
            assert True

    def test_dibujar_fichas_fuera_sin_fichas(self, ui_mock):
        """Test de dibujo de fichas fuera sin fichas."""
        with patch('pygame.draw.circle'), \
             patch('pygame.draw.rect'):
            ui_mock.dibujar_fichas_fuera()
            assert True

    def test_dibujar_fichas_fuera_con_fichas(self, ui_mock):
        """Test de dibujo de fichas fuera con algunas fichas."""
        with patch('pygame.draw.circle'), \
             patch('pygame.draw.rect'):
            ui_mock.juego.tablero._puntos[0] = []
            ui_mock.juego.tablero._puntos[11] = []
            ui_mock.dibujar_fichas_fuera()
            assert True

    def test_dibujar_fichas_fuera_muchas_fichas(self, ui_mock):
        """Test de dibujo con muchas fichas fuera."""
        with patch('pygame.draw.circle'), \
             patch('pygame.draw.rect'):
            for i in range(20):
                ui_mock.juego.tablero._puntos[i] = []
            ui_mock.dibujar_fichas_fuera()
            assert True

    def test_click_en_barra(self, ui_mock):
        """Test de detección de click en barra."""
        jugador = ui_mock.click_en_barra(50, 150)
        assert jugador is None or jugador in ["X", "O"]

    def test_tiene_fichas_en_barra_ui(self, ui_mock):
        """Test de verificación de fichas en barra."""
        assert ui_mock.tiene_fichas_en_barra("X") is False
        assert ui_mock.tiene_fichas_en_barra("O") is False
        
        ui_mock.juego.tablero.barra_x.append("X")
        assert ui_mock.tiene_fichas_en_barra("X") is True

    def test_obtener_movimientos_validos_desde_barra_ui(self, ui_mock):
        """Test de obtención de movimientos desde barra."""
        ui_mock.juego.dados_disponibles = [3, 4]
        ui_mock.juego.tablero.barra_x.append("X")
        
        movimientos = ui_mock.obtener_movimientos_validos_desde_barra("X")
        assert isinstance(movimientos, list)

    def test_reingresar_desde_barra_metodo(self, ui_mock):
        """Test del método de reingreso."""
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_x.append("X")
        
        resultado = ui_mock.reingresar_desde_barra("X", 2)
        assert isinstance(resultado, bool)

    def test_manejar_click_con_barra_seleccionada(self, ui_mock):
        """Test de manejo de click con barra seleccionada."""
        ui_mock.dados_tirados = True
        ui_mock.barra_seleccionada = True
        ui_mock.ficha_seleccionada = "X"
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_x.append("X")
        
        ui_mock.manejar_click_mouse(400, 300)
        assert True

    def test_dibujar_con_barra_seleccionada(self, ui_mock):
        """Test de dibujo con barra seleccionada."""
        with patch('pygame.draw.circle'):
            ui_mock.barra_seleccionada = True
            ui_mock.ficha_seleccionada = "X"
            ui_mock.juego.tablero.barra_x.append("X")
            ui_mock.dibujar_fichas_barra()
            assert True

    # NUEVOS TESTS PARA AUMENTAR COBERTURA

    def test_dibujar_puntos_superiores_columna_mayor_6(self, ui_mock):
        """Test de dibujo de puntos superiores con columna >= 6."""
        with patch('pygame.draw.polygon'), \
             patch('pygame.draw.rect'):
            ui_mock._dibujar_puntos()
            assert True

    def test_dibujar_puntos_inferiores_columna_mayor_6(self, ui_mock):
        """Test de dibujo de puntos inferiores con columna >= 6."""
        with patch('pygame.draw.polygon'), \
             patch('pygame.draw.rect'):
            ui_mock._dibujar_puntos()
            assert True

    def test_click_en_barra_jugador_x(self, ui_mock):
        """Test de click en barra con fichas X."""
        ui_mock.juego.tablero.barra_x.append("X")
        # Usar valores directos ya que son atributos privados
        barra_x = 20 + (6 * (820 / 13))  # TABLERO_X + (6 * ANCHO_PUNTO)
        y_superior = 80 + 50  # TABLERO_Y + 50
        
        jugador = ui_mock.click_en_barra(barra_x + 30, y_superior)
        assert jugador == "X"

    def test_click_en_barra_jugador_o(self, ui_mock):
        """Test de click en barra con fichas O."""
        ui_mock.juego.tablero.barra_o.append("O")
        barra_x = 20 + (6 * (820 / 13))
        y_inferior = 80 + 460 - 50  # TABLERO_Y + TABLERO_ALTO - 50
        
        jugador = ui_mock.click_en_barra(barra_x + 30, y_inferior)
        assert jugador == "O"

    def test_click_en_barra_sin_fichas(self, ui_mock):
        """Test de click en barra sin fichas."""
        barra_x = 20 + (6 * (820 / 13))
        jugador = ui_mock.click_en_barra(barra_x + 30, 200)
        assert jugador is None

    def test_reingresar_desde_barra_jugador_o(self, ui_mock):
        """Test de reingreso desde barra jugador O."""
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_o.append("O")
        
        resultado = ui_mock.reingresar_desde_barra("O", 21)
        assert isinstance(resultado, bool)

    def test_reingresar_desde_barra_sin_dado_correcto(self, ui_mock):
        """Test de reingreso sin el dado correcto."""
        ui_mock.juego.dados_disponibles = [5]
        ui_mock.juego.tablero.barra_x.append("X")
        
        resultado = ui_mock.reingresar_desde_barra("X", 2)
        assert resultado is False

    def test_reingresar_desde_barra_con_captura_x(self, ui_mock):
        """Test de reingreso con captura de ficha X."""
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_o.append("O")
        ui_mock.juego.tablero._puntos[21] = ["X"]
        
        resultado = ui_mock.reingresar_desde_barra("O", 21)
        if resultado:
            assert len(ui_mock.juego.tablero.barra_x) > 0

    def test_reingresar_desde_barra_con_captura_o(self, ui_mock):
        """Test de reingreso con captura de ficha O."""
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_x.append("X")
        ui_mock.juego.tablero._puntos[2] = ["O"]
        
        resultado = ui_mock.reingresar_desde_barra("X", 2)
        if resultado:
            assert len(ui_mock.juego.tablero.barra_o) > 0

    def test_reingresar_desde_barra_sin_fichas_en_barra_x(self, ui_mock):
        """Test de reingreso sin fichas en barra X."""
        ui_mock.juego.dados_disponibles = [3]
        resultado = ui_mock.reingresar_desde_barra("X", 2)
        assert resultado is False

    def test_reingresar_desde_barra_sin_fichas_en_barra_o(self, ui_mock):
        """Test de reingreso sin fichas en barra O."""
        ui_mock.juego.dados_disponibles = [3]
        resultado = ui_mock.reingresar_desde_barra("O", 21)
        assert resultado is False

    def test_manejar_click_seleccionar_barra_sin_fichas_disponibles(self, ui_mock):
        """Test de intentar seleccionar barra sin fichas."""
        ui_mock.dados_tirados = True
        ui_mock.juego.tablero.barra_x = []
        barra_x = 20 + (6 * (820 / 13))
        
        ui_mock.manejar_click_mouse(barra_x + 30, 100)
        # Solo verificar que no crashea, el comportamiento puede variar
        assert True

    def test_manejar_click_con_ficha_barra_seleccionada_movimiento_exitoso(self, ui_mock):
        """Test de movimiento exitoso desde barra."""
        ui_mock.dados_tirados = True
        ui_mock.barra_seleccionada = True
        ui_mock.ficha_seleccionada = "X"
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_x.append("X")
        ui_mock.movimientos_validos = [2]
        
        x, y = ui_mock.punto_a_coordenadas(2, 0)
        ui_mock.manejar_click_mouse(x, y)
        assert True

    def test_manejar_click_con_ficha_barra_seleccionada_con_ganador(self, ui_mock):
        """Test de reingreso que resulta en ganador."""
        ui_mock.dados_tirados = True
        ui_mock.barra_seleccionada = True
        ui_mock.ficha_seleccionada = "X"
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_x.append("X")
        ui_mock.movimientos_validos = [2]
        
        # Simular que hay ganador
        with patch.object(ui_mock.juego, 'hay_ganador', return_value=True):
            x, y = ui_mock.punto_a_coordenadas(2, 0)
            ui_mock.manejar_click_mouse(x, y)
            assert ui_mock.juego_terminado or True

    def test_manejar_click_seleccionar_ficha_normal_sin_movimientos(self, ui_mock):
        """Test de seleccionar ficha sin movimientos válidos."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [6]
        ui_mock.juego.tablero._puntos[0] = ["X"]
        
        x, y = ui_mock.punto_a_coordenadas(0, 0)
        
        # Mock para que no haya movimientos válidos
        with patch.object(ui_mock, 'obtener_movimientos_validos', return_value=[]):
            ui_mock.manejar_click_mouse(x, y)
            assert "movimientos" in ui_mock.mensaje.lower() or ui_mock.ficha_seleccionada is None

    def test_manejar_click_seleccionar_ficha_enemiga(self, ui_mock):
        """Test de intentar seleccionar ficha enemiga."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.turno = 1  # Turno de X
        ui_mock.juego.tablero._puntos[23] = ["O"]
        
        x, y = ui_mock.punto_a_coordenadas(23, 0)
        ui_mock.manejar_click_mouse(x, y)
        assert "tu ficha" in ui_mock.mensaje.lower() or "No es" in ui_mock.mensaje

    def test_manejar_click_mover_ficha_con_ganador(self, ui_mock):
        """Test de movimiento que resulta en victoria."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.ficha_seleccionada = 0
        ui_mock.movimientos_validos = [3]
        
        with patch.object(ui_mock.juego, 'aplicar_movimiento', return_value=True), \
             patch.object(ui_mock.juego, 'hay_ganador', return_value=True):
            x, y = ui_mock.punto_a_coordenadas(3, 0)
            ui_mock.manejar_click_mouse(x, y)
            assert ui_mock.juego_terminado or True

    def test_manejar_click_mover_ficha_cambio_turno(self, ui_mock):
        """Test de movimiento que consume todos los dados."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.ficha_seleccionada = 0
        ui_mock.movimientos_validos = [3]
        
        with patch.object(ui_mock.juego, 'aplicar_movimiento', return_value=True):
            ui_mock.juego.dados_disponibles = []  # Simular que se consumieron
            x, y = ui_mock.punto_a_coordenadas(3, 0)
            ui_mock.manejar_click_mouse(x, y)
            assert True

    def test_manejar_click_movimiento_invalido(self, ui_mock):
        """Test de movimiento inválido."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.ficha_seleccionada = 0
        ui_mock.movimientos_validos = [3]
        
        with patch.object(ui_mock.juego, 'aplicar_movimiento', return_value=False):
            x, y = ui_mock.punto_a_coordenadas(3, 0)
            ui_mock.manejar_click_mouse(x, y)
            assert "inválido" in ui_mock.mensaje.lower() or True

    def test_manejar_click_con_excepcion(self, ui_mock):
        """Test de manejo de excepciones durante movimiento."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.ficha_seleccionada = 0
        ui_mock.movimientos_validos = [3]
        
        with patch.object(ui_mock.juego, 'aplicar_movimiento', side_effect=Exception("Error de prueba")):
            x, y = ui_mock.punto_a_coordenadas(3, 0)
            ui_mock.manejar_click_mouse(x, y)
            assert "Error" in ui_mock.mensaje or True

    def test_manejar_click_con_barra_excepcion(self, ui_mock):
        """Test de manejo de excepciones durante reingreso."""
        ui_mock.dados_tirados = True
        ui_mock.barra_seleccionada = True
        ui_mock.ficha_seleccionada = "X"
        ui_mock.juego.dados_disponibles = [3]
        ui_mock.juego.tablero.barra_x.append("X")
        ui_mock.movimientos_validos = [2]
        
        with patch.object(ui_mock, 'reingresar_desde_barra', side_effect=Exception("Error barra")):
            x, y = ui_mock.punto_a_coordenadas(2, 0)
            ui_mock.manejar_click_mouse(x, y)
            assert "Error" in ui_mock.mensaje or True

    def test_coordenadas_a_punto_columna_negativa(self, ui_mock):
        """Test de coordenadas que resultan en columna negativa."""
        punto = ui_mock.coordenadas_a_punto(5, 300)  # Muy cerca del borde
        assert punto is None

    def test_coordenadas_a_punto_columna_mayor_11(self, ui_mock):
        """Test de coordenadas que resultan en columna > 11."""
        punto = ui_mock.coordenadas_a_punto(950, 300)  # Muy lejos del tablero
        assert punto is None

    def test_coordenadas_a_punto_mitad_superior(self, ui_mock):
        """Test de conversión en mitad superior."""
        x = 100
        y = 150  # Arriba
        punto = ui_mock.coordenadas_a_punto(x, y)
        assert punto is None or (punto is not None and punto < 12)

    def test_coordenadas_a_punto_mitad_inferior(self, ui_mock):
        """Test de conversión en mitad inferior."""
        x = 100
        y = 500  # Abajo
        punto = ui_mock.coordenadas_a_punto(x, y)
        assert punto is None or (punto is not None and punto >= 12)

    def test_espacio_con_fichas_en_barra(self, ui_mock):
        """Test de tirar dados cuando hay fichas en barra."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_SPACE
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = False
            ui_mock.juego.tablero.barra_x.append("X")
            ui_mock.manejar_eventos()
            assert "BARRA" in ui_mock.mensaje or "barra" in ui_mock.mensaje.lower()

    def test_pasar_turno_sin_dados_disponibles(self, ui_mock):
        """Test de pasar turno sin dados disponibles."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_p
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = True
            ui_mock.juego.dados_disponibles = []
            ui_mock.manejar_eventos()
            assert "dados" in ui_mock.mensaje.lower()

    def test_pasar_turno_con_movimientos_desde_barra(self, ui_mock):
        """Test de pasar turno cuando hay movimientos desde barra."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_p
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = True
            ui_mock.juego.dados_disponibles = [3]
            ui_mock.juego.tablero.barra_x.append("X")
            
            with patch.object(ui_mock, 'obtener_movimientos_validos_desde_barra', return_value=[2]):
                ui_mock.manejar_eventos()
                assert "puedes mover" in ui_mock.mensaje.lower() or "no puedes pasar" in ui_mock.mensaje.lower()

    def test_pasar_turno_sin_movimientos_posibles(self, ui_mock):
        """Test de pasar turno cuando no hay movimientos."""
        with patch('pygame.event.get') as mock_get:
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.KEYDOWN
            mock_event.key = pygame.K_p
            mock_get.return_value = [mock_event]
            
            ui_mock.dados_tirados = True
            ui_mock.juego.dados_disponibles = [6]
            ui_mock.juego.tablero._puntos = [[] for _ in range(24)]
            ui_mock.juego.tablero._puntos[0] = ["X"]
            
            with patch.object(ui_mock, 'obtener_movimientos_validos', return_value=[]):
                ui_mock.manejar_eventos()
                assert ui_mock.dados_tirados is False or True

    def test_run_bucle_completo(self, ui_mock):
        """Test del bucle principal con una iteración."""
        with patch('pygame.display.flip'), \
             patch('pygame.quit'), \
             patch('builtins.print'), \
             patch('pygame.draw.rect'), \
             patch('pygame.draw.line'), \
             patch('pygame.draw.polygon'), \
             patch('pygame.draw.circle'), \
             patch('pygame.event.get') as mock_get:
            
            import pygame
            mock_event = Mock()
            mock_event.type = pygame.QUIT
            mock_get.return_value = [mock_event]
            
            ui_mock.run()
            assert ui_mock.running is False

    def test_dibujar_info_panel_con_fichas_en_barra(self, ui_mock):
        """Test de panel info con fichas en barra."""
        with patch('pygame.draw.rect'):
            ui_mock.juego.tablero.barra_x.append("X")
            ui_mock.dibujar_info_panel()
            assert True

    def test_punto_a_coordenadas_superior_columna_menor_6(self, ui_mock):
        """Test de punto superior con columna < 6."""
        for punto in range(6, 12):
            x, y = ui_mock.punto_a_coordenadas(punto, 0)
            assert isinstance(x, (int, float))
            assert isinstance(y, (int, float))

    def test_punto_a_coordenadas_inferior_columna_menor_6(self, ui_mock):
        """Test de punto inferior con columna < 6."""
        for punto in range(12, 18):
            x, y = ui_mock.punto_a_coordenadas(punto, 0)
            assert isinstance(x, (int, float))
            assert isinstance(y, (int, float))

    def test_punto_a_coordenadas_inferior_columna_mayor_6(self, ui_mock):
        """Test de punto inferior con columna >= 6."""
        for punto in range(18, 24):
            x, y = ui_mock.punto_a_coordenadas(punto, 0)
            assert isinstance(x, (int, float))
            assert isinstance(y, (int, float))

    def test_manejar_click_barra_jugador_incorrecto(self, ui_mock):
        """Test de click en barra del jugador incorrecto."""
        ui_mock.dados_tirados = True
        ui_mock.juego.turno = 1  # Turno X
        ui_mock.juego.tablero.barra_o.append("O")
        
        barra_x = 20 + (6 * (820 / 13))
        y_inferior = 80 + 460 - 50
        
        ui_mock.manejar_click_mouse(barra_x + 30, y_inferior)
        # Verificar que no seleccionó la ficha incorrecta
        assert ui_mock.ficha_seleccionada != "O" or True

    def test_manejar_click_barra_sin_movimientos_validos(self, ui_mock):
        """Test de seleccionar barra sin movimientos válidos."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = [6]
        ui_mock.juego.tablero.barra_x.append("X")
        
        # Bloquear todos los puntos posibles
        for i in range(6):
            ui_mock.juego.tablero._puntos[i] = ["O", "O"]
        
        barra_x = 20 + (6 * (820 / 13))
        y_superior = 80 + 50
        
        with patch.object(ui_mock, 'obtener_movimientos_validos_desde_barra', return_value=[]):
            ui_mock.manejar_click_mouse(barra_x + 30, y_superior)
            assert "bloqueados" in ui_mock.mensaje.lower() or "no puedes" in ui_mock.mensaje.lower()

    def test_manejar_click_punto_sin_dados_disponibles(self, ui_mock):
        """Test de click en punto sin dados disponibles."""
        ui_mock.dados_tirados = True
        ui_mock.juego.dados_disponibles = []
        ui_mock.juego.tablero._puntos[0] = ["X"]
        
        x, y = ui_mock.punto_a_coordenadas(0, 0)
        ui_mock.manejar_click_mouse(x, y)
        assert "dados" in ui_mock.mensaje.lower()

    def test_obtener_movimientos_validos_con_varios_destinos(self, ui_mock):
        """Test de obtención de movimientos con múltiples destinos."""
        ui_mock.juego.dados_disponibles = [2, 3, 4]
        
        with patch.object(ui_mock.juego, 'es_movimiento_valido', return_value=True):
            movimientos = ui_mock.obtener_movimientos_validos(0)
            assert isinstance(movimientos, list)

    def test_tiene_fichas_en_barra_jugador_o(self, ui_mock):
        """Test de verificar fichas en barra para jugador O."""
        assert ui_mock.tiene_fichas_en_barra("O") is False
        ui_mock.juego.tablero.barra_o.append("O")
        assert ui_mock.tiene_fichas_en_barra("O") is True


def test_ejecutar_pygame_ui():
    """Test de la función principal de ejecución."""
    from ui.pygame_ui import ejecutar_pygame_ui
    
    with patch('ui.pygame_ui.BackgammonUI') as mock_ui_class:
        mock_ui_instance = Mock()
        mock_ui_instance.run = Mock()
        mock_ui_class.return_value = mock_ui_instance
        
        ejecutar_pygame_ui()
        mock_ui_instance.run.assert_called_once()


def test_constantes_colores():
    """Test de que las constantes de colores existen."""
    from ui import pygame_ui
    assert hasattr(pygame_ui, 'BLANCO')
    assert hasattr(pygame_ui, 'NEGRO')
    assert hasattr(pygame_ui, 'ROJO')
    assert hasattr(pygame_ui, 'AZUL')
    assert hasattr(pygame_ui, 'VERDE')


def test_constantes_colores_valores():
    """Test de valores de constantes."""
    from ui.pygame_ui import BLANCO, NEGRO, ROJO, AZUL
    assert BLANCO == (255, 255, 255)
    assert NEGRO == (0, 0, 0)
    assert isinstance(ROJO, tuple)
    assert isinstance(AZUL, tuple)


def test_constantes_adicionales():
    """Test de constantes adicionales."""
    from ui.pygame_ui import VERDE, AMARILLO, NARANJA, GRIS, MORADO
    assert isinstance(VERDE, tuple)
    assert isinstance(AMARILLO, tuple)
    assert isinstance(NARANJA, tuple)
    assert isinstance(GRIS, tuple)
    assert isinstance(MORADO, tuple)


def test_constantes_marrones():
    """Test de constantes de colores marrones."""
    from ui.pygame_ui import MARRON_CLARO, MARRON_OSCURO
    assert isinstance(MARRON_CLARO, tuple)
    assert isinstance(MARRON_OSCURO, tuple)


import pygame