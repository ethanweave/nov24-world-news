import os
import shutil
from pathlib import Path


IMAGE_NAME = "entry.png"


def main():
    root = Path(__file__).resolve().parent
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(root / IMAGE_NAME, output_dir / IMAGE_NAME)


if __name__ == "__main__":
    main()
