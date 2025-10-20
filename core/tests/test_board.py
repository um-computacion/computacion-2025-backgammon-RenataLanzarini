from core.board import Tablero

def test_tablero_inicia_sin_fichas_y_con_24_puntos():
    tablero = Tablero()
    # Al iniciar, no debe haber fichas
    assert tablero.contar_fichas() == 0
    # Los 24 puntos existen y están vacíos
    assert all(tablero.esta_vacio(i) for i in range(24))

def test_colocar_y_quitar_ficha():
    tablero = Tablero()
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