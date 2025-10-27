import os

# Configuración para entornos sin pantalla (CI/headless)
os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pytest
pygame = pytest.importorskip("pygame")

from ui.pygame_ui import BackgammonUI

def test_ui_posee_juego():
    ui = BackgammonUI()
    # La UI debe tener una instancia del juego
    assert hasattr(ui, "juego")
    
def test_ui_iniciar():
    ui = BackgammonUI()
    ui.iniciar()
    assert ui.running is True
    assert ui.screen is not None
    ui.cerrar()

def test_ui_cerrar():
    ui = BackgammonUI()
    ui.iniciar()
    ui.cerrar()
    assert ui.running is False

def test_ejecutar_pygame():
    from ui.pygame_ui import ejecutar_pygame_ui
    from unittest.mock import patch
    with patch('builtins.print'):
        ejecutar_pygame_ui()
