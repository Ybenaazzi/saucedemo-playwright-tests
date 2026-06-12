from .base_page import BasePage
from .login_page import LoginPage
from .inventory_page import InventoryPage  # Keeping for compatibility
from .products_page import ProductsPage
from .cart_page import CartPage
from .checkout_page import CheckoutPage

__all__ = [
    'BasePage',
    'LoginPage', 
    'InventoryPage',
    'ProductsPage',
    'CartPage',
    'CheckoutPage'
]