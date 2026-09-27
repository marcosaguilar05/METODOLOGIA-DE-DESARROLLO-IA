# METODOLOGIA-DE-DESARROLLO-IA

Repositorio base de **GASE v0.1** (*Governed Agentic Software Engineering*, nombre provisional).

GASE es una metodología de ingeniería de software asistida por IA cuyo núcleo es un **Engineering State** versionado, trazable y gobernado. La IA puede analizar, proponer y ejecutar; las decisiones, el contexto, la autoridad, la evidencia y las transiciones se mantienen explícitas.

## Qué contiene este repositorio

- `spec/` — especificación normativa de GASE v0.1.
- `history/` — evolución M-001 a M-014.
- `template/` — carpeta que se copia dentro de un proyecto real.
- `examples/` — ejemplos de uso.
- `.github/ISSUE_TEMPLATE/` — plantillas para observaciones y propuestas de la metodología.

## Regla principal de uso

En un proyecto real, la estructura queda así:

```text
mi-proyecto/
├── METODOLOGIA-DE-DESARROLLO-IA/
│   ├── GASE_CONTROL.md
│   ├── PROJECT.md
│   ├── INTENT.md
│   ├── SCOPE.md
│   ├── REQUIREMENTS.md
│   ├── RULES.md
│   ├── UNKNOWNS.md
│   ├── DECISIONS.md
│   ├── DATA.md
│   ├── ARCHITECTURE.md
│   ├── UX.md
│   ├── changes/
│   ├── tasks/
│   ├── decisions/
│   ├── evidence/
│   ├── state/
│   ├── deliverables/
│   └── prompts/
├── src/
├── tests/
├── assets/
└── ...
```

**El código y los tests del producto están fuera de la carpeta metodológica.**

## Punto de entrada para la IA

Toda IA debe leer primero:

```text
METODOLOGIA-DE-DESARROLLO-IA/GASE_CONTROL.md
```

Ese archivo funciona como **Control Plane** del proyecto: estado actual, decisiones activas, incógnitas, tarea actual, archivos a leer, restricciones y siguiente acción.

## Fuente de verdad

- El chat es una interfaz de trabajo.
- El proyecto conserva la memoria.
- El Engineering State es la fuente autoritativa.
- Los entregables DOCX/PDF se consideran vistas generadas del conocimiento del proyecto.

Consulta `START-HERE.md` para empezar.


## Documento DOCX

La especificación consolidada y guía práctica también está disponible como:

`deliverables/GASE-v0.1-Especificacion-y-Guia-de-Uso.docx`
