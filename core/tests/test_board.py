from core.board import Tablero

def test_tablero_inicia_con_24_puntos():
    tablero = Tablero()
    assert len(tablero._Tablero__puntos__) == 24

def test_tablero_contar_fichas_vacio():
    tablero = Tablero()
    assert tablero.contar_fichas() == 0

def test_tablero_esta_vacio_al_crear():
    tablero = Tablero()
    assert tablero.esta_vacio(0) is True
