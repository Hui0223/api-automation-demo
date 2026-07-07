from __future__ import annotations

import pytest

from common.assertions import assert_business_code, assert_has_field, assert_json_response, assert_status


@pytest.mark.smoke
def test_profile_after_login(api_client, login_token):
    response = api_client.get(
        "/jmeter-api/profile",
        headers={"Authorization": f"Bearer {login_token}"},
    )
    body = assert_json_response(response)

    assert_status(response, 200)
    assert_business_code(body, 0)
    assert_has_field(body, "profile")


@pytest.mark.regression
def test_profile_without_token(api_client):
    response = api_client.get("/jmeter-api/profile")
    body = assert_json_response(response)

    assert_status(response, 401)
    assert_business_code(body, 40101)
