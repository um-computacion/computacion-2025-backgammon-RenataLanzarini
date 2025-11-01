# PROMPT TESTING - Estrategia de Testing y Cobertura

**Fecha:** 30 de Octubre, 2025  
**Estudiante:** Renata Lanzarini  
**Materia:** Computación 2025

---

## Contexto

Código funcionando, tests básicos escritos, pero cobertura en 65%. Necesito llegar a >90% y tengo problemas específicos con testing de componentes aleatorios y Pygame.

## Prompt Utilizado

```
Necesito ayuda con la estrategia de testing para mi proyecto Backgammon. El requisito es tener >90% de cobertura.

Situación actual:
- Tengo tests básicos funcionando
- Cobertura actual: ~65%
- Uso pytest

Mis problemas:

1. **Dados aleatorios:** No puedo testear los dados porque son aleatorios. Cada vez que corro el test, obtengo valores diferentes. ¿Cómo hago tests determinísticos para código aleatorio?

Ejemplo de mi test problemático:
```python
def test_tirar_dobles():
    dados = Dados()
    resultado = dados.tirar()
    # ¿Qué assert hago acá? A veces son dobles, a veces no
    assert len(resultado) == 4  # Esto solo funciona si son dobles
```

2. **Pygame en CI:** Mis tests de UI fallan en GitHub Actions con el error:
```
pygame.error: No available video device
```
¿Cómo testeo código de Pygame sin tener un display? ¿Debo mockear todo pygame?

3. **Edge cases:** ¿Qué casos límite debería testear? Tengo tests básicos pero no sé si son suficientes.

4. **Fixtures:** Veo que muchos de mis tests repiten el mismo código de setup. ¿Cómo uso fixtures de pytest correctamente?

¿Me podrías ayudar con estas dudas y sugerir una estrategia de testing completa?
```

## Respuesta Recibida

Me enseñaron técnicas para resolver estos problemas:

### 1. Testing de Componentes Aleatorios

Me explicaron cómo usar `@patch` para mockear:

```python
from unittest.mock import patch

@patch('random.randint')
def test_tirar_dobles(mock_randint):
    # Forzar que ambos dados sean 4
    mock_randint.side_effect = [4, 4]
    
    dados = Dados()
    resultado = dados.tirar()
    
    # Ahora el test es determinístico
    assert resultado == [4, 4, 4, 4]
    assert len(resultado) == 4

@patch('random.randint')
def test_tirar_normal(mock_randint):
    # Forzar dados diferentes
    mock_randint.side_effect = [3, 5]
    
    dados = Dados()
    resultado = dados.tirar()
    
    assert resultado == [3, 5]
    assert len(resultado) == 2
```

**Explicación recibida:** `@patch` reemplaza `random.randint` con un mock que devuelve valores controlados. Esto me permitió escribir tests determinísticos.

**Después de entender la técnica:** Escribí todos mis tests de dados usando esta estrategia.

### 2. Testing de Pygame - Solución al problema de CI

**Me explicaron:** Cómo mockear pygame para que funcione sin display

**Ejemplo que me dio:**

```python
from unittest.mock import patch, Mock

@patch('pygame.init')
@patch('pygame.display.set_mode')
@patch('pygame.display.set_caption')
@patch('pygame.font.Font')
def test_ui_inicializa(mock_font, mock_caption, mock_mode, mock_init):
    ui = BackgammonUI()
    
    # Verificar que se llamaron los métodos
    pygame.init.assert_called_once()
    pygame.display.set_mode.assert_called_once()
    
    # Verificar que la lógica se inicializó
    assert ui.juego is not None

@patch('pygame.event.get')
def test_manejo_eventos(mock_get):
    # Simular evento de mouse
    mock_event = Mock()
    mock_event.type = pygame.MOUSEBUTTONDOWN
    mock_event.pos = (100, 100)
    mock_get.return_value = [mock_event]
    
    ui = BackgammonUI()
    ui.manejar_eventos()
    # Verificar comportamiento esperado
```

**Trade-off que me ayudó a entender:** No testeo el renderizado real, solo la lógica. La IA me explicó que para este proyecto, 75% de cobertura en UI es aceptable porque:
- La lógica crítica está en core/ (>90%)
- El renderizado es difícil de testear automáticamente
- Testing manual complementa

**Mi decisión:** Acepté este trade-off y enfoqué mis esfuerzos en testear core/.

### 3. Edge Cases - Ideas sugeridas

La IA me sugirió **qué casos** testear (no me dio los tests, solo las ideas):

```python
# Índices límite
def test_punto_valido_limites():
    tablero = Tablero()
    assert tablero.punto_valido(0)     # Mínimo
    assert tablero.punto_valido(23)    # Máximo
    assert not tablero.punto_valido(-1)
    assert not tablero.punto_valido(24)

# Listas vacías
def test_sacar_de_barra_vacia():
    tablero = Tablero()
    assert len(tablero.barra_x) == 0
    # No debe romper
    result = tablero.sacar_de_barra("X")
    assert result is None

# Perder más fichas de las que hay
def test_perder_ficha_hasta_cero():
    jugador = Jugador("Test", "X")
    for _ in range(20):  # Más de 15
        jugador.perder_ficha()
    # No debe ser negativo
    assert jugador.fichas_restantes() >= 0

# Usar todos los dados dobles
def test_usar_cuatro_dados_dobles():
    juego = BackgammonJuego()
    juego.dados_disponibles = [3, 3, 3, 3]
    
    # Usar los 4
    for i in range(4):
        juego.aplicar_movimiento(11, 14)
    
    assert len(juego.dados_disponibles) == 0

# Captura con múltiples fichas (no debería permitir)
def test_no_captura_punto_con_dos_fichas():
    juego = BackgammonJuego()
    juego.tablero.colocar_ficha(5, "O")
    juego.tablero.colocar_ficha(5, "O")  # 2 fichas
    juego.dados_disponibles = [5]
    
    # No debe permitir mover
    assert juego.es_movimiento_valido(0, 5) == False
```

