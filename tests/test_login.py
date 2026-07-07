from __future__ import annotations

import pytest

from common.assertions import assert_business_code, assert_has_field, assert_json_response, assert_status


def test_login_cases_loaded(login_cases):
    assert len(login_cases) >= 5


@pytest.mark.regression
def test_login_with_data(api_client, login_cases):
    for case in login_cases:
        response = api_client.post("/jmeter-api/login", json_body=case["input"])
        body = assert_json_response(response)

        assert_status(response, case["expected"]["status_code"])
        assert_business_code(body, case["expected"]["code"])
        if case["expected"]["code"] == 0:
            assert_has_field(body, "token")
