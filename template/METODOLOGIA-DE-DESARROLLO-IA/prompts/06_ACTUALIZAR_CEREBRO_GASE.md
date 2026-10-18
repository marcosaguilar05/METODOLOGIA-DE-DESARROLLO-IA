# Prompt 06 — Actualizar Cerebro Metodológico GASE (v0.2 Pilot)

> **Uso:** Copia y pega este prompt al culminar un hito, refactorización o sesión de trabajo para sincronizar el conocimiento durable del proyecto sin generar ruido operacional innecesario.

```markdown
Actúa como el **Metodólogo de Ingeniería de Software y Custodio del Cerebro GASE** para el proyecto: `[NOMBRE_DEL_PROYECTO]`.

Hemos completado el siguiente hito / cambio técnico en la plataforma:
- **Resumen del cambio o hito:** [DESCRIBE_EL_HITO_O_TRABAJO_REALIZADO]
- **Archivos creados o modificados:** [LISTA_DE_ARCHIVOS_AFECTADOS]
- **Resultado de pruebas / build:** [OUTPUT_DE_TESTS_BUILD_O_VERIFICACION]

---

### 🧠 Directiva de Sincronización Metodológica (Skill: `skills/sync/SKILL.md`):

Aplica el Runtime GASE v0.2 Pilot para consolidar el estado durable del proyecto siguiendo este protocolo:

#### 1. Clasificación Operacional del Cambio (`runtime/ROUTER.md`)
- Determina si el trabajo ejecutado califica como:
  - **`DIRECT`**: Cambio pequeño, reversible, de bajo riesgo. Requiere actualización concisa de `GASE_CONTROL.md` y `state/ES-XXXX.md` con evidencia compacta (evitando burocracia documental de artefactos vacíos).
  - **`GOVERNED`**: Modificó contratos, reglas, datos, arquitectura, seguridad o múltiples superficies. Requiere gobernanza completa proporcional al nivel de rigor (`R1`, `R2`, `R3`).
  - **`CRITICAL`**: Afectó políticas de seguridad, datos sensibles, aislamiento multi-tenant o infraestructura crítica. Exige validación exhaustiva y evidencia formal.

#### 2. Registro de Decisiones Durables (`DECISIONS.md` / `decisions/ADR-XXXX.md`)
- Si durante la sesión se tomó una decisión arquitectónica, de datos o de diseño que deba ser respetada a futuro, regístrala con:
  - Identificador correlativo (`DEC-XXX` o `ADR-XXXX`).
  - Fecha, Estado (`ACCEPTED`), Contexto, Decisión técnica detallada y Justificación/Impacto.

#### 3. Generación del Snapshot de Estado (`state/ES-XXXX.md`)
- Crea el nuevo snapshot incrementando el correlativo (ej. de `ES-0037` a `ES-0038`).
- Incluye:
  - Versión activa de GASE y Rigor del proyecto.
  - Resumen ejecutivo del estado del sistema tras este hito.
  - Invariantes y reglas de negocio preservadas (`RULES.md`).
  - Decisiones activas aplicadas (`DEC-XXX`).
  - Resumen de evidencia determinista verificada.

#### 4. Cadena de Tareas, Entregables y Evidencia (Solo si `GOVERNED` o `CRITICAL`)
- **Tarea (`tasks/TSK-XXXX.md`):** Registra el objetivo técnico, criterios de aceptación y estado `COMPLETED`.
- **Entregable (`deliverables/DEL-XXXX.md`):** Lista de archivos, componentes, endpoints o contratos entregados.
- **Evidencia (`evidence/EVD-XXXX.md`):** Logs deterministas de pruebas unitarias, build (`npm run build`, `pytest`), typechecks o linters.

#### 5. Actualización del Tablero Central (`GASE_CONTROL.md`)
- Actualiza el puntero de **Engineering State** al nuevo `ES-XXXX`.
- Actualiza la **Fase** y **Última Actualización** si corresponde.
- Añade las nuevas decisiones `DEC-XXX` a la lista de vigentes.
- Registra el cierre de la tarea/cambio activo (`NONE` o listo para siguiente hito).
- Limpia o sincroniza `runtime/SESSION_HANDOFF.md` eliminando ruido volátil ya consolidado.

#### 6. Auditoría Determinista de Integridad
- Verifica que las rutas relativas sean válidas y que no existan inconsistencias de enlaces o IDs.
- Confirma que no se promueva ruido operacional (conversaciones o dudas transitorias) a la fuente de verdad.

Por favor, presenta las modificaciones exactas y aplica la sincronización de los artefactos correspondientes.
```
