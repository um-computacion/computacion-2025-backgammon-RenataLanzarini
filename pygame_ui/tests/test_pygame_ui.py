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
    