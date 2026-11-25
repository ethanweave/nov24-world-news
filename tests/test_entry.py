import os
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT / "main.py"
IMAGE = ROOT / "entry.png"


class EntryTests(unittest.TestCase):
    def run_entry(self, output: Path) -> bytes:
        env = os.environ.copy()
        env["MAKEFUN_OUTPUT_DIR"] = str(output)
        subprocess.run(
            [sys.executable, str(ENTRY)],
            cwd=ROOT,
            env=env,
            check=True,
            capture_output=True,
        )
        return (output / "entry.png").read_bytes()

    def test_runs_twice_identically(self):
        with tempfile.TemporaryDirectory() as first_dir, tempfile.TemporaryDirectory() as second_dir:
            first = self.run_entry(Path(first_dir))
            second = self.run_entry(Path(second_dir))
        self.assertEqual(first, second)
        self.assertEqual(first, IMAGE.read_bytes())

    def test_image_is_within_limits(self):
        data = IMAGE.read_bytes()
        self.assertLessEqual(len(data), 1_048_576)
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")

        offset = 8
        width = height = None
        saw_end = False
        while offset < len(data):
            length = struct.unpack(">I", data[offset : offset + 4])[0]
            kind = data[offset + 4 : offset + 8]
            payload = data[offset + 8 : offset + 8 + length]
            checksum = struct.unpack(">I", data[offset + 8 + length : offset + 12 + length])[0]
            self.assertEqual(checksum, zlib.crc32(kind + payload) & 0xFFFFFFFF)
            if kind == b"IHDR":
                width, height = struct.unpack(">II", payload[:8])
            if kind == b"IEND":
                saw_end = True
                break
            offset += 12 + length

        self.assertEqual((width, height), (1024, 1024))
        self.assertTrue(saw_end)


if __name__ == "__main__":
    unittest.main()
