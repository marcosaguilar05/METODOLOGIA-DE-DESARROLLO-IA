# GASE v0.1 — Especificación consolidada

## 1. Definición

GASE es una metodología de ingeniería de software asistida por IA orientada a coordinar personas, agentes y herramientas mediante la evolución gobernada de un **Engineering State** versionado y trazable.

## 2. Modelo central

```text
INTENT
  ↓
ENGINEERING STATE
  ↓
TASK
  ↓
IMPACT
  ↓
RISK / RIGOR
  ↓
CONTEXT
  ↓
AUTHORITY
  ↓
EXECUTION
  ↓
EVIDENCE
  ↓
GATE
  ↓
TRANSITION
```

## 3. Kernel

GASE conserva siempre:

1. Intent
2. Engineering State
3. Identity
4. Traceability
5. Impact
6. Risk
7. Rigor
8. Context
9. Authority
10. Execution Contract
11. Verification
12. Evidence
13. Gates
14. Versioning
15. Change Governance

Los elementos pueden comprimirse físicamente, pero no desaparecer conceptualmente.

## 4. Engineering State

El Engineering State representa el conocimiento autoritativo vigente del proyecto.

```text
ESₙ = (Artifacts, Relations, Policies, Evidence, Governance)
```

Una modificación significativa propone:

```text
ESₙ → Candidate → Verify → ESₙ₊₁
```

## 5. Fuente de verdad

- Chat ≠ Project Truth
- Proposal ≠ Decision
- Generated ≠ Verified
- Capability ≠ Authority

La memoria durable del proyecto vive en sus artefactos y estados.

## 6. Rigor

- R1 — Essential
- R2 — Controlled
- R3 — Governed
- R4 — Critical

```text
EffectiveRigor(T) =
MAX(ProjectRigor, ChangeRigor(T), PolicyMinimum)
```

## 7. Impacto

Todo cambio significativo analiza impacto directo, transitivo y semántico.

Propagaciones:

- NONE
- INFORM
- REVIEW
- REVALIDATE
- INVALIDATE
- BLOCK

## 8. Autoridad

IA:

- A0 Observe
- A1 Suggest
- A2 Prepare
- A3 Execute Constrained
- A4 Execute + Verify
- A5 Governed Autonomous Transition

Humano:

- H0 Inform
- H1 Review
- H2 Approve
- H3 Decide
- H4 Dual Control
- H5 Independent Authority

Execution Authority no implica Transition Authority.

## 9. Context Compiler

El contexto requerido se deriva de obligaciones de ingeniería, no solo de similitud semántica.

```text
CP(T) = Compile(ES, Task, Impact, Governance)
```

El contexto obligatorio no puede descartarse silenciosamente por límites de tokens.

## 10. Evidencia

Una tarea no se considera terminada porque exista código.

Debe existir un Verification Contract y evidencia suficiente.

Preferencia:

> Deterministic before probabilistic.

## 11. Transición

Una transición válida requiere:

- intención válida;
- contexto válido;
- autoridad;
- scope;
- políticas;
- evidencia;
- integridad del estado.

## 12. Tecnología

GASE no posee stack fijo.

```text
NEED
→ CAPABILITY PROFILE
→ CANDIDATES
→ FIT
→ EVIDENCE
→ AUTHORITY
→ ADR
→ PROJECT TECHNOLOGY
```

## 13. Adopción

Proyecto nuevo:

```text
PROJECT
→ INTENT
→ RIGOR
→ ES-0001
→ DISCOVERY
→ REQUIREMENTS
→ DESIGN
→ READY TASK
→ EXECUTE
```

Proyecto existente:

reconstruye progresivamente un Observed Engineering State.

## 14. Control Plane

Cada proyecto GASE debe disponer de un punto de entrada operativo:

```text
METODOLOGIA-DE-DESARROLLO-IA/GASE_CONTROL.md
```

El Control Plane no reemplaza todos los artefactos: indexa y orienta.

## 15. Entregables

Los entregables son vistas del mismo conocimiento:

```text
Engineering State
├── AI Context
├── Code
├── Tests
├── DOCX
├── PDF
└── Reports
```

## 16. Principios superiores

- Reducir burocracia, no garantías.
- Automatizar la ingeniería repetitiva, no eliminarla.
- Más autonomía no implica menos gobernanza.
- La IA razona; los mecanismos deterministas prueban lo comprobable.
- La tecnología sigue al proyecto.
- El proyecto debe poder continuar sin depender del historial de una conversación.

## 17. Baseline

GASE v0.1 es una hipótesis metodológica congelada para validación.

Los problemas reales se registran como `METH-OBS-*`.
Los cambios propuestos se registran como `METH-PROP-*`.