**Después de entender qué casos testear:** Escribí todos estos tests yo mismo, usando las técnicas de mocking que aprendí.

### 4. Uso de Fixtures - Técnica explicada

**Me explicaron:** Cómo usar fixtures de pytest para evitar código duplicado

**Ejemplo de patrón:**

```python
import pytest

@pytest.fixture
def tablero_limpio():
    """Tablero vacío para tests."""
    t = Tablero()
    t.reset()
    return t

@pytest.fixture
def tablero_inicial():
    """Tablero con configuración inicial."""
    t = Tablero()
    t.reset()
    t.configurar_inicial()
    return t

@pytest.fixture
def juego_iniciado():
    """Juego listo para jugar."""
    j = BackgammonJuego()
    j.iniciar()
    return j

# Uso en tests
def test_mover_ficha(tablero_limpio):
    tablero_limpio.colocar_ficha(0, "X")
    tablero_limpio.mover_ficha(0, 3)
    assert tablero_limpio.fichas_en(3) == 1

def test_tirar_dados(juego_iniciado):
    valores = juego_iniciado.tirar_dados()
    assert juego_iniciado.dados_disponibles == valores
```

**Entendí los beneficios:**
- No repito código de setup
- Tests más cortos y claros
- Cambios en setup se hacen en un solo lugar

**Después:** Creé mis propias fixtures para tablero_limpio, juego_iniciado, etc.

### 5. Tests Parametrizados - Herramienta aprendida

**Me enseñaron:** Cómo usar `@pytest.mark.parametrize`

**Ejemplo del patrón:**

```python
@pytest.mark.parametrize("origen,destino,valido", [
    (0, 3, True),      # Válido
    (0, 25, False),    # Destino fuera de rango
    (-2, 5, False),    # Origen inválido
    (5, 5, False),     # Mismo punto
    (0, 10, False),    # Dado no disponible
])
def test_validacion_movimientos(juego_iniciado, origen, destino, valido):
    juego_iniciado.dados_disponibles = [3]
    resultado = juego_iniciado.es_movimiento_valido(origen, destino)
    assert resultado == valido
```

**Entendí la ventaja:** Un test, múltiples casos. Si uno falla, pytest me dice exactamente cuál.

**Después:** Usé esto extensivamente para testear validaciones con diferentes inputs.

### 6. Estrategia de Priorización - Consejo recibido

La IA me sugirió priorizar así:

1. **Tests unitarios de core/** (Prioridad ALTA)
   - Son la lógica crítica
   - Objetivo: >95% cobertura
   - Usar mocking para dados

2. **Tests de integración** (Prioridad MEDIA)
   - Flujo completo del juego
   - Objetivo: Cubrir casos de uso principales

3. **Tests de CLI** (Prioridad MEDIA)
   - Comandos y parsing
   - Objetivo: >85% cobertura

4. **Tests de UI** (Prioridad BAJA)
   - Difícil de automatizar
   - Objetivo: >70% cobertura
   - Complementar con testing manual

## Implementación Final

Después de aprender estas técnicas, escribí todos los tests necesarios para alcanzar 92% de cobertura.

## Resultado Final

```
core/board.py       95% ✅
core/game.py        92% ✅
core/player.py     100% ✅
core/dice.py       100% ✅
cli/cli.py          88% ✅
ui/pygame_ui.py     75% ⚠️
--------------------------
TOTAL               92% ✅
```

## Problemas Encontrados y Soluciones

### Problema 1: Tests inconsistentes
**Síntoma:** Tests pasaban individualmente, fallaban juntos.
**Causa:** No reseteaba el tablero entre tests.
**Solución:** Fixtures con reset automático.

### Problema 2: Pygame en CI
**Síntoma:** `pygame.error: No available video device`
**Causa:** CI sin display.
**Solución:** Mockear todo pygame.

### Problema 3: Cobertura estancada en 85%
**Síntoma:** No llegaba a 90%.
**Causa:** Faltaban tests de edge cases.
**Solución:** Testear límites, listas vacías, valores extremos.

## Comandos Útiles Aprendidos

```bash
# Ver cobertura detallada
pytest --cov=core --cov=cli --cov-report=term-missing

# Ejecutar solo tests rápidos (sin Pygame)
pytest -m "not slow"

# Ver qué líneas NO están cubiertas
pytest --cov=core --cov-report=html
# Abre htmlcov/index.html

# Ejecutar tests en paralelo (más rápido)
pytest -n auto
```

## Reflexión

Aprendizajes principales:

1. **Mocking:** Aprendí a usar `@patch` para controlar componentes externos
2. **Edge cases:** Útil saber qué casos testear
3. **Fixtures:** Entendí el patrón y lo apliqué
4. **Priorizar:** No todo necesita 100%
5. **CI:** Componentes gráficos requieren mocks

## Conclusión

Alcancé 92% de cobertura aplicando las técnicas. El proyecto cumple el requisito de >90%.