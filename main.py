import csv
import requests
import logging
from typing import Dict, Any, Set
from pathlib import Path

# Constants defining required fields, API details, timeout in seconds, and log filename

REQUIRED_FIELDS = ["email"]
API_ENDPOINT = "http://zlocalhost/api/create_user"
TIMEOUT = 10
LOG_FILE = "error_log.txt"


def configure_logging() -> None:
    """
    Set up logging configuration:
    - Log messages to a file (error_log.txt) with INFO level and above
    - Log warnings and above also printed to the console
    """
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a",
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    logging.getLogger().addHandler(console_handler)


def get_missing_fields(user_data: Dict[str, Any]) -> Set[str]:
    """
    Check which required fields are missing or empty in the user data.
    Args:
        user_data: Dictionary representing a single user's data from CSV
    Returns:
        A set of field names that are missing or empty
    """
    return {
        field
        for field in REQUIRED_FIELDS
        if field not in user_data or not str(user_data.get(field, "")).strip()
    }


def validate_and_log_user_data(user_data: Dict[str, Any], row_num: int) -> bool:
    """
    Validate the user data by checking for missing required fields.
    If validation fails, log a warning with row number and missing fields.
    Args:
        user_data: Dictionary of user data
        row_num: The line number from the CSV file (starting at 1)
    Returns:
        True if validation passes, False if required fields are missing
    """
    missing_fields = get_missing_fields(user_data)
    if missing_fields:
        user_ident = user_data.get("name", "unnamed user") or "unnamed user"
        logging.warning(
            f"Skipped row {row_num} ({user_ident}): Missing required field(s) - {', '.join(missing_fields)}"
        )
        return False
    return True


def user_creation_request(user_data: Dict[str, Any], row_num: int) -> bool:
    """
    Send an HTTP POST request to create a user via the API endpoint.

    Args:
        user_data: Dictionary of user data to send in JSON format
        row_num: The CSV row number for logging purposes

    Returns:
        True if user creation succeeded (status code 201), False otherwise
    """
    try:
        response = requests.post(API_ENDPOINT, json=user_data, timeout=TIMEOUT)
        response.raise_for_status()
        return response.status_code == 201
    except requests.exceptions.RequestException as e:
        email = user_data.get("email", "no-email-provided")
        logging.error(f"API call failed for row {row_num} ({email}): {str(e)}")
        return False


def create_users(file_path: str) -> None:
    """
    Main function to read users from a CSV file and attempt to create each user.
    It validates user data before sending API requests and logs all important events.

    Args:
        file_path: Path to the CSV file containing user data
    """
    configure_logging()

    if not Path(file_path).exists():
        logging.error(f"Input file does not exist: {file_path}")
        return
    try:
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row_num, row in enumerate(reader, start=1):
                if not validate_and_log_user_data(row, row_num):
                    continue
                if user_creation_request(row, row_num):
                    logging.info(
                        f"Successfully created user {row['email']} (row {row_num})"
                    )
                else:
                    logging.error(
                        f"Failed to create user {row['email']} (row {row_num})"
                    )
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    create_users("users.csv")
