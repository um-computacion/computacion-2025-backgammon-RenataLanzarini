import sys
import pytest
import main

def test_main_cli(monkeypatch, capsys):
    monkeypatch.setattr("cli.cli.ejecutar_cli", lambda: print("CLI CALLED"))
    monkeypatch.setattr("pygame_ui.pygame_ui.ejecutar_pygame_ui", lambda: None)

    sys.argv = ["main.py", "cli"]
    main.main()
    out = capsys.readouterr().out
    assert "Iniciando Backgammon en modo CLI..." in out
    assert "CLI CALLED" in out

def test_main_ui(monkeypatch, capsys):
    monkeypatch.setattr("pygame_ui.pygame_ui.ejecutar_pygame_ui", lambda: print("UI CALLED"))
    monkeypatch.setattr("cli.cli.ejecutar_cli", lambda: None)

    sys.argv = ["main.py", "ui"]
    main.main()
    out = capsys.readouterr().out
    assert "Iniciando Backgammon en modo Pygame UI..." in out
    assert "UI CALLED" in out

def test_main_argumento_invalido(monkeypatch, capsys):
    monkeypatch.setattr("cli.cli.ejecutar_cli", lambda: None)
    monkeypatch.setattr("pygame_ui.pygame_ui.ejecutar_pygame_ui", lambda: None)

    sys.argv = ["main.py", "otro"]
    main.main()
    out = capsys.readouterr().out
    assert "Opción inválida" in out

def test_main_sin_argumentos(monkeypatch, capsys):
    monkeypatch.setattr("cli.cli.ejecutar_cli", lambda: None)
    monkeypatch.setattr("pygame_ui.pygame_ui.ejecutar_pygame_ui", lambda: None)

    sys.argv = ["main.py"]
    with pytest.raises(SystemExit) as excinfo:
        main.main()
    assert excinfo.value.code == 1
    out = capsys.readouterr().out
    assert "Uso: python main.py [cli|ui]" in out