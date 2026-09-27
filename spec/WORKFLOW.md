# Workflow operativo

## Task lifecycle

```text
DRAFT
→ ANALYZING
→ READY
→ AUTHORIZED
→ IN_PROGRESS
→ VERIFYING
→ DONE
```

Estados auxiliares:

- BLOCKED
- SUSPENDED
- AWAITING_DECISION
- AWAITING_REVIEW
- FAILED
- CANCELLED
- SUPERSEDED

## Flujo

```text
REQUEST
→ TASK
→ IMPACT
→ RISK
→ CONTEXT
→ AUTHORITY
→ EXECUTION
→ EVIDENCE
→ GATE
→ TRANSITION
```

## Regla

Una IA no debe saltar directamente de una conversación a una mutación autoritativa del proyecto.

## Handoff

Una tarea debe poder continuar con otro humano, modelo o agente usando el estado persistido del proyecto.
