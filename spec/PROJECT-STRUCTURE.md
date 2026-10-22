# Estructura estándar de un proyecto GASE v0.2 Pilot

```text
mi-proyecto/
│
├── METODOLOGIA-DE-DESARROLLO-IA/
│   ├── GASE_CONTROL.yaml
│   ├── gase.config.yaml
│   ├── PROJECT.md
│   ├── INTENT.md
│   ├── SCOPE.md
│   ├── REQUIREMENTS.md
│   ├── RULES.yaml
│   ├── UNKNOWNS.yaml
│   ├── DECISIONS.md
│   ├── DATA.md
│   ├── ARCHITECTURE.md
│   ├── UX.md
│   │
│   ├── runtime/
│   │   ├── router.yaml
│   │   ├── context_compiler.yaml
│   │   ├── skill_registry.yaml
│   │   ├── SESSION_HANDOFF.md
│   │   └── VERIFICATION.md
│   │
│   ├── skills/
│   │   ├── session/
│   │   ├── feature/
│   │   ├── debug/
│   │   ├── refactor/
│   │   ├── security/
│   │   ├── domain/
│   │   ├── verification/
│   │   └── sync/
│   │
│   ├── tools/
│   │   └── gase_doctor.py
│   │
│   ├── changes/
│   ├── tasks/
│   ├── decisions/
│   ├── evidence/
│   ├── state/
│   ├── deliverables/
│   └── prompts/
│
├── src/
├── tests/
├── assets/
└── ...
```

## Separación

`METODOLOGIA-DE-DESARROLLO-IA/` contiene:

- gobernanza;
- conocimiento de ingeniería;
- runtime metodológico;
- contexto;
- evidencia;
- entregables.

El producto ejecutable vive fuera.

## Regla de versión

No crear carpetas `v0.2/`, `experimental/` o similares dentro de un proyecto.

La estructura física se mantiene estable.

La madurez de capacidades se expresa mediante metadata/configuración.

## Regla del Runtime

El Runtime no reemplaza archivos autoritativos.

Solo decide qué cargar y qué workflow aplicar.

## Portabilidad

Usar referencias relativas al repositorio cuando sea posible.

Evitar rutas `file:///C:/...` u otras rutas absolutas en artefactos persistentes.
