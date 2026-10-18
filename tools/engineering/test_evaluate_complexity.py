"""On-demand portability regression for the complexity compatibility probe."""

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.engineering import evaluate_complexity


class ProbePortabilityTests(unittest.TestCase):
    def test_source_encoding_is_independent_of_windows_legacy_locale(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "example.py"
            source.write_bytes("# coding: utf-8\n# “示例”\ndef sample():\n    return 1\n".encode())
            read_text = Path.read_text

            def legacy_read(path, *args, **kwargs):
                kwargs.setdefault("encoding", "cp1252")
                return read_text(path, *args, **kwargs)

            with mock.patch.object(Path, "read_text", autospec=True, side_effect=legacy_read):
                scores = evaluate_complexity.lizard_scores(source)
            self.assertEqual(scores, [{"name": "sample", "line": 3, "cyclomatic": 1}])


if __name__ == "__main__":
    unittest.main()
