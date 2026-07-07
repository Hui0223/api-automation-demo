from __future__ import annotations

import pytest

from common.assertions import assert_business_code, assert_has_field, assert_json_response, assert_status


@pytest.mark.smoke
def test_health(api_client):
    response = api_client.get("/jmeter-api/health")
    body = assert_json_response(response)

    assert_status(response, 200)
    assert_business_code(body, 0)
    assert_has_field(body, "service")
