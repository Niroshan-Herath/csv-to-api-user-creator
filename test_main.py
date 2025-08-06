from main import validate_user_data
 
def test_validation():

    # Test valid email

    assert validate_user_data({"email": "good@test.com"}) is True

    # Test missing email

    assert validate_user_data({"email": ""}) is False

    # Test no email key

    assert validate_user_data({"name": "Bob"}) is False
 
