# START HERE — Cómo usar GASE en un proyecto real

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

dentro de tu proyecto:

```text
gestion-inventario/
└── METODOLOGIA-DE-DESARROLLO-IA/
```

## 3. Abre `GASE_CONTROL.md`

Ese archivo es el **Control Plane**. La primera vez estará en modo `INITIALIZING`.

## 4. Habla con la IA usando `prompts/START_PROJECT.md`

No necesitas saber ingeniería formal. Describe el proyecto con lenguaje natural.

La IA debe ayudarte a transformar esa intención en:

- `PROJECT`
- `INTENT`
- `SCOPE`
- `UNKNOWNS`
- `RIGOR`
- primer `Engineering State`

sin inventar información.

## 5. Discovery

La IA resuelve contigo las incógnitas que realmente afectan las siguientes decisiones.

No se intenta diseñar todo de una vez.

## 6. Cuando aparezca una decisión

Se registra en:

```text
DECISIONS.md
```

o como ADR cuando sea arquitectónica:

```text
decisions/ADR-XXXX.md
```

## 7. Cuando cambie algo importante

Se crea:

```text
changes/CHG-XXXX.md
```

y se actualiza `GASE_CONTROL.md`.

## 8. Cuando una tarea esté lista

Se crea:

```text
tasks/TASK-XXXX.md
```

La tarea debe especificar al menos:

- intención;
- scope;
- contexto requerido;
- autoridad;
- criterio de aceptación;
- verificación.

## 9. La IA implementa

La IA trabaja sobre el código real del proyecto (`src/`, `tests/`, etc.), no dentro de la carpeta metodológica.

## 10. Evidencia

Los resultados relevantes quedan vinculados desde:

```text
evidence/
```

## 11. Nuevo estado

Cuando el cambio es aceptado:

```text
ES-0001 → ES-0002
```

y se actualiza:

```text
state/
GASE_CONTROL.md
```

## Regla de oro

**La persona expresa intención. La IA estructura y ejecuta. Las herramientas prueban. El estado del proyecto conserva lo que quedó decidido.**
