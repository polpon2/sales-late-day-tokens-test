# Testing Guide

`sales-late-day-tokens-test` contains tests for the sales late-day tokens functionality.

## Prerequisite

Make sure you have [Poetry](https://python-poetry.org/) installed.

## Disclaimer

1. It is recommended to have a fresh database before running the tests (to avoid user conflicts with the tester)
2. Make sure no one request requests while the test is running, or else some test will break
3. It is recommended to test in development settings (since it WILL change stuff in the database for real)

## Running Tests
```bash
# Assuming you are inside the "sales-late-day-tokens-test" folder

poetry install && poetry run pytest tests
```

## Test Repo Structure
```bash
sales-late-day-tokens-test
├── README.md
├── app.py
├── poetry.lock
├── pyproject.toml
└── tests # Tests Module
    ├── __init__.py
    ├── test_core.py # Tests normal functionality
    ├── test_fail.py # Tests forced kill
    └── test_timeout.py # Tests forced timeout
```

# Contributing
Feel free to contribute by opening issues or creating pull requests.