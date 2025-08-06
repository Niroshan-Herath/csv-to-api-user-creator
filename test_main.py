from main import validate_and_log_user_data  # Correct function name


def test_validation():
    """Test validation logic with different input cases"""
    # Test valid email (row_num is required per your actual function)

    assert (
        validate_and_log_user_data({"email": "good@test.com", "name": "Alice"}, 1)
        is True
    )

    # Test empty email

    assert validate_and_log_user_data({"email": "", "name": "Bob"}, 2) is False

    # Test missing email key

    assert validate_and_log_user_data({"name": "Charlie"}, 3) is False
