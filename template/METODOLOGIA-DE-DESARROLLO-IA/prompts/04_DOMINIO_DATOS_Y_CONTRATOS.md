# Prompt 04 — Modelado de Dominio, Datos y Contratos (GASE Runtime v0.2)

> **Uso:** Utiliza este prompt cuando requieras modelar nuevas entidades de negocio, definir contratos de API, esquemas de validación o capas de persistencia y datos.

```markdown
Actúa como un **Especialista en Arquitectura de Dominio y Datos** para el proyecto: `[NOMBRE_DEL_PROYECTO]`.

Necesito modelar o modificar la siguiente entidad / contrato de datos:
- **Entidad o Contrato:** `[NOMBRE_DE_LA_ENTIDAD_O_SERVICIO]`
- **Propósito de negocio:** [DESCRIBE_EL_MODELO_Y_SUS_REGLAS_DE_NEGOCIO]
- **Operaciones requeridas:** [CRUD / TRANSACCIONES_COMPLEJAS / EVENTOS / AGREGACIONES]

---

### 🗄️ Protocolo de Dominio y Persistencia (Skill: `skills/domain/SKILL.md`):

1. **Gobernanza de Datos (`DATA.md` & `RULES.yaml`):**
   - Asegurar coherencia con el modelo de datos documentado en `DATA.md`.
   - Garantizar el aislamiento de datos (por ejemplo, multi-tenancy o segmentación obligatoria por empresa/usuario).
   - Validar restricciones de integridad referencial, índices para consultas frecuentes y transacciones con commit/rollback atómico.

2. **Diseño de Contratos y Esquemas:**
   - Diseñar esquemas de entrada (validación estricta), esquemas de persistencia y esquemas de salida (DTOs).
   - Definir contratos de API claros (OpenAPI, endpoints REST o RPC) con códigos de estado HTTP semánticos.
   - Proteger los datos sensibles y evitar la fuga de campos internos en respuestas públicas.

3. **Capa de Persistencia Reutilizable (DRY):**
   - Centralizar las operaciones de base de datos en DAOs, repositorios o servicios desacoplados de la capa de transporte o presentación.
   - Cero consultas duplicadas ad-hoc.

4. **Comentarios y Documentación:**
   - Comentar exhaustivamente cada campo, relación e invariante de negocio en **estricto idioma español**.

Presenta el diagrama o esquema de entidades, los contratos de validación, la capa de persistencia y las instrucciones de migración si aplican.
```
