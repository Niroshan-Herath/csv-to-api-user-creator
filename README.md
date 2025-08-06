# User Account Creation Automation

## Project Overview

This Python project automates the creation of user accounts by reading user data from a CSV file (`users.csv`) and sending HTTP POST requests to a mock API endpoint. The script includes robust validation and error handling to ensure data integrity and proper logging of failures.

---

## Features

- **Input validation:** Skips CSV rows missing required fields (e.g., email).
- **API interaction:** Sends user creation requests to a configurable API endpoint.
- **Error handling:** Logs all errors (missing fields, failed API calls, unexpected issues) to a timestamped log file (`error_log.txt`).
- **Modular design:** Clear, reusable functions for validation, logging, and API communication.
- **Automated testing:** Includes unit tests to verify validation logic.
- **CI/CD pipeline:** Automated linting, testing, containerization, and deployment via GitHub Actions.

---

## Setup and Installation

### Prerequisites

- Python 3.13+
- Docker (for mock API container)
- GitHub account (for CI/CD pipeline integration)

### Installing dependencies

```bash
pip install -r requirements.txt
