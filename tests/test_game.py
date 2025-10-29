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
    # CORRECCIÓN: Usar un punto que esté vacío en configuración inicial
    punto_vacio = 4  # Este punto debería estar vacío
    fichas_originales = juego.tablero.fichas_en(punto_vacio)
    juego.colocar_ficha(punto_vacio, "X")
    assert juego.tablero.fichas_en(punto_vacio) == fichas_originales + 1

def test_es_movimiento_valido():
    juego = BackgammonJuego()
    # CORRECCIÓN: Configurar escenario válido
    juego.turno = 1  # Asegurar turno de jugador X
    juego.dados_disponibles = [3]
    # El punto 0 tiene fichas X en configuración inicial
    assert juego.es_movimiento_valido(0, 3)

def test_es_movimiento_invalido():
    juego = BackgammonJuego()
    assert not juego.es_movimiento_valido(-1, 5)
    assert not juego.es_movimiento_valido(0, 25)
    assert not juego.es_movimiento_valido(0, 5)

def test_aplicar_movimiento():
    juego = BackgammonJuego()
    # CORRECCIÓN: Configurar escenario válido
    juego.turno = 1  # Jugador X
    juego.dados_disponibles = [3]
    # El punto 0 tiene fichas X
    resultado = juego.aplicar_movimiento(0, 3)
    assert resultado is True

def test_aplicar_movimiento_invalido_completo():
    juego = BackgammonJuego()
    # Intentar mover sin fichas
    resultado = juego.aplicar_movimiento(0, 5)
    assert resultado is False
    
def test_jugador_incorrecto():
    juego = BackgammonJuego()
    # CORRECCIÓN: Usar punto que no tenga fichas del jugador actual
    juego.tablero.reset()
    juego.colocar_ficha(0, "O")  # Ficha del jugador 2
    juego.dados_disponibles = [5]
    # Turno del jugador 1, no puede mover ficha de jugador 2
    resultado = juego.aplicar_movimiento(0, 5)
    assert resultado is False

def test_reiniciar_configura_tablero():
    juego = BackgammonJuego()
    juego.reiniciar()
    # Después de reiniciar, el tablero debe tener 30 fichas
    assert juego.tablero.contar_fichas() == 30
    assert juego.tablero.contar_fichas_jugador("X") == 15
    assert juego.tablero.contar_fichas_jugador("O") == 15

def test_tirar_dados_actualiza_disponibles():
    juego = BackgammonJuego()
    valores = juego.tirar_dados()
    # Los dados disponibles deben ser iguales a los valores tirados
    assert juego.dados_disponibles == valores

def test_movimiento_sin_dados():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()
    # Sin tirar dados, no se puede mover
    resultado = juego.aplicar_movimiento(0, 3)
    assert resultado is False

def test_movimiento_con_dado_correcto():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()
    # CORRECCIÓN: Asegurar turno correcto
    juego.turno = 1
    juego.dados_disponibles = [3, 4]
    # Mover 3 espacios desde el punto 0
    resultado = juego.aplicar_movimiento(0, 3)
    assert resultado is True

def test_movimiento_distancia_incorrecta():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()
    juego.dados_disponibles = [2, 5]
    # Intentar mover 3 espacios (no hay dado de 3)
    resultado = juego.aplicar_movimiento(0, 3)
    assert resultado is False

def test_cambiar_turno_limpia_dados():
    juego = BackgammonJuego()
    juego.dados_disponibles = [3, 4]
    juego.cambiar_turno()
    assert juego.dados_disponibles == []

def test_tiene_dados_disponibles():
    juego = BackgammonJuego()
    assert not juego.tiene_dados_disponibles()
    juego.dados_disponibles = [3, 4]
    assert juego.tiene_dados_disponibles()

