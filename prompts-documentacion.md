# PROMPT DOCUMENTACIÓN - Estructuración de la Justificación Técnica

**Fecha:** 31 de Octubre, 2025  
**Estudiante:** Renata Lanzarini  
**Materia:** Computación 2025

---

## Introducción

Este documento registra cómo estructuré la documentación técnica del proyecto (JUSTIFICACION.md).

---

## Contexto

Proyecto completo funcionando. Ahora toca escribir la JUSTIFICACION.md explicando decisiones técnicas. Tengo claro qué decidí, pero no cómo estructurar el documento para que sea claro.

## Prompt Utilizado

```
Necesito estructurar la documentación técnica de mi proyecto Backgammon. 
Tengo que escribir una JUSTIFICACION.md que explique todas mis decisiones 
de diseño, pero no estoy segura de cómo organizarla.

El documento debe cubrir:
- Arquitectura general (por qué elegí capas)
- Diseño de cada clase (por qué existe, qué alternativas consideré)
- Decisiones de implementación (estructuras de datos, algoritmos)
- Aplicación de principios SOLID
- Estrategia de testing

Mi problema es que tengo MUCHA información y no sé:
1. ¿En qué orden debería presentar todo?
2. ¿Cuánto detalle poner en cada sección?
3. ¿Cómo explicar las decisiones sin que sea una lista aburrida?
4. ¿Debería justificar TODAS las decisiones o solo las importantes?

Mi idea inicial es:
- Sección 1: Arquitectura
- Sección 2: Clases
- Sección 3: SOLID
- Sección 4: Testing

¿Tiene sentido este orden? ¿Falta algo importante?
```

## Respuesta Recibida (Resumen)

La IA me ayudó a **estructurar** la documentación:

### 1. Estructura Sugerida

La IA me recomendó esta organización:

```
1. Introducción (contexto del proyecto)
2. Arquitectura General (decisión macro)
   └─ Por qué capas, alternativas, beneficios
3. Diseño de Clases (decisiones micro)
   └─ Para cada clase: responsabilidad, alternativas, decisión
4. Decisiones de Implementación (detalles técnicos)
   └─ Estructuras de datos, algoritmos específicos
5. Manejo de Errores
6. Testing
7. SOLID (aplicación de principios)
8. Problemas y Soluciones
9. Conclusiones
```

**Razón del orden:** De lo general a lo específico. Primero arquitectura (big picture), luego clases (componentes), después detalles (implementación).

**Mi decisión:** Adopté esta estructura porque tiene sentido pedagógico.

### 2. Nivel de Detalle - Guía recibida

La IA me sugirió para cada decisión:

**Template recomendado:**
```
Decisión: [Qué elegí]
Alternativas evaluadas: [Qué otras opciones consideré]
Por qué la elegí: [Ventajas]
Trade-offs: [Desventajas que acepté]
```

**Ejemplo que me dio:**

```
### Estructura de Datos del Tablero

**Decisión:** Usar lista de listas `[[] for _ in range(24)]`

**Alternativas evaluadas:**
- Dict de listas
- Lista de tuplas (cantidad, color)
- NumPy array

**Por qué la elegí:**
- Simple y pythonic
- Acceso O(1) por índice
- No requiere dependencias externas

**Trade-offs:**
- Usa más memoria que alternativas compactas
- No previene errores de tipo
```

**Mi implementación:** Usé este patrón en todas las secciones del documento.

### 3. Qué Justificar - Priorización sugerida

La IA me ayudó a priorizar qué decisiones documentar en detalle:

**Prioridad ALTA (justificar extensamente):**
- Decisiones arquitecturales (capas, separación)
- Estructuras de datos principales (tablero, dados disponibles)
- Decisiones que afectan múltiples componentes
- Casos donde rechacé alternativas populares

**Prioridad MEDIA (justificar brevemente):**
- Métodos auxiliares
- Validaciones específicas
- Nombres de variables

**Prioridad BAJA (solo mencionar):**
- Detalles de implementación obvios
- Convenciones estándar de Python

**Mi decisión:** Enfoqué el documento en decisiones de prioridad ALTA y MEDIA.

### 4. Cómo Explicar - Técnicas sugeridas

La IA me sugirió técnicas para hacer el documento más claro:

**Técnica 1: Comparación con tablas**
```
| Opción | Ventaja | Desventaja | Decisión |
|--------|---------|------------|----------|
```

**Técnica 2: Ejemplos de código**
```python
# ✅ BIEN
codigo_elegido()

# ❌ MAL - por qué no
codigo_rechazado()
```

**Técnica 3: Diagramas ASCII**
```
┌─────────┐
│ core/   │ ← Lógica
└────┬────┘
     ↓
┌─────────┐
│ cli/ui/ │ ← Presentación
└─────────┘
```

**Mi implementación:** Usé las tres técnicas en diferentes secciones.

### 5. Sección SOLID - Recomendación específica

La IA me recomendó para SOLID:

