#!/usr/bin/env python3
"""AI-DK – automatische Qualitätsprüfungen (Core + Profiles).

Ausführung (Repo-Root):
  python3 .ai/tests/check_core.py

Exit 0 = bestanden, Exit 1 = Fehler.
Schreibt Bericht nach .ai/tests/reports/latest.txt
"""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
AI = ROOT / ".ai"
RULES = AI / "rules"
PROFILES = ROOT / "profiles"
FLUTTER = PROFILES / "flutter"
FLUTTER_RULES = FLUTTER / "rules"
REPORT_DIR = AI / "tests" / "reports"
REPORT_FILE = REPORT_DIR / "latest.txt"

CORE_FILES = [
    "00_PROJECT_CHARTER.md",
    "01_BOOTSTRAP.md",
    "02_DEVELOPMENT_WORKFLOW.md",
    "03_CODING_STANDARDS.md",
    "04_TESTING.md",
    "05_AI_BEHAVIOR.md",
    "06_GIT_WORKFLOW.md",
    "07_DOCUMENTATION.md",
    "08_PROJECT_STATE.md",
    "09_RELEASE_PROCESS.md",
    "10_SECURITY.md",
    "11_VERSION.md",
]

# Bootstrap is agent entry — lean structure, not full norm template
BOOTSTRAP_HEADINGS = [
    "## Ziel",
    "## Geltungsbereich",
    "## Spezifikation",
    "## Verbindliche Startsequenz",
    "## Ausnahmen",
    "## KI-Verhalten",
    "## Checkliste",
    "## Version",
]

REQUIRED_HEADINGS = [
    "## Ziel",
    "## Geltungsbereich",
    "## Grundprinzipien",
    "## Verbindliche Regeln",
    "## Empfehlungen",
    "## KI-Verhalten",
    "## Checkliste",
    "## Beispiele",
    "## Ausnahmen",
    "## Version",
]

RULE_FILES = [
    "coding.yml",
    "testing.yml",
    "git.yml",
    "architecture.yml",
    "documentation.yml",
    "security.yml",
    "release.yml",
    "version.yml",
]

FLUTTER_MD = [
    "README.md",
    "STACK.md",
    "ARCHITECTURE.md",
    "CODING.md",
    "TESTING.md",
]

FLUTTER_STRUCTURED = [
    "STACK.md",
    "ARCHITECTURE.md",
    "CODING.md",
    "TESTING.md",
]

# Backtick refs that look like AI-DK paths / core / profile / docs filenames
REF_RE = re.compile(
    r"`("
    r"(?:\.ai/)?"
    r"(?:"
    r"[0-9]{2}_[A-Z0-9_]+\.md"
    r"|rules/[A-Za-z0-9_./-]+"
    r"|tests/[A-Za-z0-9_./-]+"
    r"|plans/[A-Za-z0-9_./-]+"
    r"|profiles/[A-Za-z0-9_./-]+"
    r")"
    r"|profiles/[A-Za-z0-9_./-]+"
    r"|docs/[A-Za-z0-9_./-]+"
    r"|rfcs/[A-Za-z0-9_./-]+"
    r")`"
)

META_DOCS = [
    "docs/GOVERNANCE.md",
    "docs/GLOSSARY.md",
    "docs/QUALITY.md",
    "docs/adr/README.md",
    "rfcs/README.md",
]


