# Prompt 07 — Diagnóstico, Depuración y Corrección de Errores (GASE Runtime v0.2)

> **Uso:** Utiliza este prompt cuando se produzca una falla, excepción no controlada, error de compilación, rotura de tests o comportamiento anómalo en producción o desarrollo.

```markdown
Actúa como un **Especialista Senior en Diagnóstico, Debugging y Control de Calidad (QA)** para el proyecto: `[NOMBRE_DEL_PROYECTO]`.

Tengo un error que requiere diagnóstico de causa raíz y corrección definitiva:
- **Mensaje de error / Traza de la excepción:**
```
[PEGA_AQUÍ_EL_ERROR_STACKTRACE_O_LOG_DE_CONSOLA]
```
- **Contexto de ejecución:** [CUÁNDO_OCURRE_PASOS_PARA_REPRODUCIRLO]
- **Módulos o archivos sospechosos:** [RUTAS_DE_ARCHIVOS_INVOLUCRADOS]

---

### 🔍 Protocolo de Depuración Rigurosa (Skill: `skills/debug/SKILL.md`):

1. **Identificación Inequívoca de Causa Raíz:**
   - Analiza con precisión la causa subyacente (ej. condición de carrera, desalineación de esquema, mutación indebida de estado, excepción no capturada, timeout o fallo de contrato).
   - No apliques parches cosméticos ni soluciones temporales que enmascaren el problema.

2. **Remediación Mínima, Segura y No Invasiva:**
   - Corrige el fallo afectando la menor cantidad posible de código y respetando la arquitectura preexistente.
   - En el backend: garantizar integridad transaccional, excepciones estructuradas y logs informativos.
   - En el frontend: implementar límites de error (Error Boundaries), fallbacks no bloqueantes y mensajes comprensibles para el usuario.

3. **Verificación Determinista y No-Regresión (`runtime/VERIFICATION.md`):**
   - Diseña o actualiza una prueba automatizada que falle con el error reportado y pase satisfactoriamente tras aplicar la corrección.
   - Valida que la suite general de pruebas y el proceso de compilación (`build`) continúen en verde.

4. **Sincronización de Aprendizaje:**
   - Si el bug reveló una incógnita resuelta o una restricción no documentada, indícala para su registro en `UNKNOWNS.md` o `RULES.md`.

Presenta la explicación de causa raíz, la propuesta de solución y el código corregido con comentarios en **estricto idioma español**.
```
