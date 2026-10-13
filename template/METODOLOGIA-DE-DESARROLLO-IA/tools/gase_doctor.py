#!/usr/bin/env python3
"""GASE Doctor — auditoría de solo lectura y sin dependencias externas."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
issues = []

def add(level, code, message, path=""):
    issues.append((level, code, message, path))

text_ext = {".md", ".txt", ".yaml", ".yml", ".json"}
files = [p for p in ROOT.rglob("*")
         if p.is_file() and ".git" not in p.parts and p.suffix.lower() in text_ext]

absolute_refs = 0
for p in files:
    text = p.read_text(encoding="utf-8", errors="ignore")
    absolute_refs += len(re.findall(r'file:///[A-Za-z]:/|[A-Za-z]:\\\\', text))

if absolute_refs:
    add("WARNING", "PORTABILITY_ABSOLUTE_PATHS",
        f"{absolute_refs} referencias absolutas detectadas; usar rutas relativas cuando sea posible.")

required = ["GASE_CONTROL.md", "PROJECT.md", "INTENT.md", "SCOPE.md"]
for rel in required:
    if not (ROOT / rel).exists():
        add("ERROR", "MISSING_CORE_FILE", f"Falta {rel}", rel)

runtime_required = [
    "runtime/ROUTER.md",
    "runtime/CONTEXT_COMPILER.md",
    "runtime/SKILL_REGISTRY.md",
    "runtime/VERIFICATION.md",
]
for rel in runtime_required:
    if not (ROOT / rel).exists():
        add("WARNING", "MISSING_RUNTIME_FILE", f"Falta {rel}", rel)

cp = ROOT / "GASE_CONTROL.md"
if cp.exists():
    text = cp.read_text(encoding="utf-8", errors="ignore")
    words = len(text.split())
    lines = text.count("\n") + 1
    if words > 2500:
        add("WARNING", "CONTROL_PLANE_LARGE",
            f"Control Plane grande: ~{words} palabras / {lines} líneas.", "GASE_CONTROL.md")
    else:
        add("INFO", "CONTROL_PLANE_SIZE",
            f"Control Plane: ~{words} palabras / {lines} líneas.", "GASE_CONTROL.md")

order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
issues.sort(key=lambda x: (order.get(x[0], 9), x[1], x[3]))
counts = {k: sum(1 for i in issues if i[0] == k) for k in order}

print("GASE Doctor")
print("=" * 60)
print(f"Root: {ROOT}")
print(f"ERROR: {counts['ERROR']} | WARNING: {counts['WARNING']} | INFO: {counts['INFO']}")
print("-" * 60)
for level, code, message, path in issues:
    suffix = f" [{path}]" if path else ""
    print(f"{level:<7} {code}: {message}{suffix}")

sys.exit(1 if counts["ERROR"] else 0)