**No hacer:** Lista genérica de qué es cada principio
**Hacer:** Ejemplos concretos de MI proyecto

```
❌ MAL:
"SRP dice que cada clase debe tener una responsabilidad..."

✅ BIEN:
"Apliqué SRP separando Tablero (datos) de BackgammonJuego (reglas).
Alternativa rechazada: Poner validación en Tablero (violaría SRP porque...)"
```

**Mi implementación:** Cada principio SOLID tiene ejemplos de mi código, con casos donde lo apliqué y casos donde evité violarlo.

## Decisiones Tomadas (por mí)

Después del feedback sobre estructura:

1. ✅ Adopté el orden sugerido (general → específico)
2. ✅ Usé el template de alternativas para cada decisión
3. ✅ Prioricé decisiones arquitecturales
4. ✅ Agregué tablas comparativas
5. ✅ Incluí ejemplos de código con ✅/❌
6. ✅ Escribí SOLID con ejemplos concretos de mi proyecto
7. ✅ Agregué sección de "Problemas Encontrados"

**Importante:** La IA me ayudó con la **estructura y organización**, pero todo el contenido técnico (decisiones, análisis, trade-offs) lo escribí yo basándome en mi experiencia desarrollando el proyecto.

## Contenido del Documento Final

### Secciones Implementadas

**1. Arquitectura General (4 páginas)**
- Por qué arquitectura en capas
- Alternativas evaluadas (MVC, todo en uno)
- Regla de dependencia (DIP)
- Beneficios obtenidos

**2. Diseño de Clases (8 páginas)**

Para cada clase:
- `BackgammonJuego`: Coordinador central
- `Tablero`: Estructura de datos (comparé 4 opciones)
- `Jugador`: ¿Es necesaria? (debate extenso)
- `Dados`: ¿Clase o función? (justificado por testing)

Cada clase incluye:
- Responsabilidad
- Alternativas
- Decisión y razones
- Trade-offs

**3. Decisiones de Implementación (6 páginas)**
- Gestión de dados disponibles (lista vs set vs contador)
- Reingreso desde barra (origen=-1)
- Configuración inicial del tablero

**4. Manejo de Errores (2 páginas)**
- Excepciones vs booleanos
- Validación por capas

**5. Estrategia de Testing (4 páginas)**
- Tipos de tests (unitarios, mocking, parametrizados)
- Edge cases
- Cobertura por módulo
- Problemas con Pygame en CI

**6. Principios SOLID (5 páginas)**
- SRP: Ejemplos concretos de separación
- OCP: Agregar Pygame sin modificar core
- LSP: Diseño sin herencia
- ISP: Interfaces usan solo lo necesario
- DIP: Dirección de dependencias

**7. Problemas y Soluciones (2 páginas)**
- 6 problemas encontrados durante desarrollo
- Cómo los resolví

**8. Conclusiones (1 página)**
- Aprendizajes
- Rol de la IA
- Resultado final

### Métricas del Documento Final

- **Extensión:** 1048 líneas / ~30 páginas
- **Código de ejemplo:** 25+ snippets
- **Tablas comparativas:** 8 tablas
- **Diagramas:** 3 diagramas ASCII
- **Decisiones justificadas:** 15+ decisiones mayores

## Reflexión sobre Documentación

### Qué funcionó bien

**1. Estructura general → específico**
- El lector entiende primero el big picture
- Los detalles tienen contexto

**2. Template de alternativas**
- Cada decisión muestra que consideré opciones
- Queda claro POR QUÉ elegí algo

**3. Ejemplos de código**
- ✅/❌ hace muy visual qué es correcto/incorrecto
- Más claro que solo texto

**4. Sección de problemas**
- Muestra honestidad sobre dificultades
- Documenta aprendizajes

### Rol de la IA

La IA me ayudó con:

✅ **Estructura general** del documento  
✅ **Template** para justificar decisiones  
✅ **Priorización** de qué documentar  
✅ **Técnicas** de presentación (tablas, código)  

❌ **NO escribió** el contenido técnico  
❌ **NO explicó** mis decisiones  
❌ **NO analizó** trade-offs del proyecto  

### Aprendizajes

1. **Documentar ayuda a pensar:** Explicar decisiones me hizo reflexionar más sobre ellas
2. **Las alternativas importan:** No solo qué elegí, sino qué rechacé
3. **El contexto es clave:** Cada decisión necesita su "por qué"
4. **La estructura ayuda:** Documento bien organizado es más fácil de seguir

## Conclusión

Documento de justificación completo que explica decisiones, muestra alternativas, justifica elecciones, y analiza trade-offs.

---

**Archivos relacionados:**
- [JUSTIFICACION.md](./JUSTIFICACION.md) - Documento final (1048 líneas)
- [PROMPT_DESARROLLO.md](./PROMPT_DESARROLLO.md) - Fase de desarrollo
- [PROMPT_TESTING.md](./PROMPT_TESTING.md) - Fase de testing