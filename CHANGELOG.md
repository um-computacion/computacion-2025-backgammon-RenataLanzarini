# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] - 2025-10-31

### Added
- Implementación completa del juego Backgammon según reglas tradicionales
- Módulo core/ con lógica de negocio separada de interfaces
  - BackgammonJuego: Coordinación del flujo del juego
  - Board: Gestión del tablero y movimientos
  - Player: Representación de jugadores
  - Dice: Lógica de dados con manejo de dobles
- Interfaz CLI completamente funcional
  - Visualización ASCII del tablero
  - Entrada por comandos de texto
  - Validación de movimientos en tiempo real
- Interfaz gráfica con Pygame
  - Tablero visual interactivo
  - Sistema de click para selección de fichas
  - Indicadores visuales de movimientos válidos
  - Panel de información y controles
  - Gestión de fichas en barra y fuera del tablero
- Sistema completo de testing
  - 292 tests unitarios
  - Cobertura del 96% en módulo core
  - Integración con pytest y pytest-cov
- Análisis de calidad de código
  - Pylint score: 10.00/10
  - Integración con Coveralls para CI/CD
- Documentación técnica completa
  - README.md con instrucciones detalladas
  - JUSTIFICACION.md con decisiones de diseño
  - Archivos de prompts de IA utilizados
- Despliegue con Docker
  - Dockerfile optimizado
  - docker-compose.yml para múltiples modos

### Technical Implementation
- **Lenguaje:** Python 3.11+
- **Dependencias:** Pygame, pytest, pytest-cov, pylint
- **Arquitectura:** Separación completa lógica/presentación
- **Principios:** SOLID, DRY, clean code
- **Patrones:** MVC (Model-View-Controller)

## Desarrollo por Sprints

### Sprint 1 (2025-10-26)
- Setup inicial del proyecto
- Configuración de estructura de carpetas
- Implementación de clases base (Board, Player, Dice)
- Sistema de versionado con Git

### Sprint 2 (2025-10-27)
- Implementación completa de reglas de Backgammon
- Sistema de movimientos válidos
- Gestión de capturas
- Lógica de reingreso desde barra

### Sprint 3 (2025-10-28)
- Interfaz CLI funcional
- Interfaz Pygame con gráficos
- Integración de interfaces con lógica core

### Sprint 4 (2025-10-29)
- Batería completa de tests unitarios
- Optimización de cobertura (96%)
- Análisis de calidad con Pylint

### Sprint 5 (2025-10-31)
- Documentación completa
- Setup de Docker
- Preparación de archivos de prompts
- Revisión final y ajustes
