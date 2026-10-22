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
        # Estamos en la raíz del repositorio de la metodología base
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

# Validación de artefactos Core (acepta .yaml o .md)
def check_any_exists(options, error_code, label):
    found = any((ROOT / opt).exists() for opt in options)
    if not found:
        add("ERROR", error_code, f"Falta {label} ({' o '.join(options)})")
        return None
    for opt in options:
        if (ROOT / opt).exists():
            return ROOT / opt
    return None

cp_path = check_any_exists(["GASE_CONTROL.yaml", "GASE_CONTROL.md"], "MISSING_CONTROL_PLANE", "Control Plane")
check_any_exists(["PROJECT.md"], "MISSING_CORE_FILE", "PROJECT.md")
check_any_exists(["INTENT.md"], "MISSING_CORE_FILE", "INTENT.md")
check_any_exists(["SCOPE.md"], "MISSING_CORE_FILE", "SCOPE.md")
check_any_exists(["RULES.yaml", "RULES.md"], "MISSING_RULES", "Reglas del sistema")
check_any_exists(["UNKNOWNS.yaml", "UNKNOWNS.md"], "MISSING_UNKNOWNS", "Registro de incógnitas")

# Runtime
check_any_exists(["runtime/router.yaml", "runtime/ROUTER.md"], "MISSING_RUNTIME_ROUTER", "Router")
check_any_exists(["runtime/context_compiler.yaml", "runtime/CONTEXT_COMPILER.md"], "MISSING_CONTEXT_COMPILER", "Context Compiler")
check_any_exists(["runtime/skill_registry.yaml", "runtime/SKILL_REGISTRY.md"], "MISSING_SKILL_REGISTRY", "Skill Registry")
check_any_exists(["runtime/VERIFICATION.md"], "MISSING_VERIFICATION", "Verification Runtime")

# Control Plane Health
if cp_path and cp_path.exists():
    text = cp_path.read_text(encoding="utf-8", errors="ignore")
    words = len(text.split())
    lines = text.count("\n") + 1
    rel_cp = str(cp_path.relative_to(ROOT))
    if words > 1500:
        add("WARNING", "CONTROL_PLANE_LARGE",
            f"Control Plane grande: ~{words} palabras / {lines} líneas.", rel_cp)
    else:
        add("INFO", "CONTROL_PLANE_SIZE",
            f"Control Plane ({cp_path.suffix}): ~{words} palabras / {lines} líneas.", rel_cp)

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
