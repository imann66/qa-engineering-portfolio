# Database Validation and Integration Testing

## Overview

This section documents integration testing between the Task Management API and its PostgreSQL database.

The objective is to verify that API operations correctly interact with the database and maintain data integrity.

## Test Scope

- API and database data consistency
- Update persistence
- Delete persistence
- Invalid update handling
- Database constraints
- Transaction rollback
- Data integrity

## Tools

- Python
- REST API
- PostgreSQL
- SQL
- Postman

## Validation Approach

API responses are compared with database records to verify that application operations produce the expected database state.

Database queries are also used to validate persistence, constraints, and rollback behavior.

Refer to `integration-test-cases.md` and `execution-report.md` for details.
