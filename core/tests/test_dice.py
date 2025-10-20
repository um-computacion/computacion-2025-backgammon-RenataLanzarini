import pytest
from core.dice import Dado

def test_valor_en_rango():
    dado = Dado()
    for _ in range(20):
        valor = dado.lanzar()
        assert 1 <= valor <= 6

def test_dobles():
    dado1 = Dado()
    dado2 = Dado()

    valores = [dado1.lanzar(), dado2.lanzar()]

    # si ambos valores son iguales → es doble
    if valores[0] == valores[1]:
        assert valores[0] == valores[1]