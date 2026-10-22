# Prompt 02 — Implementar Nueva Funcionalidad (GASE Runtime v0.2)

> **Uso:** Copia y pega este prompt cuando necesites construir una nueva característica, módulo o flujo de negocio completo.

```markdown
Actúa como un **Ingeniero de Software Senior** para el proyecto: `[NOMBRE_DEL_PROYECTO]`.

Necesito implementar la siguiente funcionalidad:
- **Nombre de la funcionalidad:** [NOMBRE_DE_LA_FUNCIONALIDAD]
- **Requerimiento detallado:** [DESCRIPCIÓN_COMPLETA_DEL_COMPORTAMIENTO_ESPERADO]
- **Superficies afectadas:** [FRONTEND / BACKEND / DB / CONTRATOS / INTEGRACIONES]

---

### ⚙️ Protocolo de Implementación Gobernado (Skill: `skills/feature/SKILL.md`):

1. **Enrutamiento Operacional (`runtime/router.yaml`):**
   - Si afecta modelos de datos, reglas de negocio o contratos compartidos, trátala como **`GOVERNED`**.
   - Si es un ajuste local y contenido, clasifícala como **`DIRECT`**.

2. **Alineación de Contexto Mínimo (`runtime/context_compiler.yaml`):**
   - Consulta `REQUIREMENTS.md` y `RULES.yaml` para respetar invariantes de negocio.
   - Si afecta datos o persistencia, revisa `DATA.md` y los modelos existentes.
   - Si afecta la arquitectura del sistema, consulta `ARCHITECTURE.md` y `DECISIONS.md`.

3. **Pautas de Calidad de Código:**
   - **Modularidad (SRP):** Desacoplar la lógica de orquestación, reglas de negocio y persistencia.
   - **Comentarios Exhaustivos:** Todo código nuevo o modificado debe contener explicaciones detalladas en **estricto idioma español**.
   - **Tipado Fuerte:** Definir interfaces, tipos o esquemas explícitos (cero `any`).
   - **Manejo de Errores Resiliente:** Tratamiento atómico de excepciones, mensajes de error semánticos y degradación no bloqueante en UI.

4. **Verificación Determinista (`runtime/VERIFICATION.md`):**
   - Proporciona las pruebas unitarias o de integración correspondientes para verificar el nuevo comportamiento.

Presenta el análisis de impacto, la propuesta técnica y el código completo implementado archivo por archivo.
```
