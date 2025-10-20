import unittest

try:
    from core.player import Jugador  # si tu clase se llama Player, cambiá el nombre aquí
except ImportError:
    Jugador = None

class TestJugador(unittest.TestCase):
    def test_clase_existe(self):
        self.assertIsNotNone(Jugador, "No se pudo importar la clase Jugador desde core.player")

    def test_inicializacion_basica(self):
        self.assertIsNotNone(Jugador, "Falta clase Jugador")
        j = Jugador(nombre="Alice")
        # Debe tener atributo nombre
        self.assertTrue(hasattr(j, "nombre"), "El jugador debería tener atributo 'nombre'")
        self.assertEqual(j.nombre, "Alice")
        # Debe tener atributo fichas (o similar); si tu atributo se llama distinto, avisame y lo ajusto
        self.assertTrue(hasattr(j, "fichas"), "El jugador debería tener atributo 'fichas'")
        # Número de fichas no negativo
        self.assertGreaterEqual(getattr(j, "fichas"), 0, "Las fichas no deben ser negativas")

    def test_representacion_str(self):
        self.assertIsNotNone(Jugador, "Falta clase Jugador")
        j = Jugador(nombre="Bob")
        # No exigimos un formato exacto, solo que __str__ no rompa y devuelva str
        self.assertIsInstance(str(j), str)

if __name__ == "__main__":
    unittest.main()