from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from common.api_client import APIClient
from common.mock_server import start_mock_server
from config.settings import get_settings


@pytest.fixture(scope="session")
def settings():
    return get_settings()


@pytest.fixture(scope="session", autouse=True)
def mock_server(settings):
    if not settings.auto_start_mock:
        yield None
        return

    server = start_mock_server(settings.mock_host, settings.mock_port)
    yield server
    server.shutdown()
    server.server_close()


@pytest.fixture(scope="session")
def api_client(settings, mock_server):
    return APIClient(
        base_url=settings.base_url,
        default_headers=settings.default_headers,
        timeout=settings.timeout,
    )


@pytest.fixture(scope="session")
def login_token(api_client):
    response = api_client.post(
        "/jmeter-api/login",
        json_body={"username": "alice", "password": "123456"},
    )
    body = response.json()
    assert response.status_code == 200
    assert body["code"] == 0
    return body["token"]


@pytest.fixture(scope="session")
def login_cases():
    path = PROJECT_ROOT / "data" / "login_cases.json"
    return json.loads(path.read_text(encoding="utf-8"))
