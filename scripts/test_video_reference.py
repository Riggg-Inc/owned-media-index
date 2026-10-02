"""Regression tests for the reference's fail-closed publication parity check."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from check_video_reference import check, REFERENCE


class VideoReferenceTests(unittest.TestCase):
    def test_repository_copies_match(self):
        check()

    def test_equal_copies_pass(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for path in (root / REFERENCE, root / "docs" / REFERENCE):
                path.parent.mkdir(parents=True)
                path.write_text("reviewed content")
            check(root)

    def test_body_and_metadata_drift_fail(self):
        for changed in ("different body", "different review date"):
            with self.subTest(changed=changed), TemporaryDirectory() as directory:
                root = Path(directory)
                for path, content in ((root / REFERENCE, "reviewed content"), (root / "docs" / REFERENCE, changed)):
                    path.parent.mkdir(parents=True)
                    path.write_text(content)
                with self.assertRaisesRegex(ValueError, "drift"):
                    check(root)

    def test_missing_copy_fails(self):
        with TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "missing"):
                check(Path(directory))


if __name__ == "__main__":
    unittest.main()
