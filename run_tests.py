from __future__ import annotations

import sys
from pathlib import Path

import pytest


def main() -> int:
    project_root = Path(__file__).resolve().parent
    reports_dir = project_root / "reports"
    reports_dir.mkdir(exist_ok=True)

    args = [
        "-v",
        "--junitxml",
        str(reports_dir / "junit.xml"),
    ]
    args.extend(sys.argv[1:])
    return pytest.main(args)


if __name__ == "__main__":
    raise SystemExit(main())

