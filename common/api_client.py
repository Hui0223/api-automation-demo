from __future__ import annotations

import json
import time
from typing import Any

import requests

from common.logger import get_logger, to_json_summary


class APIClient:
    def __init__(self, base_url: str, default_headers: dict[str, str] | None = None, timeout: float = 5):
        self.base_url = base_url.rstrip("/")
        self.default_headers = default_headers or {}
        self.timeout = timeout
        self.session = requests.Session()
        self.session.trust_env = False
        self.logger = get_logger("project_a.api")

    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _headers(self, headers: dict[str, str] | None) -> dict[str, str]:
        merged = dict(self.default_headers)
        if headers:
            merged.update(headers)
        return merged

    def _request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        url = self._url(path)
        headers = self._headers(kwargs.pop("headers", None))
        start = time.perf_counter()
        response = self.session.request(method, url, headers=headers, timeout=self.timeout, **kwargs)
        response.elapsed_ms = round((time.perf_counter() - start) * 1000, 2)  # type: ignore[attr-defined]
        self._log(method, url, response, kwargs)
        return response

    def get(self, path: str, *, params: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> requests.Response:
        return self._request("GET", path, params=params, headers=headers)

    def post(self, path: str, *, json_body: dict[str, Any] | None = None, headers: dict[str, str] | None = None) -> requests.Response:
        return self._request("POST", path, json=json_body, headers=headers)

    def _log(self, method: str, url: str, response: requests.Response, kwargs: dict[str, Any]) -> None:
        try:
            body: Any = response.json()
        except ValueError:
            body = response.text
        self.logger.info(
            "%s %s -> %s %sms %s",
            method,
            url,
            response.status_code,
            getattr(response, "elapsed_ms", "n/a"),
            to_json_summary(body),
        )
