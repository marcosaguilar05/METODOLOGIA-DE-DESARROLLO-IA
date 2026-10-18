# Prompt 03 — Refactorización, Descomposición y Clean Code (GASE Runtime v0.2)

> **Uso:** Emplea este prompt cuando un módulo o archivo supere los límites de tamaño recomendados (>200 líneas), contenga acoplamiento excesivo o acumule deuda técnica.

```markdown
Actúa como un **Arquitecto de Software y Especialista en Clean Code** para el proyecto: `[NOMBRE_DEL_PROYECTO]`.

Necesito refactorizar y descomponer modularmente el siguiente archivo:
- **Archivo a refactorizar:** `[RUTA_DEL_ARCHIVO]`
- **Motivo de la refactorización:** [EJEMPLO: Excede 200 líneas / Acoplamiento excesivo / if-else complejos / Lógica duplicada]

---

### 🧩 Protocolo de Refactorización Limpia (Skill: `skills/refactor/SKILL.md`):

1. **Garantía Fundamental de Invarianza:**
   - La refactorización debe preservar el comportamiento observable externo sin romper compatibilidad existente.
   - Todo cambio debe validar las pruebas existentes antes y después del cambio (`runtime/VERIFICATION.md`).

2. **Reglas de Descomposición Modular:**
   - **Límites de Longitud:** Ningún archivo debe superar preferentemente **200 - 250 líneas de código**. Si es un punto de entrada o página, mantenerlo bajo **100 - 150 líneas**.
   - **Funciones Atómicas:** Funciones individuales concentradas en una única responsabilidad, con un máximo ideal de **30 - 40 líneas**.
   - **Erradicación de `if/else` y `switch` anidados:** Sustituir condicionales extensos por mapas de handlers, diccionarios de lookup o estrategias polimórficas tipadas.
   - **Separación de Capas:** Desacoplar la orquestación, el estado, la presentación visual y el acceso a datos en módulos independientes y reutilizables.
   - **Extracción de Constantes y Datos:** Trasladar mocks, estructuras estáticas y opciones de configuración fuera de los componentes activos a archivos dedicados.

3. **Comentarios y Tipado:**
   - Mantener comentarios técnicos descriptivos y docstrings rigurosamente en **estricto idioma español**.
   - Preservar tipado estricto sin recurrir a tipos dinámicos o evasivos.

Entrega la estrategia de partición modular, la justificación de diseño y el código refactorizado listo para su integración.
```
