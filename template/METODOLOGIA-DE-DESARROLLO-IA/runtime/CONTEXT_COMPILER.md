# Runtime Context Compiler

## Capas

### L0 — Core
- Control Plane
- políticas críticas
- tarea/cambio activo

### L1 — Work Type
Contexto necesario por feature, bug, refactor, seguridad, datos, etc.

### L2 — Domain
Solo el dominio o módulo afectado.

### L3 — Execution
Archivos/código/contratos necesarios para ejecutar.

### L4 — History
Cargar únicamente cuando sea necesaria trazabilidad o reconstrucción.

## Regla

`History != default context`.

El contexto debe ser suficiente, no máximo.
