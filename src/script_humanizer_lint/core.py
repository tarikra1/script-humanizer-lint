"""Deterministic linter for spoken voiceover and short-form video scripts."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass

AI_BUZZWORDS = (
    "delve",
    "tapestry",
    "testament",
    "game-changer",
    "unleash",
    "elevate",
    "ever-evolving",
    "in today's fast-paced",
    "let's dive in",
    "here's the thing",
)

CONTRAST_RE = re.compile(r"\bnot\s+(?:just|merely|only)\s+[^,.!?;]{2,40},\s*but\b", re.IGNORECASE)
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?؟])\s+")


@dataclass(frozen=True)
class ScriptFinding:
    line: int
    rule: str
    detail: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def lint_script(text: str, max_sentence_words: int = 22) -> list[ScriptFinding]:
    findings: list[ScriptFinding] = []
    for idx, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue

        if "—" in line:
            findings.append(ScriptFinding(idx, "NO_EM_DASH", "Replace em-dashes with a clean period or natural spoken pause."))
        if ";" in line:
            findings.append(ScriptFinding(idx, "NO_SEMICOLON", "Split semicolon clauses into two direct spoken sentences."))
        if CONTRAST_RE.search(line):
            findings.append(ScriptFinding(idx, "CONTRAST_CLICHE", "Avoid 'Not just X, but Y' rhetorical contrast patterns."))

        low = line.lower()
        for phrase in AI_BUZZWORDS:
            if phrase in low:
                findings.append(ScriptFinding(idx, "STOCK_AI_PHRASE", f"Detected stock AI phrase: '{phrase}'."))

        for sent in SENTENCE_SPLIT_RE.split(line):
            words = sent.split()
            if len(words) > max_sentence_words:
                findings.append(
                    ScriptFinding(
                        idx,
                        "BREATH_LENGTH",
                        f"Sentence has {len(words)} words (max {max_sentence_words} for crisp voiceover delivery).",
                    )
                )
    return findings
