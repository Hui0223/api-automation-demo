from __future__ import annotations

from typing import Any


def assert_status(response: Any, expected_status: int) -> None:
    assert response.status_code == expected_status, (
        f"status mismatch: expected={expected_status}, actual={response.status_code}, body={response.text}"
    )


def assert_business_code(body: dict[str, Any], expected_code: int) -> None:
    actual_code = body.get("code")
    assert actual_code == expected_code, f"business code mismatch: expected={expected_code}, actual={actual_code}, body={body}"


def assert_has_field(body: dict[str, Any], field: str) -> None:
    assert field in body, f"missing field: {field}, body={body}"


def assert_json_response(response: Any) -> dict[str, Any]:
    try:
        body = response.json()
    except ValueError as exc:
        raise AssertionError(f"response is not valid JSON: status={response.status_code}, body={response.text}") from exc
    assert isinstance(body, dict), f"response JSON should be object, actual={type(body).__name__}, body={body}"
    return body
