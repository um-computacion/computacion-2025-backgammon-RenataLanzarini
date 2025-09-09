"""
Módulo Resource para gestionar recursos del juego Backgammon.
"""

class Recurso:
    """Clase que representa un recurso del juego."""

    def __init__(self, nombre: str, ruta: str):
        self.nombre = nombre
        self.ruta = ruta

    def descripcion(self) -> str:
        """
        Devuelve una cadena con información del recurso.
        """
        return f"Recurso: {self.nombre}, ruta: {self.ruta}"
