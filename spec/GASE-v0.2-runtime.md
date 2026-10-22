# GASE v0.2 Pilot — Runtime & Experience Layer

## 1. Estado

Esta especificación complementa GASE v0.1.

No modifica el Kernel; define una capa operacional para hacerlo más fácil de usar.

## 2. Arquitectura conceptual

```text
HUMAN / AGENT
      ↓
EXPERIENCE LAYER
      ↓
GOVERNANCE CORE
      ↓
TOOLS / EVIDENCE
      ↓
ENGINEERING STATE
```

## 3. Objetivo

Reducir:

- carga manual de contexto;
- selección manual de prompts;
- archivos redundantes;
- sincronización innecesaria;
- dependencia del historial de chat.

Sin reducir:

- trazabilidad;
- autoridad;
- impacto;
- rigor;
- evidencia;
- gates;
- gobernanza del cambio.

## 4. Runtime

El Runtime es una capa declarativa compuesta por:

- Router;
- Context Compiler;
- Skill Registry;
- Session Handoff;
- Verification Runtime;
- herramientas deterministas opcionales.

No es el runtime del producto.

## 5. Clasificación operacional

### READ_ONLY

No modifica proyecto ni Engineering State.

### DIRECT

Cambio de bajo impacto, local, reversible, con reglas conocidas y verificación simple.

Puede comprimirse físicamente y no requiere crear por reflejo CHG + TASK + EVID + ES.

### GOVERNED

Cambio material en comportamiento, datos, contratos, reglas, arquitectura, seguridad, integración o múltiples superficies.

Activa gobernanza GASE según rigor efectivo.

### CRITICAL

Cambio sujeto a políticas críticas, alta irreversibilidad o consecuencias severas.

Requiere mayor contexto, autoridad y evidencia.

## 6. Router

El usuario expresa intención en lenguaje natural.

El Router decide:

```text
intent
→ operating class
→ context obligations
→ skills
→ workflow
→ verification
→ sync obligations
```

El usuario no necesita memorizar prompts.

## 7. Context Compiler operativo

```text
Context(T) =
CoreContext
+ MandatoryContext(Impact(T))
+ DomainContext(T)
+ ExecutionContext(T)
```

Reglas:

- cargar lo mínimo suficiente;
- historial no es contexto por defecto;
- contexto obligatorio no puede omitirse silenciosamente;
- el Control Plane referencia, no duplica.

## 8. Skills

Una skill es una capacidad reusable y pequeña.

Debe describir:

- cuándo activarse;
- qué leer;
- qué hacer;
- qué no hacer;
- salida esperada;
- verificación relacionada.

Las skills no son agentes permanentes ni pasos obligatorios.

Normalmente se cargan de 1 a 3 por tarea.

## 9. Handoff

Una sesión debe poder continuar con otro agente mediante estado persistido.

El handoff temporal contiene:

- trabajo activo;
- decisiones aún no promovidas;
- verificación realizada;
- siguiente acción;
- bloqueos.

El conocimiento durable termina en los artefactos autoritativos.

## 10. Verificación

Principio:

> Generated ≠ Verified.

Para DIRECT se permite evidencia breve y verificable.

Para GOVERNED/CRITICAL se usan Verification Contract, Evidence Engine y Gates según GASE v0.1.

## 11. Compresión física

GASE distingue garantía conceptual de cantidad de archivos.

En R1/R2 varios elementos pueden convivir en un mismo artefacto si siguen siendo identificables y verificables.

En R3/R4 puede ser necesario separarlos por:

- aprobación;
- independencia;
- auditoría;
- evidencia;
- responsabilidad.

## 12. Control Plane

Debe responder solo:

- dónde estamos;
- qué está activo;
- qué bloquea;
- qué leer;
- qué políticas son críticas;
- qué sigue.

No debe convertirse en historial completo.

## 13. Herramientas deterministas

Se recomienda una herramienta `doctor` para detectar:

- rutas absolutas;
- links rotos;
- IDs inconsistentes;
- tasks cerradas sin evidencia;
- drift entre decisiones y arquitectura;
- estados obsoletos;
- Control Plane excesivo.

Debe auditar antes de modificar.

## 14. Dependencias

GASE v0.2 Pilot:

- no requiere memoria externa;
- no requiere MCP;
- no requiere un modelo concreto;
- no requiere un IDE concreto;
- no requiere cloud;
- no requiere una CLI.

El repositorio puede ser la memoria durable.

## 15. Compatibilidad

Un proyecto v0.1 puede adoptar la capa Runtime de forma aditiva.

No es necesario migrar retrospectivamente toda la historia.

## 16. Dualidad de formatos (YAML / Markdown)

Para reducir la huella de tokens y eliminar la ambigüedad en la manipulación del estado por parte de agentes y herramientas:

1. **Artefactos de estado estructurado y configuración** pueden expresarse en YAML puro:
   - `GASE_CONTROL.yaml`
   - `RULES.yaml`
   - `UNKNOWNS.yaml`
   - `runtime/router.yaml`
   - `runtime/skill_registry.yaml`
   - `runtime/context_compiler.yaml`
2. **Artefactos de razonamiento humano y visión técnica** permanecen en Markdown:
   - `INTENT.md`, `PROJECT.md`, `SCOPE.md`
   - `ARCHITECTURE.md` (diagramas y flujos)
   - `decisions/ADR-XXXX.md` (argumentación y trade-offs)
3. Las herramientas deterministas (`gase_doctor.py`) deben soportar e inspeccionar de forma agnóstica ambos formatos.

