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
```

Dependencies include:
- `requests` for HTTP requests
- `pytest` for testing
- `flake8` for code linting

## Usage

### 1. Prepare your user data file:
Ensure `users.csv` exists in the root directory with columns like:
```csv
name,email,role
Alice,alice@example.com,admin
Bob,,user
Charlie,charlie@example.com,moderator
```

### 2. Run the script:
```bash
python main.py
```

### 3. Check logs:
Errors and important info will be logged to `error_log.txt`.

## Project Structure
```
.
├── .github/workflows/python-app.yml  # CI/CD pipeline configuration
├── main.py                           # Main script with core logic
├── mock_api/                         # Mock API Docker container files
├── requirements.txt                  # Python dependencies
├── test_main.py                      # Unit tests
├── users.csv                         # Sample CSV input data
└── README.md                         # Project documentation
```

## Testing
Run tests locally with:
```bash
pytest
```

Tests cover validation logic and simulate API interactions.

## CI/CD Pipeline
Configured via GitHub Actions (`.github/workflows/python-app.yml`), the pipeline:

1. Checks out code on push and pull requests to `main`
2. Sets up Python 3.13 environment
3. Installs dependencies
4. Runs linting with `flake8`
5. Runs unit tests with `pytest`
6. Builds and pushes the mock API Docker image to Docker Hub
7. Runs the mock API container
8. Waits for the mock API to be ready
9. Executes `main.py` against `users.csv`
10. Verifies and outputs logs

### Secrets required:
- `DOCKER_USERNAME` — Docker Hub username
- `DOCKER_PASSWORD` — Docker Hub password

## Suggestions for Future Improvements
- Implement retry logic for transient API failures.
- Add support for configuration via environment variables or config files.
- Expand validation rules beyond just email.
- Parallelize API calls for better performance with large CSVs.
- Add more comprehensive unit and integration tests.
- Improve logging with rotating file handlers or centralized logging.

## Contact / Support
For questions or issues, please open an issue or contact the maintainer.
