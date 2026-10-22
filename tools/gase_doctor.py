#!/usr/bin/env python3
"""GASE Doctor — auditoría de integridad, portabilidad y sintaxis para GASE."""
from pathlib import Path
import re
import sys

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# Determinar directorio raíz a auditar
if len(sys.argv) > 1:
    ROOT = Path(sys.argv[1]).resolve()
else:
    script_parent = Path(__file__).resolve().parent
    parent1 = script_parent.parent
    if (parent1 / "template" / "METODOLOGIA-DE-DESARROLLO-IA").exists() and not (parent1 / "GASE_CONTROL.yaml").exists() and not (parent1 / "GASE_CONTROL.md").exists():
        ROOT = parent1 / "template" / "METODOLOGIA-DE-DESARROLLO-IA"
    else:
        ROOT = parent1

issues = []

def add(level, code, message, path=""):
    issues.append((level, code, message, path))

text_ext = {".md", ".txt", ".yaml", ".yml", ".json"}
files = [p for p in ROOT.rglob("*")
         if p.is_file() and ".git" not in p.parts and p.suffix.lower() in text_ext]

absolute_refs = 0
yaml_files_count = 0
md_files_count = 0

for p in files:
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        add("ERROR", "FILE_READ_ERROR", f"No se pudo leer: {e}", str(p.relative_to(ROOT)))
        continue

    rel = str(p.relative_to(ROOT))
    if p.suffix.lower() in {".yaml", ".yml"}:
        yaml_files_count += 1
        if HAS_YAML:
            try:
                yaml.safe_load(text)
            except Exception as e:
                add("ERROR", "INVALID_YAML_SYNTAX", f"Error de sintaxis YAML: {e}", rel)
    elif p.suffix.lower() == ".md":
        md_files_count += 1

    absolute_refs += len(re.findall(r'file:///[A-Za-z]:/|[A-Za-z]:\\\\', text))

if absolute_refs:
    add("WARNING", "PORTABILITY_ABSOLUTE_PATHS",
        f"{absolute_refs} referencias absolutas detectadas; usar rutas relativas cuando sea posible.")

# Detección estricta de duplicados (No deben convivir versión .yaml y .md del mismo archivo)
duplicates = [
    ("GASE_CONTROL.yaml", "GASE_CONTROL.md"),
    ("RULES.yaml", "RULES.md"),
    ("UNKNOWNS.yaml", "UNKNOWNS.md"),
    ("runtime/router.yaml", "runtime/ROUTER.md"),
    ("runtime/context_compiler.yaml", "runtime/CONTEXT_COMPILER.md"),
    ("runtime/skill_registry.yaml", "runtime/SKILL_REGISTRY.md"),
]
for yml_rel, md_rel in duplicates:
    if (ROOT / yml_rel).exists() and (ROOT / md_rel).exists():
        add("ERROR", "DUPLICATE_FILE",
            f"Duplicado detectado: existen {yml_rel} y {md_rel}. Debe conservarse únicamente el formato oficial reemplazado ({yml_rel}).", md_rel)

# Validación de artefactos oficiales requeridos
core_required = [
    ("GASE_CONTROL.yaml", "Control Plane"),
    ("PROJECT.md", "PROJECT.md"),
    ("INTENT.md", "INTENT.md"),
    ("SCOPE.md", "SCOPE.md"),
    ("RULES.yaml", "Reglas del sistema"),
    ("UNKNOWNS.yaml", "Registro de incógnitas"),
]
for rel_path, label in core_required:
    if not (ROOT / rel_path).exists():
        add("ERROR", "MISSING_CORE_FILE", f"Falta {label} ({rel_path})", rel_path)

# Runtime requerido
runtime_required = [
    ("runtime/router.yaml", "Router"),
    ("runtime/context_compiler.yaml", "Context Compiler"),
    ("runtime/skill_registry.yaml", "Skill Registry"),
    ("runtime/VERIFICATION.md", "Verification Runtime"),
]
for rel_path, label in runtime_required:
    if not (ROOT / rel_path).exists():
        add("ERROR", "MISSING_RUNTIME_FILE", f"Falta {label} ({rel_path})", rel_path)

# Health del Control Plane
cp_path = ROOT / "GASE_CONTROL.yaml"
if cp_path.exists():
    text = cp_path.read_text(encoding="utf-8", errors="ignore")
    words = len(text.split())
    lines = text.count("\n") + 1
    rel_cp = str(cp_path.relative_to(ROOT))
    if words > 500:
        add("WARNING", "CONTROL_PLANE_LARGE",
            f"Control Plane grande: ~{words} palabras / {lines} líneas.", rel_cp)
    else:
        add("INFO", "CONTROL_PLANE_SIZE",
            f"Control Plane (.yaml): ~{words} palabras / {lines} líneas.", rel_cp)

add("INFO", "FORMAT_METRICS", f"Archivos auditados: {len(files)} (YAML: {yaml_files_count}, MD: {md_files_count})")

order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
issues.sort(key=lambda x: (order.get(x[0], 9), x[1], x[3]))
counts = {k: sum(1 for i in issues if i[0] == k) for k in order}

print("GASE Doctor v0.2.1")
print("=" * 60)
print(f"Target: {ROOT}")
print(f"ERROR: {counts['ERROR']} | WARNING: {counts['WARNING']} | INFO: {counts['INFO']}")
print("-" * 60)
for level, code, message, path in issues:
    suffix = f" [{path}]" if path else ""
    print(f"{level:<7} {code}: {message}{suffix}")

sys.exit(1 if counts["ERROR"] else 0)
