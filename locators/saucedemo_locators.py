from saucedemo_locators import SauceDemoLocators

def test_locators_import():
    assert hasattr(SauceDemoLocators, 'USERNAME_INPUT'), "USERNAME_INPUT not found in SauceDemoLocators"
    assert hasattr(SauceDemoLocators, 'LOGIN_BUTTON'), "LOGIN_BUTTON not found in SauceDemoLocators"
    print("All locators imported successfully.")

if __name__ == "__main__":
    test_locators_import()
# This file makes the directory a Python package
class SauceDemoLocators:
    # Login Page Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    
    # Inventory Page Locators
    INVENTORY_ITEMS = ".inventory_item"
    ADD_TO_CART_BUTTON = "[data-test^='add-to-cart']"
    REMOVE_FROM_CART_BUTTON = "[data-test^='remove']"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_BUTTON = "#logout_sidebar_link"
    
    # Product Detail Page Locators
    BACK_TO_PRODUCTS_BUTTON = "#back-to-products"
    
    # Cart Page Locators
    CART_ITEMS = ".cart_item"
    CHECKOUT_BUTTON = "#checkout"
    
    # Checkout Page Locators
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    FINISH_BUTTON = "#finish"