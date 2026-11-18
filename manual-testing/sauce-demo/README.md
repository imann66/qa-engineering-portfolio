# Manual Testing – Sauce Demo

## 1. Project Overview

This project documents manual software testing activities performed on the [Sauce Demo](https://www.saucedemo.com/) web application.

The objective is to demonstrate practical QA skills through structured test planning, test case design, exploratory testing, defect identification, and bug reporting.

## 2. Testing Objectives

- Verify application functionality against expected behavior.
- Design and execute positive and negative test scenarios.
- Identify functional defects through exploratory testing.
- Document defects with clear reproduction steps.
- Evaluate application behavior under different user conditions.

## 3. Application Under Test

| Attribute        | Details                        |
| ---------------- | ------------------------------ |
| Application      | Sauce Demo                     |
| URL              | https://www.saucedemo.com/     |
| Application Type | E-commerce web application     |
| Browser          | Google Chrome 157.0            |
| Testing Type     | Manual and exploratory testing |

## 4. Testing Scope

The testing activities covered:

- User authentication and login validation.
- Product inventory and product information.
- Shopping cart functionality.
- Checkout process.
- Input validation and application behavior.

## 5. Testing Activities

| Activity            | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| Test Planning       | Defined testing objectives and scope.                          |
| Test Case Design    | Created manual test scenarios and expected results.            |
| Functional Testing  | Executed positive and negative test scenarios.                 |
| Exploratory Testing | Investigated application behavior beyond predefined scenarios. |
| Defect Reporting    | Documented identified defects with severity and priority.      |

## 6. Test Results Summary

The historical login test records contain 11 scenarios:

- 8 Passed
- 1 Failed
- 2 Without recorded execution status

Exploratory testing also identified application behavior requiring further investigation, including product information inconsistencies and checkout issues.

See the individual test execution records for details.

## 7. Project Structure

```text
sauce-demo/
├── README.md
├── test-plan.md
├── exploratory-testing.md
├── test-cases/
│   └── login-test-cases.md
└── bug-reports/
    └── BUG-001.md
```

## 8. Tools and Technologies

- Google Chrome
- Manual Testing
- Exploratory Testing
- Test Case Design
- Bug Reporting
- Markdown
- Git and GitHub

## 9. Limitations

This documentation reflects the recorded results of the learning exercises. Scenarios without recorded execution status are not counted as passed or failed.

Findings associated with specially configured test accounts should not be generalized to all application users.
