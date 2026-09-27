# Niveles de rigor

## R1 — Essential

Para bajo riesgo y alcance reducido.

Permite fuerte compresión de artefactos, pero conserva el Kernel.

## R2 — Controlled

Para producto comercial ordinario, varios módulos, múltiples usuarios o integraciones moderadas.

## R3 — Governed

Para datos sensibles, necesidad fuerte de auditoría, integración crítica o alto impacto.

## R4 — Critical

Para consecuencias severas o controles especializados.

## Regla

Una tarea puede elevar el rigor aunque el proyecto normalmente opere en un nivel menor.

```text
EffectiveRigor =
MAX(ProjectRigor, ChangeRigor, PolicyMinimum)
```

## Nunca

No se reduce rigor solamente porque el proceso resulte incómodo.
