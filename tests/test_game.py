from core.game import BackgammonJuego

def test_estado_inicial():
    juego = BackgammonJuego()
    # Verifica que al crear el juego esté en estado "inicial"
    assert juego.estado == "inicial"

def test_iniciar_cambia_estado():
    juego = BackgammonJuego()
    juego.iniciar()
    # Verifica que después de iniciar el estado pase a "jugando"
    assert juego.estado == "jugando"

def test_pausar_cambia_estado():
    juego = BackgammonJuego()
    juego.pausar()
    assert juego.estado == "pausado"

def test_finalizar_cambia_estado():
    juego = BackgammonJuego()
    juego.finalizar()
    assert juego.estado == "finalizado"

def test_reiniciar():
    juego = BackgammonJuego()
    juego.iniciar()
    juego.reiniciar()
    assert juego.estado == "inicial"
    assert juego.turno == 1

def test_en_juego():
    juego = BackgammonJuego()
    assert not juego.en_juego()
    juego.iniciar()
    assert juego.en_juego()

def test_cambiar_turno():
    juego = BackgammonJuego()
    assert juego.turno == 1
    juego.cambiar_turno()
    assert juego.turno == 2
    juego.cambiar_turno()
    assert juego.turno == 1

def test_jugador_actual():
    juego = BackgammonJuego()
    assert juego.jugador_actual() == 1
    juego.cambiar_turno()
    assert juego.jugador_actual() == 2

def test_tirar_dados():
    juego = BackgammonJuego()
    valores = juego.tirar_dados()
    assert isinstance(valores, list)
    assert len(valores) in [2, 4]

def test_descripcion():
    juego = BackgammonJuego()
    desc = juego.descripcion()
    assert isinstance(desc, str)
    assert "Estado:" in desc
    assert "Turno" in desc

def test_movimientos_disponibles():
    juego = BackgammonJuego()
    movimientos = juego.movimientos_disponibles()
    assert isinstance(movimientos, list)

def test_colocar_ficha():
    juego = BackgammonJuego()
    juego.colocar_ficha(0, "X")
    assert juego.tablero.fichas_en(0) == 1

def test_es_movimiento_valido():
    juego = BackgammonJuego()
    juego.colocar_ficha(0, "X")
    assert juego.es_movimiento_valido(0, 5)

def test_es_movimiento_invalido():
    juego = BackgammonJuego()
    assert not juego.es_movimiento_valido(-1, 5)
    assert not juego.es_movimiento_valido(0, 25)
    assert not juego.es_movimiento_valido(0, 5)

def test_aplicar_movimiento():
    juego = BackgammonJuego()
    juego.colocar_ficha(0, "X")
    resultado = juego.aplicar_movimiento(0, 5)
    assert resultado is True
    assert juego.tablero.fichas_en(5) == 1

def test_aplicar_movimiento_invalido_completo():
    juego = BackgammonJuego()
    # Intentar mover sin fichas
    resultado = juego.aplicar_movimiento(0, 5)
    assert resultado is False
    
def test_jugador_incorrecto():
    juego = BackgammonJuego()
    juego.colocar_ficha(0, "O")  # Ficha del jugador 2
    # Turno del jugador 1, no puede mover ficha de jugador 2
    resultado = juego.aplicar_movimiento(0, 5)
    assert resultado is False
