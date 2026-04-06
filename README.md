# playwright-pytestbdd-technical-task

This project was prepared for evaluation in a technical recruitment process.

It demonstrates a UI automation framework built from scratch in **Python** using **Playwright**, **Pytest**, and **Pytest-BDD**, with scenarios written in **Gherkin**.

The required technology stack was defined by the assignment. The goal of this repository is therefore to demonstrate framework structure, implementation quality, and scenario automation rather than stack selection.

---

## Assignment Scope

The original task required choosing at least one scenario block, writing a Gherkin test case in English, and automating it using **Playwright** and **Pytest-BDD**.

This implementation covers scenarios corresponding to **all three assignment levels**.

### Block level 1
- login to email account
- logout

### Block level 2
- login to email account
- create an email message for a recipient from contacts
- send the email
- logout

### Block level 3
- login to email account
- create an email message for a recipient from contacts
- add an attachment
- send the email
- logout

## What This Project Demonstrates

- building a small automation framework from scratch
- BDD scenario definition in **Gherkin**
- test execution with **Pytest-BDD**
- browser automation with **Playwright**
- maintainable structure based on **Page Object Model**
- reusable runtime setup through shared `pytest` fixtures

---

## Technology Stack

- Python 3.11
- Playwright
- Pytest
- Pytest-BDD
- Gherkin

---

## Framework Design

### Gherkin + Pytest-BDD
Scenario behavior is described in Gherkin and mapped to executable steps with Pytest-BDD.

### Page Object Model
Page Objects encapsulate selectors and UI actions, keeping step definitions focused on behavior rather than implementation details.

### Shared fixtures
`conftest.py` centralizes browser setup, page initialization, and runtime configuration.

## Repository Structure

```text
playwright-pytestbdd-technical-task/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── features/
│   └── email_operations.feature
├── pages/
│   ├── email_page.py
│   └── login_page.py
├── tests/
│   ├── steps/
│   │   ├── __init__.py
│   │   └── test_email_steps.py
│   ├── test_data/
│   │   └── funny_attachment.png
│   ├── __init__.py
│   └── test_tutamail.py
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

### Overview
- features/ – Gherkin scenarios
- pages/ – Page Object classes
- tests/steps/ – step definitions for Pytest-BDD
- tests/test_data/ – supporting files for execution
- tests/test_tutamail.py – scenario binding entry point
- conftest.py – shared fixtures and runtime setup
- pytest.ini – pytest configuration
- .github/workflows/ – draft CI workflow

---

## Prerequisites

- Python 3.11
- `pip`
- Playwright browsers installed locally

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```
Install Playwright browsers:

```bash
playwright install
```

## Runtime Configuration
The project currently runs locally using a `.env` file.

Example structure:
```env
BASE_URL=https://app.tuta.com/login
EMAIL_USERNAME=example@tutamail.com
EMAIL_PASSWORD=password
```
Sensitive runtime configuration is intentionally excluded from the repository and provided separately for evaluation purposes.

---
## How to Run
### Recommended full run
```bash
pytest
```
### Alternative explicit run
```bash
pytest tests/test_tutamail.py
```
The default pytest run is the preferred execution path for evaluation.

## Test Data / Attachment Handling

The repository includes an example file for the attachment scenario:

```text
tests/test_data/funny_attachment.png
```
The concrete file type is not important for this task. Any common file can be used for the attachment scenario.

Validation of file type, file size, or unsupported attachment behavior was not part of the requested scope.


---

## Current Status

- scenarios covering all three assignment levels are implemented
- the project is currently executable locally
- runtime secrets are externalized through `.env`
- an initial GitHub Actions workflow draft is included, but CI is not yet finalized

---

## Trade-offs and Limitations

- the chosen technology stack was defined by the assignment
- the repository focuses on framework structure and end-to-end scenario automation
- during implementation, I encountered sending limits of the target email platform, which affected repeated execution of send-related scenarios
- the current version should therefore be treated primarily as a **locally executable technical task submission**
- GitHub Actions setup is currently incomplete due to secret management and platform-side sending constraints
---

## Future Improvements

### Framework / execution
- finalize GitHub Actions secret management
- stabilize CI execution
- improve diagnostics with screenshots, traces, and logs
- improve reporting
- strengthen synchronization and selector robustness
- introduce retry strategy where appropriate
- enable parallel execution

### Test design / coverage
- introduce stronger test data isolation
- extend parameterization of selected scenarios, for example:
  - existing vs. non-existing email
  - different attachment types
  - different message lengths
- add broader negative-path and validation-focused coverage
- separate selected validation scenarios into dedicated tests where appropriate

---

## Notes for Evaluator

- This repository is submitted as part of a technical recruitment process.
- Sensitive runtime values are intentionally not committed to the repository.
- The required local `.env` configuration is provided separately for evaluation.
- Local execution should be considered the primary supported mode in the current state.
- The included GitHub Actions workflow should be treated as a draft extension rather than the primary evaluation path.
