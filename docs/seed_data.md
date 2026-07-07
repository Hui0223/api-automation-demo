# Seed Data

Seed data is the stable baseline data required by this automation project.

The current project can run against the built-in mock API server. The mock data is defined in:

```text
common/mock_server.py
```

## Test Users

| Purpose | Username | Password | Role | Expected Result |
|---|---|---|---|---|
| Valid login user | `alice` | `123456` | `tester` | Login succeeds |
| Non-existent user | `not_exist` | `123456` | N/A | Returns business code `1001` |
| Wrong password case | `alice` | `wrong_pass` | `tester` | Returns business code `1002` |

## Token

| Token Type | Value | Purpose |
|---|---|---|
| Valid token | `jt_alice_demo_token` | Access `/jmeter-api/profile` |
| Missing token | N/A | Verify unauthorized access returns `40101` |

## API Expectations

| Endpoint | Scenario | HTTP Status | Business Code |
|---|---|---:|---:|
| `GET /jmeter-api/health` | service is alive | `200` | `0` |
| `POST /jmeter-api/login` | valid user | `200` | `0` |
| `POST /jmeter-api/login` | empty username | `400` | `40001` |
| `POST /jmeter-api/login` | empty password | `400` | `40001` |
| `POST /jmeter-api/login` | non-existent user | `200` | `1001` |
| `POST /jmeter-api/login` | wrong password | `200` | `1002` |
| `GET /jmeter-api/profile` | valid token | `200` | `0` |
| `GET /jmeter-api/profile` | missing token | `401` | `40101` |

## Real Environment Requirement

If `AUTO_START_MOCK=false`, prepare equivalent data in the target environment before running the suite:

```text
alice / 123456
role = tester
not_exist must not exist
wrong_pass must not be alice's valid password
```

Stable seed data helps distinguish product regressions from environment data problems.

