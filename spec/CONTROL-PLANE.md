# Especificación del GASE Control Plane

## Objetivo

`GASE_CONTROL.yaml` es el punto de entrada operativo para humanos y agentes.

Debe responder rápidamente:

- ¿Qué proyecto es?
- ¿Qué Engineering State está activo?
- ¿Qué fase está activa?
- ¿Qué cambio/tarea está activo?
- ¿Qué bloquea?
- ¿Qué archivos debe leer la IA?
- ¿Qué políticas son críticas?
- ¿Cuál es la siguiente acción?

## Propiedades

Debe ser:

- corto;
- actualizado;
- legible por humanos;
- parseable por máquinas;
- referencial;
- portable.

## No debe ser

- historial completo;
- copia de DECISIONS;
- copia de REQUIREMENTS;
- listado exhaustivo de evidencia;
- sustituto del Engineering State.

## Regla de entrada

```text
READ GASE_CONTROL.yaml
→ READ runtime/router.yaml
→ COMPILE CONTEXT
```

## Regla de contexto

El Control Plane puede indicar artefactos obligatorios.

El Runtime añade contexto según impacto y dominio.

## Regla de actualización

Después de un cambio material:

```text
CHANGE
→ VERIFY
→ UPDATE AUTHORITATIVE ARTIFACTS
→ TRANSITION (si aplica)
→ UPDATE GASE_CONTROL
```

No es obligatorio crear un nuevo Engineering State por cada microcambio.

## Chat

La conversación puede originar propuestas, pero no reemplaza la persistencia del proyecto.
