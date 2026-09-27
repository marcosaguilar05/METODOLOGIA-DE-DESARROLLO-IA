---
gase:
  version: "0.1"
  artifact: "control_plane"
  project_id: "PROJECT-001"
  project_name: "Gestión Inventario"
  engineering_state: "ES-0001"
  project_rigor: "R2"
  phase: "DISCOVERY"
  status: "ACTIVE"
---

# GASE CONTROL PLANE — Gestión Inventario

## Intent

Plataforma multiempresa de gestión de inventario para negocios de distintos tamaños, incluyendo microempresas, con experiencia sencilla, rápida y visual. También debe poder apoyar un flujo sencillo de despacho/atención.

## Alcance confirmado

- múltiples empresas;
- múltiples ubicaciones por empresa;
- inventario por ubicación;
- entradas y salidas;
- códigos de barras/QR cuando existan;
- panel de actividad;
- traslados gobernados entre ubicaciones;
- precio de venta;
- despacho sencillo.

## Decisiones activas

- DEC-001 — plataforma multiempresa.
- DEC-002 — múltiples ubicaciones por empresa.
- DEC-003 — traslados requieren solicitud/autorización.
- DEC-004 — precio y despacho sencillo forman parte del alcance.

## Incógnitas abiertas

- UNK-004 — modelo de reabastecimiento.
- UNK-005 — roles y permisos.
- UNK-006 — criticidad operacional.
- UNK-007 — integraciones.
- UNK-008 — conectividad/offline.
- UNK-009 — precio global o por ubicación.
- UNK-010 — historial de precios.
- UNK-011 — profundidad del manejo de pagos/caja.
- UNK-012 — estados exactos del traslado.
- UNK-013 — comportamiento del inventario comprometido.

## Tecnología

UNDECIDED.

## Siguiente acción

Continuar Discovery. Resolver política de precios y posteriormente flujo de despacho.

## Regla para IA

No asumir facturación, impuestos, contabilidad o caja completa hasta que se definan.
