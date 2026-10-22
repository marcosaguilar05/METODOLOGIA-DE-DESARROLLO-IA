# CHANGELOG

## 0.2.1-pilot (YAML Hybrid Runtime)

Evolución de eficiencia para agentes y reducción de huella de contexto.

### Añadido

- Soporte nativo para estado y runtime en YAML puro:
  - `GASE_CONTROL.yaml` (Control Plane ultra-ligero y tipado).
  - `RULES.yaml` (Invariantes de negocio con IDs y severidad explícita).
  - `UNKNOWNS.yaml` (Matriz de incógnitas y bloqueos).
  - `runtime/router.yaml` (Clasificación operativa y reglas).
  - `runtime/skill_registry.yaml` (Registro estructurado de skills).
  - `runtime/context_compiler.yaml` (Matriz declarativa L0-L4).
- Validación de sintaxis YAML en `gase_doctor.py`.
- Detección flexible de directorio en `gase_doctor.py` para auditar tanto el template como proyectos en producción.

---

## 0.2.0-pilot

Primera evolución basada en uso real.

### Añadido

- GASE Runtime / Experience Layer.
- Router de intención.
- Context Compiler operativo bajo demanda.
- Skill Registry.
- Skills para sesión, feature, debug, refactor, seguridad, dominio, verificación y sincronización.
- Protocolo de handoff.
- Verification Runtime.
- `gase.config.yaml`.
- `gase_doctor.py` como validador de solo lectura.
- soporte explícito para trabajo `READ_ONLY`, `DIRECT`, `GOVERNED` y `CRITICAL`.
- compresión física permitida en R1/R2 sin eliminar garantías.
- investigación y observaciones del piloto real.

### Conservado

- Kernel GASE v0.1.
- Engineering State.
- Impact, Risk, Rigor y Authority.
- Context Compiler conceptual.
- Evidence Engine y Gates.
- neutralidad tecnológica.
- estructura autocontenida por proyecto.

### Objetivo

Reducir burocracia visible y carga de contexto sin reducir trazabilidad, evidencia ni gobernanza.

---

## 0.1.0-baseline

Primera baseline consolidada.

Incluye:

- Engineering State
- Engineering Knowledge Graph
- rigor adaptativo
- impacto
- autoridad
- Context Compiler
- Evidence Engine
- transiciones verificables
- protocolo humano–IA
- selección tecnológica por proyecto
- adopción Greenfield/Brownfield
- Control Plane Markdown
- estructura de proyecto autocontenida

La versión 0.1 se conserva como baseline histórica.
