# Prompt 05 — Diseño UI/UX Mobile-First y Sistema de Componentes (GASE Runtime v0.2)

> **Uso:** Emplea este prompt cuando necesites diseñar o rediseñar vistas de usuario, componentes táctiles responsivos o flujos ergonómicos Enterprise.

```markdown
Actúa como un **Diseñador UI/UX Senior e Ingeniero Frontend de Sistemas de Diseño** para el proyecto: `[NOMBRE_DEL_PROYECTO]`.

Necesito diseñar o rediseñar la siguiente interfaz:
- **Vista o Componente:** `[NOMBRE_DEL_COMPONENTE_O_VISTA]`
- **Objetivo visual y de uso:** [DESCRIBE_EL_OBJETIVO_DE_INTERACCIÓN_Y_EXPERIENCIA]
- **Dispositivos prioritarios:** [SMARTPHONE / TABLET / ESCRITORIO / TERMINAL POS / DOCK]

---

### 🎨 Protocolo de Experiencia de Usuario y Ergonomía (`UX.md`):

1. **Filosofía Mobile-First Estricta:**
   - Diseñar primero para anchos móviles reducidos (**360px a 430px**) antes de expandir hacia pantallas mayores.
   - **Áreas táctiles ergonómicas:** Todo botón, selector o control interactivo debe contar con un tamaño objetivo mínimo de **44x44px** y feedback visual inmediato al toque.
   - **Tablas y Listados Adaptativos:** Proporcionar vista alternativa en tarjetas/listas en dispositivos móviles para evitar scrolls horizontales forzados.
   - **Navegación y Docks Inferiores:** Respetar safe-area-insets y agregar espaciado de seguridad inferior (`padding-bottom`) para evitar colisiones con barras de navegación móviles.

2. **Sistema de Tokens, Color y Contraste:**
   - Paleta corporativa armónica de alto contraste con jerarquía tipográfica nítida.
   - Acentos de color semánticos (estados de éxito, alerta, advertencia y neutros).
   - Uso de iconografía consistente y comprensible.

3. **Estados de Carga y Transiciones Adaptativas:**
   - Evitar loaders circulares o spinners genéricos.
   - Implementar **Skin Skeletons** (`animate-pulse`) que repliquen la anatomía geométrica del contenido que está por cargar.
   - Micro-animaciones sutiles y fluidas de entrada, salida y transición de vistas.

4. **Sincronización Bidireccional de Estado con la URL:**
   - Los filtros, pestañas activas, identificadores de submódulo y selecciones principales deben reflejarse en los Query Params y Fragmentos Hash de la URL, permitiendo recargar la página o navegar por el historial sin perder el estado de la vista.

5. **Modularidad y Calidad de Componentes:**
   - Componentes atómicos reutilizables en carpetas dedicadas de UI.
   - Archivos contenidos (< 200 líneas) con comentarios y documentación en **estricto idioma español**.

Entrega el diseño completo, la estructura de componentes modulares y el código funcional listo para desplegar.
```
