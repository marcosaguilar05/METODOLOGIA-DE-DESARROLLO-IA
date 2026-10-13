# RSR-001 — Patrones de runtime agentic aplicables a GASE

## Objetivo

Estudiar patrones de herramientas contemporáneas de desarrollo asistido por IA
sin convertir ninguna herramienta externa en dependencia obligatoria.

## Patrones retenidos

### Router de intención
El usuario habla en lenguaje natural; el sistema elige proceso.

### Skills bajo demanda
No cargar todas las instrucciones y especialidades en cada tarea.

### Contexto durable en el repositorio
El proyecto debe sobrevivir a un cambio de chat/modelo/agente.

### Trabajo proporcional
Cambios pequeños no deben activar automáticamente la ceremonia máxima.

### Verificación separada
La generación y la verificación son fases distintas.

### Handoff explícito
El siguiente agente debe saber trabajo activo, bloqueos y siguiente acción.

## Decisión metodológica

GASE adopta estos patrones como Experience Layer, pero conserva:

- Engineering State;
- Impact;
- Risk/Rigor;
- Authority;
- Evidence;
- Gates;
- Technology Neutrality.

## No adoptado como requisito

- memoria externa obligatoria;
- proveedor específico;
- agente específico;
- IDE específico;
- CLI obligatoria;
- stack específico.
