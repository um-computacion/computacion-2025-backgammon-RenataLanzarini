from cli.cli import BackgammonCLI

def test_cli_posee_juego():
    cli = BackgammonCLI()
    # El CLI debe tener una instancia del juego
    assert hasattr(cli, "juego")

def test_cli_inicializa_juego():
    cli = BackgammonCLI()
    # La instancia de juego no debería ser None
    assert cli.juego is not None

def test_cli_iniciar_muestra_mensaje(capsys):
    cli = BackgammonCLI()
    cli.iniciar()
    salida = capsys.readouterr().out
    assert "Bienvenido a Backgammon (CLI)" in salida