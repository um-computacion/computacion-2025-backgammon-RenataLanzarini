# PROMPT DESARROLLO - Diseño e Implementación del Proyecto Backgammon

**Fecha:** 30 de Octubre, 2025  
**Estudiante:** Renata Lanzarini  
**Materia:** Computación 2025

---

## Introducción

Este documento registra las consultas realizadas durante la fase de **desarrollo del proyecto**, desde decisiones de arquitectura hasta implementación de reglas complejas del juego.

---

## PARTE 1: Diseño Inicial y Arquitectura

### Contexto

Estoy arrancando con el proyecto y tengo algunas ideas sobre la arquitectura, pero hay varios puntos donde no estoy segura cuál es la mejor opción. Necesito feedback técnico antes de empezar a programar en serio.

### Prompt Utilizado

```
Estoy empezando un proyecto de Backgammon en Python y ya tengo algunas ideas, 
pero quiero validarlas contigo antes de empezar a programar. Los requisitos son:

1. Implementar el juego completo de Backgammon con todas sus reglas
2. Dos interfaces: CLI (línea de comandos) y GUI (Pygame)
3. Aplicar principios SOLID
4. Usar atributos privados con notación __atributo__
5. Testing con >90% de cobertura
6. Dockerización

Mis dudas:
- ¿Cómo debería estructurar las carpetas y módulos?
- ¿Qué clases necesito y cuál debería ser la responsabilidad de cada una?
- ¿Cómo separar la lógica de las interfaces para poder reutilizar código?
- ¿Qué estructura de datos debería usar para el tablero? Estoy pensando en 
  una lista de listas, pero no estoy segura si es la mejor opción.
- ¿Cómo manejo el caso especial de reingresar fichas desde la barra?

Mi idea inicial es tener:
- core/ para la lógica
- cli/ para la interfaz de consola
- ui/ para pygame

¿Es correcto este enfoque? ¿Qué me recomendás?
```

### Respuesta Recibida

Me dieron feedback sobre varios aspectos:

#### 1. Estructura de Carpetas

Confirmaron que mi idea inicial tenía sentido:

```
backgammon/
├── core/           # Lógica del juego
│   ├── game.py
│   ├── board.py
│   ├── player.py
│   └── dice.py
├── cli/           # Interfaz CLI
│   └── cli.py
├── ui/            # Interfaz Pygame
│   └── pygame_ui.py
├── tests/         # Tests
└── main.py        # Punto de entrada
```

**Validación recibida:** La separación en tres capas es correcta y sigue buenos principios de diseño.

#### 2. Clases - Feedback recibido

**BackgammonJuego (game.py)**
- Mi idea: Coordinar el flujo del juego
- Feedback: Mantener el estado centralizado aquí
- Implementé como coordinador central

**Tablero (board.py)** - Duda sobre estructura de datos
- Estaba pensando en: `_puntos = [[] for _ in range(24)]`
- Me compararon con dict, tuplas, y NumPy
- Ventajas de lista de listas: natural, simple, no necesita dependencias
- Mantuve mi elección

**Jugador (player.py)** - ¿Es necesaria?
- Mi duda: Quizás es muy simple, solo un dict
- Argumentos a favor: extensibilidad, type hints, encapsulación
- Decidí mantenerla

**Dados (dice.py)** - ¿Clase o función?
- Mi duda inicial: Parece muy simple para una clase
- Argumentos a favor de clase: facilita testing con mocks, guardar estado
- Implementé como clase

#### 3. Separación de Lógica

Confirmaron mi intuición sobre dependencias:
- core/ NO debe importar de cli/ ni ui/ ✓ (ya lo tenía pensado)
- cli/ y ui/ SÍ importan de core/ ✓ (era mi plan)

**Beneficio:** Puedo reutilizar la misma lógica en diferentes interfaces.

#### 4. Reingreso desde Barra

Tenía tres opciones y necesitaba evaluarlas:

**Opción 1:** Método separado `reingresar_ficha(destino)`  
**Opción 2:** Flag booleano `mover(origen, destino, desde_barra=True)`  
**Opción 3:** Valor especial `origen = -1`

Me ayudaron a ver pros y contras. Elegí la opción 3 porque es más simple y -1 claramente está fuera del rango válido.

### Implementación Final

1. ✅ Adopté la estructura de carpetas (core/cli/ui)
2. ✅ Implementé las 4 clases principales en core/
3. ✅ Usé lista de listas para el tablero
4. ✅ Implementé origen=-1 para reingreso
5. ✅ Separé completamente core/ de las interfaces

### Reflexión - Parte 1

Esta consulta me sirvió para:
- Confirmar que mi arquitectura en capas era el camino correcto
- Decidirme por lista de listas después de ver la comparación
- Resolver la duda sobre el reingreso (opción 3 ganó)
- Entender mejor cómo aplicar Dependency Inversion

