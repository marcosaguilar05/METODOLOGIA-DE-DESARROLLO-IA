# Especificación del GASE Control Plane

## Objetivo

`GASE_CONTROL.md` es el punto de entrada operativo para humanos y agentes.

Debe responder rápidamente:

- ¿Qué proyecto es?
- ¿Qué Engineering State está activo?
- ¿Qué fase está activa?
- ¿Qué decisiones están vigentes?
- ¿Qué incógnitas siguen abiertas?
- ¿Qué tarea está activa?
- ¿Qué debe leer la IA?
- ¿Qué no debe asumir?
- ¿Cuál es la siguiente acción?

## Propiedades

El Control Plane debe ser:

- corto;
- actualizado;
- legible por humanos;
- parseable por máquinas;
- referencial, no duplicador de todo el conocimiento.

## Regla de entrada

Antes de realizar trabajo significativo:

```text
READ GASE_CONTROL.md
```

## Regla de actualización

Después de un cambio significativo:

```text
CHG
→ artifacts affected
→ Engineering State
→ GASE_CONTROL.md
```

## Chat

La conversación puede originar propuestas, pero no reemplaza la persistencia del proyecto.
