class TestData:
    """包含测试所需的所有测试数据常量"""
    
    # Valid user credentials
    VALID_USER_CREDENTIALS = {
        "standard_user": {
            "username": "standard_user",
            "password": "secret_sauce"
        },
        "problem_user": {
            "username": "problem_user",
            "password": "secret_sauce"
        },
        "performance_glitch_user": {
            "username": "performance_glitch_user",
            "password": "secret_sauce"
        },
        "error_user": {
            "username": "error_user",
            "password": "secret_sauce"
        },
        "visual_user": {
            "username": "visual_user",
            "password": "secret_sauce"
        }
    }

    # Locked out user
    LOCKED_USER = {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }

    # Invalid user credentials - changed from set to list
    INVALID_CREDENTIALS = [
        {"username": "", "password": ""},
        {"username": "invalid_user", "password": "invalid_password"}
    ]

    # URLs
    BASE_URL = "https://www.saucedemo.com/"
    
    # Error messages
    ERROR_MESSAGES = {
        "empty_credentials": "Epic sadface: Username is required",
        "locked_user": "Epic sadface: Sorry, this user has been locked out.",
        "invalid_credentials": "Epic sadface: Username and password do not match any user in this service"
    }
    
    # Product information
    PRODUCTS = [
        {"name": "Sauce Labs Backpack", "price": "$29.99"},
        {"name": "Sauce Labs Bike Light", "price": "$9.99"},
        {"name": "Sauce Labs Bolt T-Shirt", "price": "$15.99"},
        {"name": "Sauce Labs Fleece Jacket", "price": "$49.99"},
        {"name": "Sauce Labs Onesie", "price": "$7.99"},
        {"name": "Test.allTheThings() T-Shirt (Red)", "price": "$15.99"}
    ]