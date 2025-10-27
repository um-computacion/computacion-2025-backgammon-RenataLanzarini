from cli.cli import BackgammonCLI
from unittest.mock import patch
import pytest

def test_cli_posee_juego():
    cli = BackgammonCLI()
    assert hasattr(cli, "juego")

def test_cli_inicializa_juego():
    cli = BackgammonCLI()
    assert cli.juego is not None

@patch('builtins.input', side_effect=['salir'])
def test_cli_iniciar_muestra_mensaje(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "Bienvenido" in captured.out
    assert "comenzado" in captured.out

@patch('builtins.input', side_effect=['estado', 'salir'])
def test_cli_comando_estado(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "Estado:" in captured.out

@patch('builtins.input', side_effect=['reiniciar', 'salir'])
def test_cli_comando_reiniciar(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "reinició" in captured.out

@patch('builtins.input', side_effect=['tirar', 'salir'])
def test_cli_comando_tirar(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "Dados:" in captured.out

@patch('builtins.input', side_effect=['mover 0 5', 'salir'])
def test_cli_comando_mover_invalido(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "inválido" in captured.out

@patch('builtins.input', side_effect=['mover', 'salir'])
def test_cli_comando_mover_mal_formato(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "Uso:" in captured.out

@patch('builtins.input', side_effect=['mover abc def', 'salir'])
def test_cli_comando_mover_no_enteros(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "enteros" in captured.out

@patch('builtins.input', side_effect=['comando_invalido', 'salir'])
def test_cli_comando_desconocido(mock_input, capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    captured = capsys.readouterr()
    assert "Comandos:" in captured.out

def test_mostrar_estado(capsys):
    cli = BackgammonCLI()
    cli.mostrar_estado()
    captured = capsys.readouterr()
    assert "Estado:" in captured.out

def test_reiniciar_juego(capsys):
    cli = BackgammonCLI()
    cli.reiniciar_juego()
    captured = capsys.readouterr()
    assert "reinició" in captured.out

def test_salir(capsys):
    cli = BackgammonCLI()
    cli.salir()
    captured = capsys.readouterr()
    assert "Gracias" in captured.out

def test_mostrar_estado_con_dados(capsys):
    cli = BackgammonCLI()
    cli.juego.dados_disponibles = [3, 4]
    cli.mostrar_estado()
    captured = capsys.readouterr()
    assert "Dados disponibles:" in captured.out