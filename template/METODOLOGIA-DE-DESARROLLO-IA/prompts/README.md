# Catálogo de Plantillas de Prompts — GASE v0.2 Pilot

Este directorio reúne las plantillas estandarizadas de prompts estructurados para interactuar con modelos y asistentes de IA (Gemini, Claude, GPT, DeepSeek, Antigravity, Cursor, etc.) siguiendo rigurosamente los principios de **GASE v0.2 Pilot (Governed Agentic Software Engineering)**.

La filosofía de GASE v0.2 separa la **intención humana** de la **ejecución operativa**:
> **«La persona expresa intención. La IA enruta, compila contexto, ejecuta y verifica. El repositorio conserva lo que quedó realmente decidido.»**

---

## 🧭 Mapa de Prompts y Mapeo con el Runtime GASE

| # | Archivo | Caso de Uso / Necesidad | Skill Asociada | Clasificación Típica | Rol de la IA |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **00** | [00_GASE_RUNTIME_ROUTER.md](00_GASE_RUNTIME_ROUTER.md) | Enrutador maestro operativo para cualquier petición inicial. | `runtime/router.yaml` | *Cualquiera* | Runtime Router GASE |
| **01** | [01_CONTINUAR_SESION.md](01_CONTINUAR_SESION.md) | Retomar o iniciar sesión de trabajo cargando el contexto mínimo. | `skills/session` | `READ_ONLY` / `DIRECT` | Tech Lead Full-Stack |
| **02** | [02_NUEVA_FUNCIONALIDAD.md](02_NUEVA_FUNCIONALIDAD.md) | Construir una característica, módulo o flujo de punta a punta. | `skills/feature` | `DIRECT` / `GOVERNED` | Senior Software Engineer |
| **03** | [03_REFACTORIZACION_Y_CLEAN_CODE.md](03_REFACTORIZACION_Y_CLEAN_CODE.md) | Modularizar archivos extensos (>200 líneas) y reducir deuda técnica. | `skills/refactor` | `DIRECT` / `GOVERNED` | Software Architect & Clean Coder |
| **04** | [04_DOMINIO_DATOS_Y_CONTRATOS.md](04_DOMINIO_DATOS_Y_CONTRATOS.md) | Modelar entidades, contratos API (OpenAPI), DTOs y persistencia. | `skills/domain` | `GOVERNED` / `CRITICAL` | Domain & Data Architect |
| **05** | [05_DISENO_UI_UX_ENTERPRISE.md](05_DISENO_UI_UX_ENTERPRISE.md) | Diseñar pantallas Mobile-First, componentes táctiles y UX Enterprise. | `UX.md` | `DIRECT` / `GOVERNED` | Senior UI/UX & Design Systems |
| **06** | [06_ACTUALIZAR_CEREBRO_GASE.md](06_ACTUALIZAR_CEREBRO_GASE.md) | Sincronizar el conocimiento durable del proyecto (`DEC`, `state/`, `GASE_CONTROL`). | `skills/sync` | `GOVERNED` | Metodólogo Custodio del Cerebro |
| **07** | [07_DEBUGEAR_Y_CORREGIR_ERRORES.md](07_DEBUGEAR_Y_CORREGIR_ERRORES.md) | Diagnosticar fallos de raíz, asegurar no regresión y tests. | `skills/debug` | `DIRECT` / `GOVERNED` | Debugging & QA Specialist |
| — | [START_PROJECT.md](START_PROJECT.md) | Inicializar un nuevo proyecto desde cero (PROJECT, INTENT, SCOPE). | `runtime/router.yaml` | `GOVERNED` | Metodólogo GASE |
| — | [CONTINUE_PROJECT.md](CONTINUE_PROJECT.md) | Continuación minimalista orientada a CLI y ejecución rápida. | `skills/session` | `DIRECT` | Asistente de Proyecto |
| — | [REQUEST_CHANGE.md](REQUEST_CHANGE.md) | Registro formal de solicitud de cambio mayor o crítico. | `runtime/router.yaml` | `GOVERNED` / `CRITICAL` | Asistente de Gobernanza |

---

## ⚡ Cómo Usar Estas Plantillas

1. **Selecciona la plantilla** correspondiente al trabajo que vas a realizar.
2. **Copia el bloque Markdown** del prompt.
3. **Rellena las variables** entre corchetes (ej. `[NOMBRE_DEL_PROYECTO]`, `[DESCRIPCIÓN]`).
4. **Pégalo en el chat de tu IA o entorno IDE** (Gemini, Claude, Cursor, Antigravity, etc.).
5. La IA leerá automáticamente `GASE_CONTROL.yaml`, activará el Runtime Router y compilará únicamente el contexto necesario sin sobrecargar la ventana de contexto.

---

## 🧠 El Rol de `06_ACTUALIZAR_CEREBRO_GASE.md`

En la metodología GASE, **el repositorio es el cerebro y la memoria durable del sistema**. 

Al finalizar una tarea o hito importante, el prompt `06_ACTUALIZAR_CEREBRO_GASE.md`:
1. Clasifica si el trabajo fue `DIRECT` (evidencia compacta sin burocracia) o `GOVERNED` (trazabilidad formal completa).
2. Promueve decisiones técnicas a `DECISIONS.md`.
3. Crea el nuevo snapshot de estado de ingeniería `state/ES-XXXX.md`.
4. Actualiza el puntero del tablero central `GASE_CONTROL.yaml`.
5. Descarta el ruido volátil de las conversaciones y preserva la verdad arquitectónica verificada.
