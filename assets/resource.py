"""
Módulo Resource para gestionar recursos del juego Backgammon.
"""

class Recurso:
    """Clase que representa un recurso del juego."""

    def __init__(self, nombre: str, ruta: str):
        self.__nombre__ = nombre
        self.__ruta__ = ruta

    def descripcion(self) -> str:
        """
        Devuelve una cadena con información del recurso.
        """
        return f"Recurso: {self.__nombre__}, ruta: {self.__ruta__}"
