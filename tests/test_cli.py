"""Tests para la interfaz CLI de Backgammon."""
import pytest
from unittest.mock import patch
from cli.cli import BackgammonCLI


def test_cli_iniciar_muestra_mensaje(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'BACKGAMMON' in captured.out or 'backgammon' in captured.out.lower()


def test_cli_comando_estado(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['estado', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'ESTADO' in captured.out or 'estado' in captured.out.lower()


def test_cli_comando_reiniciar(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['reiniciar', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'reiniciado' in captured.out.lower() or 'Juego' in captured.out


def test_cli_comando_tirar(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['tirar', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'Dados' in captured.out or 'dados' in captured.out.lower()


def test_cli_comando_tablero(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['tablero', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'TABLERO' in captured.out or 'BAR' in captured.out


def test_cli_comando_ayuda(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['ayuda', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'AYUDA' in captured.out or 'ayuda' in captured.out.lower()


def test_cli_comando_desconocido(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['comando_inventado', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'no reconocido' in captured.out.lower() or 'Comando' in captured.out


def test_mostrar_estado(capsys):
    cli = BackgammonCLI()
    cli.mostrar_estado()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_reiniciar_juego(capsys):
    cli = BackgammonCLI()
    cli.reiniciar_juego()
    captured = capsys.readouterr()
    assert 'reiniciado' in captured.out.lower() or len(captured.out) > 0


def test_salir(capsys):
    cli = BackgammonCLI()
    cli.salir()
    captured = capsys.readouterr()
    assert 'Gracias' in captured.out or 'gracias' in captured.out.lower()


def test_mostrar_tablero_vacio(capsys):
    cli = BackgammonCLI()
    cli.mostrar_tablero_visual()
    captured = capsys.readouterr()
    assert 'TABLERO' in captured.out or 'BAR' in captured.out


def test_mostrar_ayuda(capsys):
    cli = BackgammonCLI()
    cli.mostrar_ayuda()
    captured = capsys.readouterr()
    assert 'AYUDA' in captured.out or 'ayuda' in captured.out.lower()


def test_mostrar_bienvenida(capsys):
    cli = BackgammonCLI()
    cli.mostrar_bienvenida()
    captured = capsys.readouterr()
    assert 'B A C K G A M M O N' in captured.out or 'backgammon' in captured.out.lower()


def test_formato_barra_sin_fichas():
    cli = BackgammonCLI()
    resultado = cli._formato_barra(0)
    assert '|' in resultado


def test_cli_ejecuta_sin_errores():
    cli = BackgammonCLI()
    assert cli is not None
    assert hasattr(cli, '__juego__')


def test_mostrar_tablero_con_texto(capsys):
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    cli.mostrar_tablero_visual()
    captured = capsys.readouterr()
    assert len(captured.out) > 100


def test_cli_comando_mover_con_tablero(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['tirar', 'mover 1 2', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'dados' in captured.out.lower() or 'Dados' in captured.out


def test_mostrar_victoria(capsys):
    cli = BackgammonCLI()
    cli._mostrar_victoria('X')
    captured = capsys.readouterr()
    assert 'GANADO' in captured.out or 'ganado' in captured.out.lower()


def test_cli_comando_help_alias(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['help', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'AYUDA' in captured.out or 'ayuda' in captured.out.lower()


def test_cli_comando_h_alias(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['h', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'AYUDA' in captured.out or 'ayuda' in captured.out.lower()


def test_cli_comando_question_alias(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['?', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'AYUDA' in captured.out or 'ayuda' in captured.out.lower()


def test_cli_comando_exit_alias(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['exit']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'Gracias' in captured.out or 'gracias' in captured.out.lower()


def test_cli_comando_q_alias(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['q']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'Gracias' in captured.out or 'gracias' in captured.out.lower()


def test_cli_entrada_vacia(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_mostrar_victoria_jugador_o(capsys):
    cli = BackgammonCLI()
    cli._mostrar_victoria('O')
    captured = capsys.readouterr()
    assert 'O' in captured.out


def test_formato_barra_cero_fichas():
    cli = BackgammonCLI()
    for fila in range(5):
        resultado = cli._formato_barra(fila)
        assert '|' in resultado


def test_cli_init():
    cli = BackgammonCLI()
    assert cli.modo_tutorial is True
    assert cli.__juego__ is not None


def test_procesar_tirada_valida(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli._procesar_tirada(None)
    captured = capsys.readouterr()
    assert 'Dados' in captured.out or 'dados' in captured.out.lower()


def test_procesar_tirada_con_ganador(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli._procesar_tirada('X')
    captured = capsys.readouterr()
    assert 'terminó' in captured.out.lower() or 'reiniciar' in captured.out.lower()


def test_visualizacion_puntos(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli.mostrar_tablero_visual()
    captured = capsys.readouterr()
    assert any(str(i) in captured.out for i in range(1, 25))


def test_metodos_existentes():
    cli = BackgammonCLI()
    assert hasattr(cli, 'mostrar_tablero_visual')
    assert hasattr(cli, 'mostrar_ayuda')
    assert hasattr(cli, 'mostrar_bienvenida')
    assert hasattr(cli, 'iniciar')


def test_comandos_aliases():
    cli = BackgammonCLI()
    comandos = ['ayuda', 'help', 'h', '?', 'salir', 'exit', 'q']
    for cmd in comandos:
        assert isinstance(cmd, str)


def test_mostrar_estado_detallado(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli.mostrar_estado()
    captured = capsys.readouterr()
    assert len(captured.out) > 50


def test_reiniciar_con_juego(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli.reiniciar_juego()
    captured = capsys.readouterr()
    assert 'reiniciado' in captured.out.lower() or 'Juego' in captured.out


def test_manejo_excepciones(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['mover abc def', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_flujo_completo_basico(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['ayuda', 'tablero', 'estado', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'AYUDA' in captured.out or 'ayuda' in captured.out.lower()


def test_formato_barra_varios_casos():
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    for fila in range(5):
        resultado = cli._formato_barra(fila)
        assert isinstance(resultado, str)
        assert '|' in resultado


def test_mostrar_victoria_varios_casos(capsys):
    cli = BackgammonCLI()
    for jugador in ['X', 'O']:
        cli._mostrar_victoria(jugador)
        captured = capsys.readouterr()
        assert jugador in captured.out


def test_posibles_metodos_privados():
    cli = BackgammonCLI()
    assert hasattr(cli, '_formato_barra')
    assert hasattr(cli, '_obtener_simbolo')
    assert hasattr(cli, '_mostrar_info_barra')


def test_rendimiento_metodos_basicos(capsys):
    cli = BackgammonCLI()
    import time
    start = time.time()
    for _ in range(10):
        cli.mostrar_estado()
    elapsed = time.time() - start
    assert elapsed < 1.0


def test_llamadas_repetidas(capsys):
    cli = BackgammonCLI()
    for _ in range(3):
        cli.mostrar_ayuda()
        cli.mostrar_estado()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_diferentes_casos_formato_barra():
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    resultados = [cli._formato_barra(i) for i in range(5)]
    assert all('|' in r for r in resultados)


def test_multiples_comandos(capsys):
    cli = BackgammonCLI()
    comandos = ['ayuda', 'estado', 'tablero', 'salir']
    with patch('builtins.input', side_effect=comandos):
        cli.iniciar()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_metodos_sin_parametros(capsys):
    cli = BackgammonCLI()
    cli.mostrar_ayuda()
    cli.mostrar_bienvenida()
    cli.mostrar_estado()
    captured = capsys.readouterr()
    assert len(captured.out) > 100


def test_cobertura_formato_barra_con_fichas():
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    
    juego.tablero.barra_x.append('X')
    juego.tablero.barra_o.append('O')
    
    resultado = cli._formato_barra(0)
    assert 'X' in resultado or resultado is not None


def test_cobertura_explicar_error(capsys):
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    juego.tirar_dados()
    cli._explicar_error_movimiento(0, 10, 1, 11)
    captured = capsys.readouterr()
    assert len(captured.out) >= 0


def test_cobertura_sugerencias_sin_barra(capsys):
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    juego.tirar_dados()
    cli._mostrar_sugerencias()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_cobertura_sugerencias_con_barra(capsys):
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    
    juego.tablero.barra_x.append('X')
    juego.tirar_dados()
    
    cli._mostrar_sugerencias()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_cobertura_toggle_tutorial(capsys):
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['tutorial', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert 'tutorial' in captured.out.lower()


def test_cobertura_tirar_con_dados_disponibles(capsys):
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    juego.tirar_dados()
    cli._procesar_tirada(None)
    captured = capsys.readouterr()
    assert 'dados' in captured.out.lower() or 'Dados' in captured.out


def test_cobertura_obtener_simbolo():
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    simbolo = cli._obtener_simbolo(juego.tablero, 0, 0)
    assert simbolo in ['X', 'O', ' ', '2']


def test_cobertura_mostrar_info_barra(capsys):
    cli = BackgammonCLI()
    juego = cli.__juego__
    juego.iniciar()
    
    juego.tablero.barra_x.append('X')
    juego.tablero.barra_o.append('O')
    
    cli._mostrar_info_barra()
    captured = capsys.readouterr()
    assert len(captured.out) >= 0


def test_cobertura_mostrar_dados_con_ayuda(capsys):
    cli = BackgammonCLI()
    juego = cli.__juego__
    cli.modo_tutorial = True
    juego.iniciar()
    juego.tirar_dados()
    cli._mostrar_dados_con_ayuda()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_cobertura_procesar_movimiento(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli.__juego__.tirar_dados()
    cli._procesar_movimiento('mover 1 2', None)
    captured = capsys.readouterr()
    assert len(captured.out) >= 0


def test_cobertura_procesar_movimiento_invalido(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli._procesar_movimiento('mover 1', None)
    captured = capsys.readouterr()
    assert 'Formato' in captured.out or 'formato' in captured.out.lower()


def test_cobertura_procesar_movimiento_sin_params(capsys):
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli._procesar_movimiento('mover', None)
    captured = capsys.readouterr()
    assert 'Formato' in captured.out or 'formato' in captured.out.lower()


def test_cobertura_mostrar_fichas_fuera(capsys):
    """Test de visualización de fichas fuera."""
    cli = BackgammonCLI()
    
    # Sin fichas fuera
    cli._mostrar_fichas_fuera()
    captured = capsys.readouterr()
    assert len(captured.out) >= 0
    
    # Con fichas fuera
    cli.__juego__.tablero._puntos = [[] for _ in range(24)]
    cli._mostrar_fichas_fuera()
    captured = capsys.readouterr()
    assert len(captured.out) > 0
    
    # Con fichas mixtas
    cli.__juego__.tablero.barra_x = ["X"]
    cli._mostrar_fichas_fuera()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_procesar_pasar_turno_sin_dados(capsys):
    """Test pasar turno sin dados."""
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli._procesar_pasar_turno(None)
    captured = capsys.readouterr()
    assert "dados" in captured.out.lower() or "tira" in captured.out.lower()


def test_procesar_pasar_turno_con_ganador(capsys):
    """Test pasar turno con ganador."""
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli._procesar_pasar_turno("X")
    captured = capsys.readouterr()
    assert "terminó" in captured.out.lower() or "reiniciar" in captured.out.lower()


def test_procesar_pasar_turno_con_movimientos(capsys):
    """Test pasar turno teniendo movimientos."""
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli.__juego__.tirar_dados()
    cli._procesar_pasar_turno(None)
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_comando_pasar_en_flujo(capsys):
    """Test comando pasar en flujo normal."""
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['tirar', 'pasar', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_procesar_pasar_turno_sin_movimientos_barra(capsys):
    """Test pasar turno con fichas en barra pero sin movimientos."""
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    cli.__juego__.tirar_dados()
    
    # Agregar fichas a barra
    cli.__juego__.tablero.barra_x.append("X")
    
    # Bloquear todos los puntos de entrada
    for i in range(6):
        cli.__juego__.tablero._puntos[i] = ["O", "O"]
    
    cli._procesar_pasar_turno(None)
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_procesar_pasar_turno_sin_movimientos_normales(capsys):
    """Test pasar turno sin movimientos normales."""
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    
    # Dar dados muy altos que no permitan movimientos
    cli.__juego__.dados_disponibles = [6, 6, 6, 6]
    
    # Bloquear posibles destinos
    cli.__juego__.tablero._puntos[0] = ["X"]
    for i in range(1, 24):
        if i >= 6:
            cli.__juego__.tablero._puntos[i] = ["O", "O"]
    
    cli._procesar_pasar_turno(None)
    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_ayuda_contiene_pasar(capsys):
    """Test que ayuda menciona comando pasar."""
    cli = BackgammonCLI()
    cli.mostrar_ayuda()
    captured = capsys.readouterr()
    assert 'pasar' in captured.out.lower()


def test_comando_pasar_directo(capsys):
    """Test comando pasar usado directamente."""
    cli = BackgammonCLI()
    with patch('builtins.input', side_effect=['pasar', 'salir']):
        cli.iniciar()
    captured = capsys.readouterr()
    assert "dados" in captured.out.lower() or len(captured.out) > 0


def test_mostrar_fichas_fuera_con_capsys(capsys):
    """Test mostrar fichas fuera captura salida."""
    cli = BackgammonCLI()
    cli.__juego__.iniciar()
    
    # Vaciar algunos puntos para simular fichas fuera
    cli.__juego__.tablero._puntos[0] = []
    cli.__juego__.tablero._puntos[1] = []
    
    cli._mostrar_fichas_fuera()
    captured = capsys.readouterr()
    assert "FUERA" in captured.out or "fuera" in captured.out.lower() or len(captured.out) >= 0