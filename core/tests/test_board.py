from core.board import Tablero

def test_tablero_inicia_sin_fichas_y_con_24_puntos():
    tablero = Tablero()
    # Al iniciar, no debe haber fichas
    assert tablero.contar_fichas() == 0
    # Los 24 puntos existen y están vacíos
    assert all(tablero.esta_vacio(i) for i in range(24))