El feedback sobre las alternativas fue útil para tomar decisiones más informadas.

---

## PARTE 2: Implementación de Reglas y Validación

### Contexto

Arquitectura lista, ahora toca implementar las validaciones de movimientos. El método `es_movimiento_valido()` se me está haciendo muy largo y difícil de leer. Tengo las reglas pero no estoy segura del orden ni de cómo organizarlas.

### Prompt Utilizado

```
Tengo la estructura básica del proyecto Backgammon funcionando, pero necesito 
ayuda con la implementación de las reglas de validación de movimientos.

Mi código actual de es_movimiento_valido() está así:

def es_movimiento_valido(self, origen, destino):
    # Validaciones básicas
    if not self.tablero.punto_valido(destino):
        return False
    # ... más validaciones
    return True

Pero me faltan varias reglas importantes:

1. Si un jugador tiene fichas en la barra, DEBE reingresar antes de poder 
   mover otras fichas
2. No puede mover a un punto bloqueado por el oponente (2+ fichas)
3. Si el destino tiene 1 ficha enemiga, debe capturarla
4. La distancia debe coincidir con uno de los dados disponibles
5. Para reingreso (origen=-1), el cálculo de distancia es diferente

Mis preguntas:
- ¿En qué orden debería hacer estas validaciones? 
- ¿Cómo manejo el caso de fichas en barra? ¿Debería ser la primera validación?
- ¿Cómo implemento la captura de fichas?
- ¿Debería tener un método separado para cada tipo de validación o todo en uno?

Actualmente mi método tiene como 30 líneas y se está volviendo difícil de leer.
```

### Respuesta Recibida

Me dieron sugerencias sobre organización:

#### 1. Orden de Validaciones

Sugerencia: Poner las más restrictivas primero

1. **Primero:** Fichas en barra (más restrictivo)
2. **Segundo:** Índices válidos (previene errores)
3. **Tercero:** Dado disponible (regla del juego)
4. **Cuarto:** Destino no bloqueado (regla del juego)

**Razón:** Si falla una restrictiva, no hay que validar el resto.

Implementé siguiendo este orden y el código quedó mucho más claro.

#### 2. Ejemplo de Estructura

Me mostraron cómo estructurarlo:

```python
def es_movimiento_valido(self, origen, destino):
    ficha_jugador = "X" if self.turno == 1 else "O"
    
    # 1. PRIMERO: Validar restricción de barra
    tiene_en_barra = self.tablero.tiene_fichas_en_barra(ficha_jugador)
    if tiene_en_barra and origen != -1:
        return False  # DEBE reingresar
    
    # 2. Validar índices
    if not self.tablero.punto_valido(destino):
        return False
    
    # 3. Validar dado disponible
    distancia = abs(destino - origen) if origen != -1 else destino + 1
    if distancia not in self.dados_disponibles:
        return False
    
    # 4. Validar destino no bloqueado
    if self._esta_bloqueado(destino, ficha_jugador):
        return False
    
    return True
```

Lo implementé adaptándolo a mi código.

#### 3. ¿Dividir en Métodos?

Me explicaron el trade-off:

**Opción A: Todo en un método**
- Pro: Ver todo el flujo de una vez
- Contra: Método largo (~60 líneas)

**Opción B: Métodos separados**
- Pro: Métodos cortos
- Contra: Saltar entre métodos

Recomendación: <100 líneas está bien en un método.

Decidí mantenerlo todo junto (son 60 líneas).

#### 4. Captura de Fichas

Me dieron un patrón:

```python
def aplicar_movimiento(self, origen, destino):
    if not self.es_movimiento_valido(origen, destino):
        return False
    
    # Verificar si hay captura
    if self.tablero.fichas_en(destino) == 1:
        color_destino = self.tablero.ficha_en(destino)
        if color_destino != ficha_jugador:
            self.tablero.capturar_ficha(destino)
    
    # Mover y consumir dado
    # ...
    return True
```

Lo implementé en `aplicar_movimiento()`.

### Implementación Final

1. ✅ Reorganicé validaciones por orden restrictivo
2. ✅ Validación de barra va primero
3. ✅ Mantuve todo en un método
4. ✅ Implementé captura en aplicar_movimiento()
5. ✅ Usé early returns

### Reflexión - Parte 2

Consultar sobre organización me ayudó a estructurar mejor el código. El orden de validaciones hace mucha diferencia en legibilidad.

---

## Conclusión - Fase de Desarrollo

### Aprendizajes

1. **Arquitectura primero:** Pensar el diseño ahorra tiempo después
2. **Comparar alternativas:** Importante ver pros y contras antes de decidir
3. **Organización del código:** El orden importa para legibilidad
4. **Separación clara:** core/ independiente facilita todo

### Resultado

Proyecto con arquitectura sólida y código organizado. Listo para la fase de testing.

---

**Siguiente fase:** Ver PROMPT_TESTING.md