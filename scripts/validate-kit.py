#!/usr/bin/env python3
"""Valide le kit tokens et estime le contexte always-on (chars/4)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MAX_AGENTS_LINES = 40
MAX_AGENTS_WORDS = 500
MAX_ALWAYS_ON_TOKENS = 800

REQUIRED = [
    "AGENTS.md",
    "docs/strategie.md",
    "docs/playbook.md",
    "templates/brief.md",
    "templates/revue-quotidienne.md",
    "checklists/livraison.md",
    ".cursor/rules/10-brief.mdc",
    ".cursor/rules/20-revue.mdc",
    ".cursor/rules/30-kit.mdc",
]


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4) if text else 0


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def main() -> int:
    errors: list[str] = []
    notes: list[str] = []

    readme = ROOT / "README.md"
    if not readme.is_file():
        errors.append("README.md manquant")
    else:
        first = readme.read_text(encoding="utf-8").lstrip().splitlines()
        if not first or first[0].strip() != "# Project-SG-langue":
            errors.append("README.md : le titre d’origine '# Project-SG-langue' doit rester la première ligne")

    agents = ROOT / "AGENTS.md"
    if not agents.is_file():
        errors.append("AGENTS.md manquant")
        agents_text = ""
    else:
        agents_text = agents.read_text(encoding="utf-8")
        lines = agents_text.splitlines()
        words = word_count(agents_text)
        if len(lines) > MAX_AGENTS_LINES:
            errors.append(f"AGENTS.md : {len(lines)} lignes > {MAX_AGENTS_LINES}")
        if words > MAX_AGENTS_WORDS:
            errors.append(f"AGENTS.md : {words} mots > {MAX_AGENTS_WORDS}")
        notes.append(f"AGENTS.md : {len(lines)} lignes, {words} mots")

    nested = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob("AGENTS.md") if p != agents]
    if nested:
        errors.append("AGENTS.md imbriqués interdits : " + ", ".join(nested))

    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"fichier requis manquant : {rel}")

    always_apply = 0
    mdc_files = sorted(ROOT.glob(".cursor/rules/**/*.mdc"))
    if not mdc_files:
        errors.append("aucune règle .mdc dans .cursor/rules/")
    for path in mdc_files:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append(f"{path.relative_to(ROOT)} : frontmatter manquant")
            continue
        if re.search(r"^alwaysApply:\s*true\s*$", text, re.MULTILINE):
            always_apply += 1
            errors.append(f"{path.relative_to(ROOT)} : alwaysApply true interdit")

    notes.append(f"règles .mdc : {len(mdc_files)} (alwaysApply true : {always_apply})")

    tokens = estimate_tokens(agents_text)
    notes.append(f"always-on estimé : {tokens} tokens (plafond {MAX_ALWAYS_ON_TOKENS})")
    if tokens > MAX_ALWAYS_ON_TOKENS:
        errors.append(f"always-on {tokens} tokens > {MAX_ALWAYS_ON_TOKENS}")

    print("KIT VERT" if not errors else "KIT ROUGE")
    for item in notes:
        print(f"- {item}")
    if errors:
        for item in errors:
            print(f"- ERREUR : {item}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
