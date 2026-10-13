# Migración — GASE v0.1 → v0.2 Pilot

## Fuente

Repositorio GitHub entregado por el usuario.

## Estrategia

Compatibilidad hacia atrás.

### Preservado

- historial `history/`;
- especificación `spec/GASE-v0.1.md`;
- ejemplos existentes;
- entregables existentes;
- Issue Templates;
- estructura base;
- neutralidad tecnológica.

### Actualizado

- `CHANGELOG.md`
- `MANIFEST.md`
- `README.md`
- `ROADMAP.md`
- `START-HERE.md`
- `VERSION`
- `spec/CONTROL-PLANE.md`
- `spec/PROJECT-STRUCTURE.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/GASE_CONTROL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/prompts/CONTINUE_PROJECT.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/prompts/START_PROJECT.md`

### Añadido

- `research/METH-OBS-001-piloto-real.md`
- `research/RSR-001-agentic-runtime-patterns.md`
- `runtime/CONTEXT_COMPILER.md`
- `runtime/README.md`
- `runtime/ROUTER.md`
- `runtime/SESSION_HANDOFF.md`
- `runtime/SKILL_REGISTRY.md`
- `runtime/VERIFICATION.md`
- `runtime/gase.config.example.yaml`
- `skills/debug/SKILL.md`
- `skills/domain/SKILL.md`
- `skills/feature/SKILL.md`
- `skills/refactor/SKILL.md`
- `skills/security/SKILL.md`
- `skills/session/SKILL.md`
- `skills/sync/SKILL.md`
- `skills/verification/SKILL.md`
- `spec/GASE-v0.2-runtime.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/gase.config.yaml`
- `template/METODOLOGIA-DE-DESARROLLO-IA/prompts/00_GASE_RUNTIME_ROUTER.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/runtime/CONTEXT_COMPILER.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/runtime/README.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/runtime/ROUTER.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/runtime/SESSION_HANDOFF.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/runtime/SKILL_REGISTRY.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/runtime/VERIFICATION.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/debug/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/domain/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/feature/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/refactor/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/security/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/session/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/sync/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/skills/verification/SKILL.md`
- `template/METODOLOGIA-DE-DESARROLLO-IA/tools/gase_doctor.py`
- `tools/gase_doctor.py`

## Cambio conceptual

La v0.2 Pilot introduce una Experience/Runtime Layer.

No elimina el Governance Core.

## Migración de proyectos v0.1

Puede hacerse de forma aditiva:

1. copiar `runtime/`;
2. copiar `skills/`;
3. copiar `tools/gase_doctor.py`;
4. añadir `gase.config.yaml`;
5. ajustar el Control Plane para usar el Router.

No es necesario reescribir estados históricos.
