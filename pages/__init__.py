from saucedemo_tests.pages.base_page import BasePage
from saucedemo_tests.pages.login_page import LoginPage
from saucedemo_tests.pages.inventory_page import InventoryPage  # Keeping for compatibility
from saucedemo_tests.pages.products_page import ProductsPage
from saucedemo_tests.pages.cart_page import CartPage
from saucedemo_tests.pages.checkout_page import CheckoutPage

__all__ = [
    'BasePage',
    'LoginPage', 
    'InventoryPage',
    'ProductsPage',
    'CartPage',
    'CheckoutPage'
]