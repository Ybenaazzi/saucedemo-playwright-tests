# Define the public API for the pages package
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage  # Keeping for compatibility
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

__all__ = [
    'BasePage',
    'LoginPage', 
    'InventoryPage',
    'ProductsPage',
    'CartPage',
    'CheckoutPage'
]
