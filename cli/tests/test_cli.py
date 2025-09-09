from cli.cli import BackgammonCLI

def test_cli_posee_juego():
    cli = BackgammonCLI()
    # El CLI debe tener una instancia del juego
    assert hasattr(cli, "juego")
    