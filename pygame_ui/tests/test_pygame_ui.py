from pygame_ui.py import BackgammonUI

def test_ui_inicia_juego():
    ui= BackgammonUI()

    assert hasattr(ui, "_Backgammon__juego__")
    