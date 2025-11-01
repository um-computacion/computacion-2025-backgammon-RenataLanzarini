"""Tests completos para BackgammonJuego """
import pytest
from core.game import BackgammonJuego


class TestEstadosDelJuego:
    """Tests para los estados del juego."""
    
    def test_estado_inicial(self):
        juego = BackgammonJuego()
        assert juego.estado == "inicial"
        assert juego.turno == 1

    def test_iniciar_cambia_estado(self):
        juego = BackgammonJuego()
        juego.iniciar()
        assert juego.estado == "jugando"
        assert juego.en_juego()

    def test_pausar_cambia_estado(self):
        juego = BackgammonJuego()
        juego.pausar()
        assert juego.estado == "pausado"
        assert not juego.en_juego()

    def test_finalizar_cambia_estado(self):
        juego = BackgammonJuego()
        juego.finalizar()
        assert juego.estado == "finalizado"
        assert not juego.en_juego()

    def test_reiniciar(self):
        juego = BackgammonJuego()
        juego.iniciar()
        juego.finalizar()
        juego.dados_disponibles = [3, 4]
        juego.turno = 2
        
        juego.reiniciar()
        
        assert juego.estado == "inicial"
        assert juego.turno == 1
        assert juego.dados_disponibles == []
        assert juego.tablero.contar_fichas() == 30