def test_usar_todos_los_dados():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()
    juego.turno = 1
    juego.dados_disponibles = [2, 3]
    
    # Usar el dado de 2 - mover de 0 a 2
    juego.aplicar_movimiento(0, 2)
    assert len(juego.dados_disponibles) == 1
    
    # CORRECCIÓN: Mover desde el punto 11 (tiene 5 fichas X) usando el dado 3
    # 11 + 3 = 14 (punto 14 está vacío en configuración inicial)
    juego.aplicar_movimiento(11, 14)
    assert len(juego.dados_disponibles) == 0

def test_movimiento_con_dobles():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()
    juego.turno = 1
    # Simular dobles (4 dados iguales)
    juego.dados_disponibles = [3, 3, 3, 3]
    # Usar el primer 3
    resultado = juego.aplicar_movimiento(0, 3)
    assert resultado is True
    assert len(juego.dados_disponibles) == 3

def test_movimiento_con_captura():
    juego = BackgammonJuego()
    # CORRECCIÓN: Configurar escenario de captura válido
    juego.turno = 1
    juego.tablero.reset()
    # Colocar 1 ficha enemiga en el destino
    juego.tablero.colocar_ficha(5, "O")
    juego.tablero.colocar_ficha(0, "X")
    juego.dados_disponibles = [5]
    # Mover y capturar
    resultado = juego.aplicar_movimiento(0, 5)
    assert resultado is True

def test_movimiento_bloqueado_por_oponente():
    juego = BackgammonJuego()
    # Colocar 2 fichas enemigas (bloqueo)
    juego.tablero.reset()
    juego.tablero.colocar_ficha(5, "O")
    juego.tablero.colocar_ficha(5, "O")
    juego.tablero.colocar_ficha(0, "X")
    juego.dados_disponibles = [5]
    # No se puede mover a punto bloqueado
    resultado = juego.aplicar_movimiento(0, 5)
    assert resultado is False

def test_reingreso_desde_barra():
    juego = BackgammonJuego()
    # Poner ficha en la barra
    juego.tablero.barra_x.append("X")
    juego.dados_disponibles = [3]
    # Reingresar desde la barra (origen=-1)
    resultado = juego.aplicar_movimiento(-1, 2)
    assert resultado is True

def test_debe_reingresar_antes_de_mover():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()
    # Poner ficha en la barra
    juego.tablero.barra_x.append("X")
    juego.dados_disponibles = [3]
    # No puede mover otras fichas si tiene en la barra
    resultado = juego.aplicar_movimiento(0, 3)
    assert resultado is False

def test_verificar_ganador_sin_ganador():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()
    # Con fichas en el tablero, no hay ganador
    assert juego.verificar_ganador() is None

def test_verificar_ganador_x_gana():
    juego = BackgammonJuego()
    # Quitar todas las fichas X del tablero
    juego.tablero.reset()
    # Solo poner fichas O
    juego.tablero.colocar_ficha(0, "O")
    juego.tablero.colocar_ficha(1, "O")
    # X no tiene fichas, debería ganar
    assert juego.verificar_ganador() == "X"

def test_verificar_ganador_o_gana():
    juego = BackgammonJuego()
    juego.tablero.reset()
    # Solo poner fichas X
    juego.tablero.colocar_ficha(0, "X")
    juego.tablero.colocar_ficha(1, "X")
    # O no tiene fichas, debería ganar
    assert juego.verificar_ganador() == "O"

def test_hay_ganador():
    juego = BackgammonJuego()
    juego.tablero.configurar_inicial()  # Tablero con fichas
    assert not juego.hay_ganador()
    juego.tablero.reset()
    juego.tablero.colocar_ficha(0, "O")  # Solo quedan fichas O
    assert juego.hay_ganador()

def test_ganador_con_fichas_en_barra():
    juego = BackgammonJuego()
    juego.tablero.reset()
    # Poner fichas X solo en la barra
    juego.tablero.barra_x.append("X")
    juego.tablero.colocar_ficha(0, "O")
    # X tiene fichas en barra, no ha ganado
    assert juego.verificar_ganador() is None
    # Quitar de la barra
    juego.tablero.barra_x.clear()
    # Ahora X no tiene fichas, gana
    assert juego.verificar_ganador() == "X"