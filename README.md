# script-humanizer-lint

[![CI](https://github.com/tarikra1/script-humanizer-lint/actions/workflows/ci.yml/badge.svg)](https://github.com/tarikra1/script-humanizer-lint/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/release-v1.0.0-0EA5E9.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Deterministic linter for short-form video and voiceover scripts that strips LLM rhetorical tells (`Not just X, but Y`, `Let's dive in`, em-dashes, semicolons, stock buzzwords) and enforces natural spoken breath lengths.**

## Quickstart

```bash
pip install -e .
script-humanizer voiceover.txt --max-words 20 --json
```

## License

MIT License — see [LICENSE](LICENSE).
