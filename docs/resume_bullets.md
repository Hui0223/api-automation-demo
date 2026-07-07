# Resume Bullets

Use these as a starting point and adjust numbers to match the real project scale.

## Project Bullets

- Built a `pytest` + `requests` API automation project with a structured layout across `tests`, `common`, `data`, `config`, `reports`, and `docs`, improving maintainability and interview readability.

- Designed a reusable `APIClient` layer to centralize base URL handling, headers, timeout, proxy isolation, latency logging, and GET/POST execution, reducing duplicated request code across test cases.

- Implemented data-driven login regression coverage using JSON test data and pytest fixtures, covering success, missing parameters, non-existent user, wrong password, and unauthorized profile access.

- Added environment-based configuration, seed data documentation, smoke/regression markers, and JUnit report generation, enabling the project to run locally or in CI with a single command: `python run_tests.py`.

## Short Interview Pitch

```text
This project demonstrates a runnable API automation framework, not just isolated scripts.
I separated test cases, common request logic, data, configuration, reports, and documentation.
The project supports environment injection, stable seed data, smoke/regression suites, and JUnit report output.
It can run with a built-in mock server, so reviewers can clone it and execute it immediately.
```

