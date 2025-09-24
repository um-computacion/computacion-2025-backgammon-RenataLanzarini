from assets import resource

def test_constantes_colores():
    assert isinstance(resource.BLANCO, tuple)
    assert resource.BLANCO == (255, 255, 255)
    assert resource.NEGRO == (0, 0, 0)

def test_constantes_ventana():
    assert resource.ANCHO_VENTANA == 800
    assert resource.ALTO_VENTANA == 600
    assert "Backgammon" in resource.TITULO_VENTANA

def test_clase_recurso_descripcion():
    r = resource.Recurso("ficha", "ruta/ficha.png")
    salida = r.descripcion()
    assert "ficha" in salida
    assert "ruta/ficha.png" in salida