class TestPropiedades:
    """Tests para getters y setters."""
    
    def test_propiedad_estado(self):
        juego = BackgammonJuego()
        juego.estado = "pausado"
        assert juego.estado == "pausado"
    
    def test_propiedad_turno(self):
        juego = BackgammonJuego()
        juego.turno = 2
        assert juego.turno == 2
    
    def test_propiedad_tablero(self):
        juego = BackgammonJuego()
        assert juego.tablero is not None
        assert len(juego.tablero._puntos) == 24
    
    def test_propiedad_jugadores(self):
        juego = BackgammonJuego()
        assert juego.jugador_x.nombre == "Jugador 1"
        assert juego.jugador_x.color == "X"
        assert juego.jugador_o.nombre == "Jugador 2"
        assert juego.jugador_o.color == "O"
    
    def test_propiedad_dados(self):
        juego = BackgammonJuego()
        assert juego.dados is not None
    
    def test_propiedad_dados_disponibles(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = [3, 4]
        assert juego.dados_disponibles == [3, 4]


class TestTurnos:
    """Tests para manejo de turnos."""
    
    def test_cambiar_turno(self):
        juego = BackgammonJuego()
        assert juego.turno == 1
        juego.cambiar_turno()
        assert juego.turno == 2
        juego.cambiar_turno()
        assert juego.turno == 1

    def test_cambiar_turno_limpia_dados(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = [3, 4, 5]
        juego.cambiar_turno()
        assert juego.dados_disponibles == []

    def test_jugador_actual(self):
        juego = BackgammonJuego()
        assert juego.jugador_actual() == 1
        juego.cambiar_turno()
        assert juego.jugador_actual() == 2


class TestDados:
    """Tests para lógica de dados."""
    
    def test_tirar_dados(self):
        juego = BackgammonJuego()
        valores = juego.tirar_dados()
        assert isinstance(valores, list)
        assert len(valores) in [2, 4]  # 2 dados o 4 si son dobles
        for valor in valores:
            assert 1 <= valor <= 6

    def test_tirar_dados_actualiza_disponibles(self):
        juego = BackgammonJuego()
        valores = juego.tirar_dados()
        assert juego.dados_disponibles == valores

    def test_tiene_dados_disponibles_true(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = [3, 4]
        assert juego.tiene_dados_disponibles()

    def test_tiene_dados_disponibles_false(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = []
        assert not juego.tiene_dados_disponibles()


class TestDescripcion:
    """Tests para método descripcion."""
    
    def test_descripcion_formato(self):
        juego = BackgammonJuego()
        juego.tirar_dados()
        desc = juego.descripcion()
        
        assert isinstance(desc, str)
        assert "Estado:" in desc
        assert "Turno actual:" in desc
        assert "Dados:" in desc
        assert "Dados disponibles:" in desc
        assert "Tablero:" in desc
    
    def test_descripcion_jugador_1(self):
        juego = BackgammonJuego()
        desc = juego.descripcion()
        assert "Jugador 1" in desc
    
    def test_descripcion_jugador_2(self):
        juego = BackgammonJuego()
        juego.cambiar_turno()
        desc = juego.descripcion()
        assert "Jugador 2" in desc


class TestMovimientosBasicos:
    """Tests para movimientos básicos."""
    
    def test_movimientos_disponibles(self):
        juego = BackgammonJuego()
        movimientos = juego.movimientos_disponibles()
        assert isinstance(movimientos, list)
        assert len(movimientos) > 0  # Hay fichas en el tablero

    def test_colocar_ficha_punto_valido(self):
        juego = BackgammonJuego()
        punto = 10
        fichas_antes = juego.tablero.fichas_en(punto)
        juego.colocar_ficha(punto, "X")
        assert juego.tablero.fichas_en(punto) == fichas_antes + 1

    def test_colocar_ficha_punto_invalido(self):
        juego = BackgammonJuego()
        # Punto inválido no debería hacer nada
        juego.colocar_ficha(25, "X")
        # Solo verificar que no crashea


class TestValidacionMovimientos:
    """Tests para validación de movimientos."""
    
    def test_movimiento_valido_jugador_x(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [3]
        # Punto 0 tiene fichas X en configuración inicial
        assert juego.es_movimiento_valido(0, 3)

    def test_movimiento_valido_jugador_o(self):
        juego = BackgammonJuego()
        juego.turno = 2
        juego.dados_disponibles = [3]
        # Punto 23 tiene fichas O en configuración inicial
        assert juego.es_movimiento_valido(23, 20)

    def test_movimiento_sin_dados(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = []
        assert not juego.es_movimiento_valido(0, 3)

    def test_movimiento_origen_invalido(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = [3]
        assert not juego.es_movimiento_valido(-5, 3)
        assert not juego.es_movimiento_valido(25, 28)

    def test_movimiento_destino_invalido(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = [3]
        assert not juego.es_movimiento_valido(0, -1)
        assert not juego.es_movimiento_valido(0, 25)

    def test_movimiento_origen_vacio(self):
        juego = BackgammonJuego()
        juego.tablero.reset()
        juego.dados_disponibles = [3]
        assert not juego.es_movimiento_valido(0, 3)

    def test_movimiento_ficha_incorrecta(self):
        juego = BackgammonJuego()
        juego.turno = 1  # Jugador X
        juego.dados_disponibles = [3]
        # Punto 23 tiene fichas O
        assert not juego.es_movimiento_valido(23, 20)

    def test_movimiento_distancia_incorrecta(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [2, 5]
        # Intentar mover 3 espacios (no hay dado de 3)
        assert not juego.es_movimiento_valido(0, 3)

    def test_movimiento_distancia_negativa(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [3]
        # Jugador X debe mover hacia adelante
        assert not juego.es_movimiento_valido(5, 2)

    def test_movimiento_bloqueado_dos_fichas(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "X")
        juego.tablero.colocar_ficha(3, "O")
        juego.tablero.colocar_ficha(3, "O")
        juego.dados_disponibles = [3]
        assert not juego.es_movimiento_valido(0, 3)

    def test_movimiento_bloqueado_mas_de_dos_fichas(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "X")
        for _ in range(5):
            juego.tablero.colocar_ficha(3, "O")
        juego.dados_disponibles = [3]
        assert not juego.es_movimiento_valido(0, 3)

    def test_movimiento_sobre_ficha_propia(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [11]
        # Punto 0 y 11 tienen fichas X
        assert juego.es_movimiento_valido(0, 11)


class TestAplicarMovimientos:
    """Tests para aplicar movimientos."""
    
    def test_aplicar_movimiento_exitoso(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [3]
        resultado = juego.aplicar_movimiento(0, 3)
        assert resultado is True
        assert 3 not in juego.dados_disponibles

    def test_aplicar_movimiento_invalido(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = []
        resultado = juego.aplicar_movimiento(0, 3)
        assert resultado is False

    def test_aplicar_movimiento_consume_dado(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [3, 4]
        juego.aplicar_movimiento(0, 3)
        assert len(juego.dados_disponibles) == 1
        assert 3 not in juego.dados_disponibles

    def test_aplicar_varios_movimientos(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [2, 3]
        
        # Primer movimiento
        juego.aplicar_movimiento(0, 2)
        assert len(juego.dados_disponibles) == 1
        
        # Segundo movimiento
        juego.aplicar_movimiento(11, 14)
        assert len(juego.dados_disponibles) == 0

    def test_aplicar_movimiento_con_dobles(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [3, 3, 3, 3]
        
        resultado = juego.aplicar_movimiento(0, 3)
        assert resultado is True
        assert len(juego.dados_disponibles) == 3


class TestCaptura:
    """Tests para captura de fichas."""
    
    def test_captura_ficha_enemiga(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "X")
        juego.tablero.colocar_ficha(3, "O")
        juego.dados_disponibles = [3]
        
        assert juego.tablero.fichas_en_barra("O") == 0
        resultado = juego.aplicar_movimiento(0, 3)
        
        assert resultado is True
        assert juego.tablero.fichas_en_barra("O") == 1

    def test_captura_no_ocurre_con_ficha_propia(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "X")
        juego.tablero.colocar_ficha(3, "X")
        juego.dados_disponibles = [3]
        
        juego.aplicar_movimiento(0, 3)
        
        # Ambas fichas X están en el punto 3
        assert juego.tablero.fichas_en(3) == 2
        assert juego.tablero.fichas_en_barra("X") == 0


class TestBarra:
    """Tests para reingreso desde la barra."""
    
    def test_puede_reingresar_desde_barra_x(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3]
        
        puede, dado = juego.puede_reingresar_desde_barra(2)  # punto 2 = dado 3
        assert puede is True
        assert dado == 3

    def test_puede_reingresar_desde_barra_o(self):
        juego = BackgammonJuego()
        juego.turno = 2
        juego.tablero.barra_o.append("O")
        juego.dados_disponibles = [3]
        
        puede, dado = juego.puede_reingresar_desde_barra(21)  # punto 21 = dado 3
        assert puede is True
        assert dado == 3

    def test_no_puede_reingresar_sin_fichas_en_barra(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [3]
        
        puede, dado = juego.puede_reingresar_desde_barra(2)
        assert puede is False

    def test_no_puede_reingresar_sin_dado_correcto(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [5]
        
        puede, dado = juego.puede_reingresar_desde_barra(2)  # punto 2 necesita dado 3
        assert puede is False

    def test_no_puede_reingresar_punto_bloqueado(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.barra_x.append("X")
        juego.tablero.colocar_ficha(2, "O")
        juego.tablero.colocar_ficha(2, "O")
        juego.dados_disponibles = [3]
        
        puede, dado = juego.puede_reingresar_desde_barra(2)
        assert puede is False

    def test_puede_reingresar_punto_con_una_ficha_enemiga(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.barra_x.append("X")
        juego.tablero.colocar_ficha(2, "O")
        juego.dados_disponibles = [3]
        
        puede, dado = juego.puede_reingresar_desde_barra(2)
        assert puede is True

    def test_reingreso_desde_barra_exitoso(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3]
        
        resultado = juego.aplicar_movimiento(-1, 2)
        
        assert resultado is True
        assert juego.tablero.fichas_en_barra("X") == 0
        assert juego.tablero.fichas_en(2) == 1

    def test_reingreso_con_captura(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.barra_x.append("X")
        juego.tablero.colocar_ficha(2, "O")
        juego.dados_disponibles = [3]
        
        resultado = juego.aplicar_movimiento(-1, 2)
        
        assert resultado is True
        assert juego.tablero.fichas_en_barra("X") == 0
        assert juego.tablero.fichas_en_barra("O") == 1

    def test_debe_reingresar_antes_de_mover(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3]
        
        # No puede mover otras fichas si tiene en la barra
        resultado = juego.aplicar_movimiento(0, 3)
        assert resultado is False

    def test_obtener_movimientos_validos_desde_barra_x(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3, 5]
        
        movimientos = juego.obtener_movimientos_validos_desde_barra("X")
        
        assert 2 in movimientos  # dado 3 -> punto 2
        assert 4 in movimientos  # dado 5 -> punto 4

    def test_obtener_movimientos_validos_desde_barra_o(self):
        juego = BackgammonJuego()
        juego.turno = 2
        juego.tablero.reset()
        juego.tablero.barra_o.append("O")
        juego.dados_disponibles = [3, 5]
        
        movimientos = juego.obtener_movimientos_validos_desde_barra("O")
        
        assert 21 in movimientos  # dado 3 -> punto 21
        assert 19 in movimientos  # dado 5 -> punto 19

    def test_obtener_movimientos_desde_barra_sin_fichas(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [3, 5]
        
        movimientos = juego.obtener_movimientos_validos_desde_barra("X")
        assert movimientos == []

    def test_obtener_movimientos_desde_barra_jugador_incorrecto(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3]
        
        # Pedir movimientos de O cuando es turno de X
        movimientos = juego.obtener_movimientos_validos_desde_barra("O")
        assert movimientos == []

    def test_reingreso_x_fuera_de_home_board(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [5]
        
        # Punto 10 está fuera del home board de X (0-5)
        puede, _ = juego.puede_reingresar_desde_barra(10)
        assert puede is False

    def test_reingreso_o_fuera_de_home_board(self):
        juego = BackgammonJuego()
        juego.turno = 2
        juego.tablero.barra_o.append("O")
        juego.dados_disponibles = [5]
        
        # Punto 10 está fuera del home board de O (18-23)
        puede, _ = juego.puede_reingresar_desde_barra(10)
        assert puede is False


class TestGanadores:
    """Tests para verificación de ganadores."""
    
    def test_verificar_ganador_sin_ganador(self):
        juego = BackgammonJuego()
        assert juego.verificar_ganador() is None

    def test_verificar_ganador_x_gana(self):
        juego = BackgammonJuego()
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "O")
        assert juego.verificar_ganador() == "X"

    def test_verificar_ganador_o_gana(self):
        juego = BackgammonJuego()
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "X")
        assert juego.verificar_ganador() == "O"

    def test_hay_ganador_true(self):
        juego = BackgammonJuego()
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "O")
        assert juego.hay_ganador() is True

    def test_hay_ganador_false(self):
        juego = BackgammonJuego()
        assert juego.hay_ganador() is False

    def test_ganador_con_fichas_en_barra(self):
        juego = BackgammonJuego()
        juego.tablero.reset()
        juego.tablero.barra_x.append("X")
        juego.tablero.colocar_ficha(0, "O")
        # X tiene fichas en barra, no ha ganado
        assert juego.verificar_ganador() is None

    def test_ganador_sin_fichas_en_barra(self):
        juego = BackgammonJuego()
        juego.tablero.reset()
        juego.tablero.colocar_ficha(0, "O")
        # X no tiene fichas, gana
        assert juego.verificar_ganador() == "X"


class TestCasosEdge:
    """Tests para casos especiales y edge cases."""
    
    def test_movimiento_con_todos_los_dados_iguales(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.dados_disponibles = [2, 2, 2, 2]
        
        # Usar los 4 dados
        assert juego.aplicar_movimiento(0, 2)
        assert len(juego.dados_disponibles) == 3

    def test_reingreso_punto_destino_invalido(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3]
        
        puede, _ = juego.puede_reingresar_desde_barra(25)
        assert puede is False

    def test_aplicar_movimiento_origen_y_destino_iguales(self):
        juego = BackgammonJuego()
        juego.dados_disponibles = [0]
        resultado = juego.aplicar_movimiento(5, 5)
        assert resultado is False

    def test_movimiento_jugador_o_direccion_correcta(self):
        """Test movimiento válido del jugador O."""
        juego = BackgammonJuego()
        juego.turno = 2
        juego.tablero.reset()
        # Colocar una ficha O en punto 18
        juego.tablero.colocar_ficha(18, "O")
        # Para mover de 18 a 15 necesita dado 3 (18 - 15 = 3)
        juego.dados_disponibles = [3]
        assert juego.es_movimiento_valido(18, 15)

    def test_movimiento_jugador_o_direccion_incorrecta(self):
        juego = BackgammonJuego()
        juego.turno = 2
        juego.dados_disponibles = [5]
        # O no puede mover hacia adelante
        assert not juego.es_movimiento_valido(18, 23)

    def test_multiple_captura_en_partida(self):
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        
        # Setup: X en 0, O en 3 y 6
        juego.tablero.colocar_ficha(0, "X")
        juego.tablero.colocar_ficha(3, "O")
        juego.tablero.colocar_ficha(6, "O")
        
        # Primera captura
        juego.dados_disponibles = [3]
        juego.aplicar_movimiento(0, 3)
        assert juego.tablero.fichas_en_barra("O") == 1
        
        # Segunda captura
        juego.dados_disponibles = [3]
        juego.aplicar_movimiento(3, 6)
        assert juego.tablero.fichas_en_barra("O") == 2

    def test_todos_los_puntos_posiciones_validas(self):
        """Verifica que todos los 24 puntos son válidos."""
        juego = BackgammonJuego()
        for i in range(24):
            assert juego.tablero.punto_valido(i)

    def test_reiniciar_mantiene_objetos(self):
        """Verifica que reiniciar no crea nuevos objetos."""
        juego = BackgammonJuego()
        tablero_original = juego.tablero
        dados_original = juego.dados
        
        juego.reiniciar()
        
        assert juego.tablero is tablero_original
        assert juego.dados is dados_original


class TestBarraAdicionales:
    """Tests adicionales para mejorar cobertura de la barra."""
    
    def test_aplicar_movimiento_barra_sin_poder_reingresar(self):
        """Test cuando se intenta reingresar pero no se puede."""
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3]
        
        # Bloquear el punto 2 (donde debería entrar con dado 3)
        juego.tablero.colocar_ficha(2, "O")
        juego.tablero.colocar_ficha(2, "O")
        
        resultado = juego.aplicar_movimiento(-1, 2)
        assert resultado is False
    
    def test_reingreso_jugador_o_con_captura(self):
        """Test reingreso del jugador O con captura."""
        juego = BackgammonJuego()
        juego.turno = 2
        juego.tablero.reset()
        juego.tablero.barra_o.append("O")
        juego.tablero.colocar_ficha(21, "X")  # Una ficha X en punto 21
        juego.dados_disponibles = [3]  # dado 3 -> punto 21
        
        resultado = juego.aplicar_movimiento(-1, 21)
        assert resultado is True
        assert juego.tablero.fichas_en_barra("O") == 0
        assert juego.tablero.fichas_en_barra("X") == 1
    
    def test_obtener_movimientos_barra_con_puntos_bloqueados(self):
        """Test obtener movimientos cuando algunos puntos están bloqueados."""
        juego = BackgammonJuego()
        juego.turno = 1
        juego.tablero.reset()
        juego.tablero.barra_x.append("X")
        juego.dados_disponibles = [3, 5]
        
        # Bloquear punto 2 (dado 3)
        juego.tablero.colocar_ficha(2, "O")
        juego.tablero.colocar_ficha(2, "O")
        
        movimientos = juego.obtener_movimientos_validos_desde_barra("X")
        
        assert 2 not in movimientos  # Bloqueado
        assert 4 in movimientos  # dado 5 -> punto 4, disponible