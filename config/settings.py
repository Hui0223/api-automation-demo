from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

from common.env import load_dotenv, str_to_bool


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    test_env: str
    base_url: str
    timeout: float
    auto_start_mock: bool
    default_headers: dict[str, str]

    @property
    def mock_host(self) -> str:
        return urlparse(self.base_url).hostname or "127.0.0.1"

    @property
    def mock_port(self) -> int:
        return urlparse(self.base_url).port or 80


def get_settings() -> Settings:
    return Settings(
        test_env=os.getenv("TEST_ENV", "dev"),
        base_url=os.getenv("API_BASE_URL", "http://127.0.0.1:3100"),
        timeout=float(os.getenv("API_TIMEOUT", "5")),
        auto_start_mock=str_to_bool(os.getenv("AUTO_START_MOCK"), default=True),
        default_headers={"Content-Type": "application/json", "Accept": "application/json"},
    )

