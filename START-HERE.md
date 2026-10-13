# START HERE — Cómo usar GASE v0.2 Pilot

## 1. Crea tu proyecto normal

Ejemplo:

```text
gestion-inventario/
```

## 2. Copia la carpeta metodológica

Copia:

```text
template/METODOLOGIA-DE-DESARROLLO-IA/
```

dentro del proyecto:

```text
gestion-inventario/
└── METODOLOGIA-DE-DESARROLLO-IA/
```

## 3. Abre `GASE_CONTROL.md`

Es el **Control Plane** y punto de entrada obligatorio.

La primera vez estará en `INITIALIZING`.

## 4. La IA entra por el Runtime

La IA debe seguir:

```text
GASE_CONTROL.md
→ runtime/ROUTER.md
→ runtime/CONTEXT_COMPILER.md
→ skills necesarias
```

No debe cargar todos los artefactos por defecto.

## 5. Inicia el proyecto

Puedes escribir en lenguaje natural o usar:

```text
prompts/START_PROJECT.md
```

La IA ayuda a producir:

- PROJECT
- INTENT
- SCOPE
- UNKNOWNS
- rigor inicial
- ES-0001

sin inventar información.

## 6. Discovery

Se resuelven únicamente las incógnitas necesarias para las siguientes decisiones.

No es obligatorio diseñar todo antes de implementar.

## 7. Clasificación operacional

El Runtime clasifica el trabajo:

### READ_ONLY
Consulta o análisis. No crea artefactos de cambio.

### DIRECT
Cambio pequeño, local, reversible y verificable. Puede ejecutarse sin crear una cadena completa de CHG + TASK + EVID + ES.

### GOVERNED
Afecta reglas, datos, contratos, arquitectura, seguridad, integraciones o múltiples superficies. Usa gobernanza GASE completa según rigor.

### CRITICAL
Alto impacto, irreversibilidad, seguridad, datos sensibles u otras políticas críticas. Requiere mayor contexto, autoridad y evidencia.

## 8. Decisiones

Las decisiones durables se registran en:

```text
DECISIONS.md
```

o mediante ADR cuando corresponda:

```text
decisions/ADR-XXXX.md
```

## 9. Cambios

Los cambios significativos se registran en `changes/`.

En R1/R2 se permite compresión física si se conservan las garantías del Kernel.

## 10. Implementación

La IA trabaja sobre el código real del proyecto (`src/`, `tests/`, etc.).

La carpeta metodológica gobierna y documenta; no contiene el runtime del producto.

## 11. Verificación

Antes de declarar finalización:

```text
runtime/VERIFICATION.md
```

La evidencia debe provenir preferentemente de mecanismos deterministas: tests, build, lint, typecheck, checks de contratos, etc.

## 12. Sincronización

Solo el conocimiento durable se promueve a la fuente de verdad:

- decisiones;
- reglas;
- arquitectura;
- datos;
- riesgos;
- requisitos;
- aprendizajes reutilizables;
- Engineering State.

No se debe crear ruido documental por cambios triviales.

## Regla de oro

**La persona expresa intención. La IA enruta, compila contexto, ejecuta y verifica. El proyecto conserva lo que quedó realmente decidido.**
