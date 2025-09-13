from core.game import BackgammonJuego

def test_estado_inicial():
    juego = BackgammonJuego()
    # Verifica que al crear el juego esté en estado "inicial"
    assert juego._BackgammonJuego__estado__ == "inicial"

def test_iniciar_cambia_estado():
    juego = BackgammonJuego()
    juego.iniciar()
    # Verifica que después de iniciar el estado pase a "jugando"
    assert juego._BackgammonJuego__estado__ == "jugando"