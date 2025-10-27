import pytest
from core.dice import Dados

def test_valor_en_rango():
    dados = Dados()
    for _ in range(20):
        valores = dados.tirar()
        for valor in valores:
            assert 1 <= valor <= 6, f"Valor {valor} fuera de rango"

def test_dobles():
    dados = Dados()
    # Tiramos varias veces hasta encontrar dobles o verificar que funciona
    for _ in range(100):
        valores = dados.tirar()
        # Si es doble, debe devolver 4 valores iguales
        if len(valores) == 4:
            assert valores[0] == valores[1] == valores[2] == valores[3]
            break
        # Si no es doble, debe devolver 2 valores diferentes
        else:
            assert len(valores) == 2
            # No necesariamente son diferentes, pero debe haber 2

def test_tirar_devuelve_lista():
    dados = Dados()
    resultado = dados.tirar()
    assert isinstance(resultado, list)
    assert len(resultado) in [2, 4]  # 2 normales o 4 si es doble

def test_valores_property():
    dados = Dados()
    assert dados.valores == []  # Al inicio está vacío
    dados.tirar()
    assert len(dados.valores) in [2, 4]  # Después de tirar tiene valores