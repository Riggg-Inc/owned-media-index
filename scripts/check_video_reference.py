"""Narrow publication guard: this reference's source and public copy must match."""
from pathlib import Path
import argparse
import sys

REFERENCE = Path("tools/hosting/video-podcast-hosting-support.md")
ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    source = root / REFERENCE
    public = root / "docs" / REFERENCE
    if not source.is_file() or not public.is_file():
        raise ValueError("Video reference source/public copy is missing")
    if source.read_bytes() != public.read_bytes():
        raise ValueError("Video reference drift: review source, then run scripts/check_video_reference.py --sync")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sync", action="store_true", help="Explicitly copy reviewed source to docs; never changes review dates")
    args = parser.parse_args()
    if args.sync:
        (ROOT / "docs" / REFERENCE).write_bytes((ROOT / REFERENCE).read_bytes())
    try:
        check()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    print("Video reference source/public copy match")
    return 0


if __name__ == "__main__":
    sys.exit(main())
