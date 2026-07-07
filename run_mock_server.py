#!/usr/bin/env python3
"""Start the local mock API server for manual testing in a browser or Postman."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.mock_server import run_mock_server_forever
from config.settings import get_settings


def main() -> None:
    settings = get_settings()
    run_mock_server_forever(settings.mock_host, settings.mock_port)


if __name__ == "__main__":
    main()
