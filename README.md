# METODOLOGIA-DE-DESARROLLO-IA

Repositorio base de **GASE v0.2 Pilot** (*Governed Agentic Software Engineering*, nombre provisional).

GASE es una metodología de ingeniería de software asistida por IA cuyo núcleo es un **Engineering State** versionado, trazable y gobernado. La IA puede analizar, proponer y ejecutar; el proyecto conserva decisiones, contexto, autoridad, evidencia y transiciones de forma explícita.

La v0.2 Pilot **no reemplaza el Kernel de GASE v0.1**. Añade una capa de experiencia y runtime para reducir fricción operacional: router, compilación de contexto bajo demanda, skills, handoff y verificación proporcional.

## Qué contiene este repositorio

- `spec/` — especificación normativa de GASE.
- `runtime/` — referencia de la Experience/Runtime Layer.
- `history/` — evolución M-001 a M-014.
- `research/` — investigación y observaciones que justifican la evolución.
- `template/` — carpeta lista para copiar dentro de un proyecto real.
- `examples/` — ejemplos de uso.
- `.github/ISSUE_TEMPLATE/` — observaciones y propuestas metodológicas.

## Regla principal de uso

En un proyecto real:

```text
mi-proyecto/
├── METODOLOGIA-DE-DESARROLLO-IA/
│   ├── GASE_CONTROL.md
│   ├── gase.config.yaml
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
│   ├── runtime/
│   ├── skills/
│   ├── tools/
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

**El código, tests y assets del producto viven fuera de la carpeta metodológica.**

## Punto de entrada para la IA

Toda IA debe leer primero:

```text
METODOLOGIA-DE-DESARROLLO-IA/GASE_CONTROL.md
```

El Control Plane funciona como router hacia el estado y contexto vigente. No debe duplicar toda la historia del proyecto.

Cuando el Runtime está habilitado, el flujo recomendado es:

```text
GASE_CONTROL.md
  ↓
runtime/ROUTER.md
  ↓
runtime/CONTEXT_COMPILER.md
  ↓
skills necesarias
  ↓
prompt/proceso aplicable
  ↓
ejecución
  ↓
runtime/VERIFICATION.md
  ↓
sincronización del Engineering State cuando corresponda
```

## Principio de operación

**Trabajo pequeño permanece pequeño. Trabajo riesgoso activa más ingeniería.**

GASE conserva el Kernel aunque físicamente comprima artefactos en R1/R2.

## Fuente de verdad

- El chat es una interfaz de trabajo.
- El proyecto conserva la memoria.
- El Engineering State es la fuente autoritativa.
- Proposal ≠ Decision.
- Generated ≠ Verified.
- Los entregables DOCX/PDF son vistas generadas del conocimiento del proyecto.

Consulta `START-HERE.md` para comenzar.

## Compatibilidad

- `spec/GASE-v0.1.md` se conserva como baseline.
- La v0.2 Pilot añade `spec/GASE-v0.2-runtime.md`.
- Los proyectos v0.1 pueden adoptar el Runtime de forma aditiva.
- Ningún proveedor, modelo, memoria externa o stack es obligatorio.

## Documento DOCX

El entregable histórico de v0.1 sigue disponible en:

`deliverables/GASE-v0.1-Especificacion-y-Guia-de-Uso.docx`

Una versión documental v0.2 podrá generarse cuando la Pilot se estabilice.
