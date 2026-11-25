import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import unittest

from script_humanizer_lint.core import lint_script


class TestScriptHumanizer(unittest.TestCase):
    def test_clean_spoken_script_passes(self) -> None:
        clean = "Most editors waste two hours cutting dead air. This workflow finishes the timeline in thirty seconds."
        self.assertEqual(lint_script(clean), [])

    def test_catches_em_dash_buzzwords_and_contrast(self) -> None:
        slop = "Let's dive in — this tool is not just fast, but a complete game-changer; it will elevate everything."
        rules = {f.rule for f in lint_script(slop)}
        self.assertIn("NO_EM_DASH", rules)
        self.assertIn("NO_SEMICOLON", rules)
        self.assertIn("CONTRAST_CLICHE", rules)
        self.assertIn("STOCK_AI_PHRASE", rules)


if __name__ == "__main__":
    unittest.main()
