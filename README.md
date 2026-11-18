# QA Engineering Portfolio

A practical portfolio documenting my hands-on learning and experience in Software Quality Assurance, including manual testing, API and database testing, test automation, and security testing.

## Testing Disciplines

### 1. Manual Testing

- Test planning and test case design
- Functional testing
- Positive and negative testing
- Exploratory testing
- Defect identification and reporting

**[Explore Manual Testing Portfolio](manual-testing/README.md)**

### 2. API and Database Testing

- REST API testing with Postman
- HTTP methods and status code validation
- CRUD testing
- SQL and PostgreSQL validation
- API and database consistency testing

**[Explore API Testing Portfolio](api-testing/README.md)**

### 3. Test Automation

- Python and Pytest
- Playwright browser automation
- Pytest fixtures and parameterization
- Browser context isolation
- UI login testing
- API authorization testing

**[Explore Playwright Automation](automation/playwright/)**

### 4. Security Testing

- Authentication and authorization testing
- Access control validation
- Insecure Direct Object Reference (IDOR) testing
- Input validation testing
- Positive and negative security test scenarios
- Regression testing after security remediation

**Explore Security Testing:**

- [Authorization Testing](security-testing/authorization/README.md)
- [IDOR Testing](security-testing/idor/README.md)
- [Input Validation Testing](security-testing/input-validation/README.md)

## Technology Stack

- Python
- Pytest
- Playwright
- Postman
- PostgreSQL
- SQL
- Git and GitHub

## Selected Automation Coverage

The automation project includes test coverage for:

- UI login scenarios, including valid, invalid, and locked-out users
- Browser context isolation
- API authorization, including access control between users and unauthenticated access

Test results are documented separately within the relevant project materials. Counts are not combined here to avoid presenting results from different suites as a single execution.

## Security Testing Coverage

The security testing section documents practical testing activities across three areas:

- **Authorization:** Verifying that authenticated users can access their own resources while unauthorized access is rejected.
- **IDOR:** Demonstrating an insecure direct object reference scenario and validating the effectiveness of the ownership-check remediation.
- **Input Validation:** Testing nonexistent resources and invalid account ID formats to verify expected API responses.

Each area includes its own README, test cases, and execution report. Historical vulnerability demonstrations are distinguished from current regression test results.

## Repository Structure

```text
qa-engineering-portfolio/
├── manual-testing/
│   ├── reports/
│   └── sauce-demo/
│       ├── bug-reports/
│       └── test-cases/
├── api-testing/
│   ├── database-validation/
│   └── postman/
│       ├── task-management-api/
│       └── user-api/
├── automation/
│   └── playwright/
│       ├── app/
│       ├── scripts/
│       └── tests/
├── security-testing/
│   ├── authorization/
│   │   ├── README.md
│   │   ├── test-cases.md
│   │   └── execution-report.md
│   ├── idor/
│   │   ├── README.md
│   │   ├── test-cases.md
│   │   └── execution-report.md
│   └── input-validation/
│       ├── README.md
│       ├── test-cases.md
│       └── execution-report.md
└── README.md
```

## Project Purpose

This repository demonstrates practical QA skills through test planning, test execution, automation, defect documentation, security testing, and validation of application behavior.

All testing activities are performed on intentionally created projects or authorized testing environments.

## Status

This portfolio is actively maintained as new testing skills and practical projects are completed.
