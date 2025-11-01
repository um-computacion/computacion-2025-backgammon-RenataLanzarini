# 🎲 Proyecto Backgammon – Computación 

## 👩‍🎓 Alumna
- **Nombre:** María Renata Lanzarini  
- **Carrera:** Ingeniería en Informática  
- **Materia:** Computación – Universidad de Mendoza  
- **Año:** 2025  


## 📌 Descripción
Este proyecto implementa una versión simplificada del **juego Backgammon** en Python, usando una arquitectura modular y con interfaces en **línea de comandos (CLI)** y **pygame (UI gráfica)**.  
Incluye pruebas automáticas con **pytest** y sigue buenas prácticas de organización de repositorio.



## 📂 Estructura del proyecto
```text
core/
   board.py        # Tablero con 24 puntos
   game.py         # Núcleo del juego (estado, turno)
   dice.py         # Dados con manejo de dobles
   player.py       # Jugador y fichas
cli/
   cli.py          # Interfaz de línea de comandos
ui/
   pygame_ui.py    # Interfaz gráfica con pygame
resources/
   resource.py     # Gestión de recursos
tests/
   test_board.py       # Test del tablero
   test_cli.py         # Test de la interfaz CLI
   test_pygame_ui.py   # Test de la interfaz pygame
main.py            # Punto de entrada
requirements.txt   # Dependencias del proyecto


## ▶️ Ejecución
# 1. Crear entorno virtual
Es recomendable usar un entorno virtual para mantener las dependencias aisladas:
python3 -m venv .venv
source .venv/bin/activate    # En Linux/Mac
# .venv\Scripts\activate     # En Windows PowerShell

# 2. Instalar dependencias
Con el entorno virtual activo:
pip install --upgrade pip
pip install -r requirements.txt

# 3. Ejecutar el juego en CLI
Desde la raíz del proyecto:
python main.py
Esto muestra un mensaje de inicio del juego en la consola.

# 4. Ejecutar la interfaz gráfica con pygame
Podés abrir la interfaz gráfica directamente:
python -m ui.pygame_ui
Esto abre una ventana de pygame con el tablero básico.

# 5. Correr los tests
Para validar el código:
pytest -q
## 🐳 Ejecución con Docker

### Modo Juego (CLI)
```bash
docker build -t backgammon .
docker run -it backgammon
```

### Modo Testing
```bash
docker-compose up backgammon-tests
```
