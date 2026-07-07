# Project Structure

## tests

Pytest test cases and fixtures. Test files should focus on inputs and assertions.

## common

Reusable code such as `APIClient`, assertion helpers, environment loading, and local mock server.
Keep request mechanics, logging, and common assertions here. Business case logic should stay in `tests`.

## data

Structured test data. Keep case data outside test logic.

## config

Runtime settings. Values are read from environment variables and optional `.env`.

## reports

Generated reports such as JUnit XML, HTML, or Allure output.

## docs

Project notes, environment guide, and conventions.

Current docs:

- `project_structure.md`: directory responsibilities.
- `seed_data.md`: stable users, tokens, and expected API results.
- `resume_bullets.md`: resume and interview wording.