class Checker:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def check_core_present(self) -> None:
        for name in CORE_FILES:
            path = AI / name
            if not path.is_file():
                self.err(f"CORE missing file: {path.relative_to(ROOT)}")

    def check_headings(self) -> None:
        for name in CORE_FILES:
            path = AI / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            headings = BOOTSTRAP_HEADINGS if name == "01_BOOTSTRAP.md" else REQUIRED_HEADINGS
            for heading in headings:
                if heading == "## Checkliste" and "## Checkliste" not in text:
                    if "## Checklisten" in text:
                        self.warn(f"{name}: uses ## Checklisten (prefer ## Checkliste)")
                        continue
                if heading not in text:
                    self.err(f"{name}: missing heading {heading}")

    def _resolve_ref(self, ref: str) -> Path:
        if ref.startswith(".ai/"):
            return ROOT / ref
        if ref.startswith("profiles/") or ref.startswith("docs/") or ref.startswith("rfcs/"):
            return ROOT / ref
        if ref.startswith("rules/") or ref.startswith("tests/") or ref.startswith("plans/"):
            return AI / ref
        return AI / ref

    def check_markdown_refs(self) -> None:
        md_files = (
            list(AI.glob("*.md"))
            + list((AI / "tests").glob("*.md"))
            + list((AI / "plans").glob("*.md"))
            + list(PROFILES.rglob("*.md"))
            + list((ROOT / "docs").rglob("*.md"))
            + list((ROOT / "rfcs").glob("*.md"))
        )
        md_files.append(RULES / "README.md")
        md_files.append(ROOT / "README.md")
        for path in md_files:
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for match in REF_RE.finditer(text):
                ref = match.group(1)
                target = self._resolve_ref(ref)
                if ref.endswith("/"):
                    dir_target = Path(str(target).rstrip("/"))
                    if not dir_target.is_dir():
                        try:
                            rel = dir_target.relative_to(ROOT)
                        except ValueError:
                            rel = dir_target
                        self.err(
                            f"{path.relative_to(ROOT)}: broken dir ref `{ref}` → {rel}"
                        )
                    continue
                if not target.exists():
                    try:
                        rel = target.relative_to(ROOT)
                    except ValueError:
                        rel = target
                    self.err(
                        f"{path.relative_to(ROOT)}: broken ref `{ref}` → {rel}"
                    )

    def check_meta_docs(self) -> None:
        for rel in META_DOCS:
            path = ROOT / rel
            if not path.is_file():
                self.err(f"META missing file: {rel}")
        for name in (
            "0001-core-layout.md",
            "0002-numbering.md",
            "0003-document-structure.md",
            "0004-markdown-canonical.md",
            "0005-specification-bootstrap.md",
        ):
            path = ROOT / "docs" / "adr" / name
            if not path.is_file():
                self.err(f"ADR missing file: docs/adr/{name}")
        if not (ROOT / "rfcs" / "0000-template.md").is_file():
            self.err("META missing file: rfcs/0000-template.md")

    def check_yaml_rules(self) -> None:
        if yaml is None:
            self.err("PyYAML not installed; cannot validate .ai/rules/*.yml")
            return
        seen_ids: set[str] = set()
        for name in RULE_FILES:
            path = RULES / name
            if not path.is_file():
                self.err(f"RULES missing file: {path.relative_to(ROOT)}")
                continue
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                self.err(f"{name}: root must be mapping")
                continue
            if data.get("aidk") != "1.1":
                self.err(f"{name}: aidk must be '1.1' (got {data.get('aidk')!r})")
            source = data.get("source")
            if not source:
                self.err(f"{name}: missing source")
            else:
                src_path = AI / source
                if not src_path.is_file():
                    self.err(f"{name}: source not found: {source}")
            for extra in data.get("sources") or []:
                if not (AI / extra).is_file():
                    self.err(f"{name}: sources entry not found: {extra}")
            rules = data.get("rules")
            if not isinstance(rules, list) or not rules:
                self.err(f"{name}: rules must be a non-empty list")
                continue
            for i, rule in enumerate(rules):
                if not isinstance(rule, dict):
                    self.err(f"{name}: rules[{i}] must be mapping")
                    continue
                rid = rule.get("id")
                sev = rule.get("severity")
                summary = rule.get("summary")
                if not rid:
                    self.err(f"{name}: rules[{i}] missing id")
                elif rid in seen_ids:
                    self.err(f"{name}: duplicate rule id {rid}")
                else:
                    seen_ids.add(rid)
                if sev not in ("must", "should"):
                    self.err(f"{name}: {rid}: severity must be must|should")
                if not summary or not isinstance(summary, str):
                    self.err(f"{name}: {rid}: missing summary")

    def check_flutter_profile(self) -> None:
        if not (PROFILES / "README.md").is_file():
            self.err("PROFILES missing file: profiles/README.md")
        for name in FLUTTER_MD:
            path = FLUTTER / name
            if not path.is_file():
                self.err(f"FLUTTER missing file: {path.relative_to(ROOT)}")
        for name in FLUTTER_STRUCTURED:
            path = FLUTTER / name
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            for heading in REQUIRED_HEADINGS:
                if heading not in text:
                    self.err(f"profiles/flutter/{name}: missing heading {heading}")

        yml = FLUTTER_RULES / "flutter.yml"
        if not yml.is_file():
            self.err(f"FLUTTER missing file: {yml.relative_to(ROOT)}")
            return
        if yaml is None:
            self.err("PyYAML not installed; cannot validate profiles/flutter/rules/flutter.yml")
            return
        data = yaml.safe_load(yml.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            self.err("flutter.yml: root must be mapping")
            return
        if data.get("aidk") != "2.0":
            self.err(f"flutter.yml: aidk must be '2.0' (got {data.get('aidk')!r})")
        if data.get("profile") != "flutter":
            self.err(f"flutter.yml: profile must be 'flutter' (got {data.get('profile')!r})")
        source = data.get("source")
        if not source:
            self.err("flutter.yml: missing source")
        else:
            src = ROOT / source if str(source).startswith("profiles/") else FLUTTER / source
            if not src.is_file():
                self.err(f"flutter.yml: source not found: {source}")
        for extra in data.get("sources") or []:
            target = ROOT / extra if str(extra).startswith("profiles/") else FLUTTER / extra
            if not target.is_file():
                self.err(f"flutter.yml: sources entry not found: {extra}")
        rules = data.get("rules")
        if not isinstance(rules, list) or not rules:
            self.err("flutter.yml: rules must be a non-empty list")
            return
        seen: set[str] = set()
        for i, rule in enumerate(rules):
            if not isinstance(rule, dict):
                self.err(f"flutter.yml: rules[{i}] must be mapping")
                continue
            rid = rule.get("id")
            sev = rule.get("severity")
            summary = rule.get("summary")
            if not rid:
                self.err(f"flutter.yml: rules[{i}] missing id")
            elif rid in seen:
                self.err(f"flutter.yml: duplicate rule id {rid}")
            else:
                seen.add(rid)
            if sev not in ("must", "should"):
                self.err(f"flutter.yml: {rid}: severity must be must|should")
            if not summary or not isinstance(summary, str):
                self.err(f"flutter.yml: {rid}: missing summary")

    def check_readme_points_to_rules(self) -> None:
        readme = ROOT / "README.md"
        text = readme.read_text(encoding="utf-8")
        if ".ai/rules" not in text and "rules/README" not in text:
            self.warn("README.md does not mention .ai/rules")
        if "profiles/flutter" not in text:
            self.warn("README.md does not mention profiles/flutter")

    def run(self) -> int:
        self.check_core_present()
        self.check_headings()
        self.check_markdown_refs()
        self.check_yaml_rules()
        self.check_flutter_profile()
        self.check_meta_docs()
        self.check_readme_points_to_rules()

        lines = [
            f"AI-DK check_core report — {date.today().isoformat()}",
            f"Root: {ROOT}",
            "",
            f"Errors: {len(self.errors)}",
            f"Warnings: {len(self.warnings)}",
            "",
        ]
        if self.errors:
            lines.append("## Errors")
            lines.extend(f"- {e}" for e in self.errors)
            lines.append("")
        if self.warnings:
            lines.append("## Warnings")
            lines.extend(f"- {w}" for w in self.warnings)
            lines.append("")
        if not self.errors:
            lines.append("RESULT: PASS")
        else:
            lines.append("RESULT: FAIL")

        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

        for e in self.errors:
            print(f"ERROR: {e}", file=sys.stderr)
        for w in self.warnings:
            print(f"WARN: {w}", file=sys.stderr)
        print(f"Report: {REPORT_FILE.relative_to(ROOT)}")
        print("PASS" if not self.errors else "FAIL")
        return 1 if self.errors else 0


if __name__ == "__main__":
    sys.exit(Checker().run())
