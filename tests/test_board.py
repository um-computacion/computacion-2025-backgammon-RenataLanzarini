from core.board import Tablero

def test_tablero_inicia_sin_fichas_y_con_24_puntos():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    # Al iniciar, no debe haber fichas
    assert tablero.contar_fichas() == 0
    # Los 24 puntos existen y están vacíos
    assert all(tablero.esta_vacio(i) for i in range(24))

def test_colocar_y_quitar_ficha():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    tablero.colocar_ficha(0, "X")
    assert not tablero.esta_vacio(0)
    assert tablero.contar_fichas() == 1

    tablero.quitar_ficha(0)
    assert tablero.esta_vacio(0)
    assert tablero.contar_fichas() == 0

def test_representacion_str():
    tablero = Tablero()
    # Verifica que __str__ no rompa y devuelva texto
    assert isinstance(str(tablero), str)

def test_punto_valido():
    tablero = Tablero()
    assert tablero.punto_valido(0)
    assert tablero.punto_valido(23)
    assert not tablero.punto_valido(-1)
    assert not tablero.punto_valido(24)

def test_tablero_vacio():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    assert tablero.tablero_vacio()
    tablero.colocar_ficha(0, "X")
    assert not tablero.tablero_vacio()

def test_limpiar_punto():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    tablero.colocar_ficha(5, "X")
    tablero.colocar_ficha(5, "X")
    assert tablero.fichas_en(5) == 2
    tablero.limpiar_punto(5)
    assert tablero.fichas_en(5) == 0

def test_total_puntos():
    tablero = Tablero()
    assert tablero.total_puntos() == 24

def test_mover_ficha():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    tablero.colocar_ficha(0, "X")
    tablero.mover_ficha(0, 5)
    assert tablero.fichas_en(0) == 0
    assert tablero.fichas_en(5) == 1

def test_mover_ficha_error():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    import pytest
    with pytest.raises(ValueError):
        tablero.mover_ficha(0, 5)

def test_colocar_ficha_invalida():
    tablero = Tablero()
    import pytest
    with pytest.raises(ValueError):
        tablero.colocar_ficha(25, "X")

def test_reset_con_fichas():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    for i in range(5):
        tablero.colocar_ficha(i, "X")
    tablero.reset()
    assert len(tablero) == 0

def test_ficha_en_punto_vacio():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    assert tablero.ficha_en(0) is None

def test_quitar_ficha_vacia():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    assert tablero.quitar_ficha(0) is None

def test_configurar_inicial():
    tablero = Tablero()
    tablero.configurar_inicial()
    # Verificar que hay 30 fichas en total (15 por jugador)
    assert tablero.contar_fichas() == 30
    
def test_configurar_inicial_fichas_x():
    tablero = Tablero()
    tablero.configurar_inicial()
    # Verificar que el jugador X tiene 15 fichas
    assert tablero.contar_fichas_jugador("X") == 15
    
def test_configurar_inicial_fichas_o():
    tablero = Tablero()
    tablero.configurar_inicial()
    # Verificar que el jugador O tiene 15 fichas
    assert tablero.contar_fichas_jugador("O") == 15

def test_configurar_inicial_posiciones():
    tablero = Tablero()
    tablero.configurar_inicial()
    # Verificar algunas posiciones específicas
    assert tablero.fichas_en(0) == 2  # 2 fichas X en punto 0
    assert tablero.fichas_en(23) == 2  # 2 fichas O en punto 23
    assert tablero.fichas_en(11) == 5  # 5 fichas X en punto 11
    assert tablero.fichas_en(12) == 5  # 5 fichas O en punto 12

def test_contar_fichas_jugador():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    tablero.colocar_ficha(0, "X")
    tablero.colocar_ficha(1, "X")
    tablero.colocar_ficha(2, "O")
    assert tablero.contar_fichas_jugador("X") == 2
    assert tablero.contar_fichas_jugador("O") == 1

def test_barra_inicialmente_vacia():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    assert len(tablero.barra_x) == 0
    assert len(tablero.barra_o) == 0

def test_capturar_ficha_x():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    tablero.colocar_ficha(5, "X")
    tablero.capturar_ficha(5)
    assert tablero.fichas_en(5) == 0
    assert len(tablero.barra_x) == 1

def test_capturar_ficha_o():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    tablero.colocar_ficha(10, "O")
    tablero.capturar_ficha(10)
    assert tablero.fichas_en(10) == 0
    assert len(tablero.barra_o) == 1

def test_tiene_fichas_en_barra():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    assert not tablero.tiene_fichas_en_barra("X")
    tablero.barra_x.append("X")
    assert tablero.tiene_fichas_en_barra("X")

def test_sacar_de_barra():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    tablero.barra_x.append("X")
    ficha = tablero.sacar_de_barra("X")
    assert ficha == "X"
    assert len(tablero.barra_x) == 0

def test_fichas_en_barra():
    tablero = Tablero()
    tablero.reset()  # ← CORRECCIÓN: Resetear para tests
    assert tablero.fichas_en_barra("X") == 0
    tablero.barra_x.extend(["X", "X", "X"])
    assert tablero.fichas_en_barra("X") == 3
