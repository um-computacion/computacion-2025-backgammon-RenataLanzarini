from cli.cli import BackgammonCLI

def test_cli_inicia_juego():
    cli = BackgammonCLI()

    assert hasattr (cli, "_BAckgammon__juego__")
    