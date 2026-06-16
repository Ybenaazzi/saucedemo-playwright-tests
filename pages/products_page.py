from .base_page import BasePage
from ..locators.saucedemo_locators import SauceDemoLocators


class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products_locator = self.find_element(SauceDemoLocators.INVENTORY_ITEMS)
        self.shopping_cart_link = self.find_element(SauceDemoLocators.SHOPPING_CART_LINK)
        self.menu_button = self.find_element(SauceDemoLocators.MENU_BUTTON)

    def get_products(self):
        """Get all product elements on the page."""
        return self.page.query_selector_all(SauceDemoLocators.INVENTORY_ITEMS)

    def get_product_names(self):
        """Get names of all products on the page."""
        product_elements = self.get_products()
        product_names = []
        for product in product_elements:
            name_element = product.query_selector(".inventory_item_name")
            if name_element:
                product_names.append(name_element.inner_text())
        return product_names

    def add_product_by_name_to_cart(self, product_name):
        """Add a specific product to cart by its name."""
        product_elements = self.get_products()
        for product in product_elements:
            name_element = product.query_selector(".inventory_item_name")
            if name_element and product_name.lower() in name_element.inner_text().lower():
                # Find the "Add to Cart" button for this specific product
                add_to_cart_button = product.query_selector(SauceDemoLocators.ADD_TO_CART_BUTTON)
                if add_to_cart_button:
                    add_to_cart_button.click()
                    return True
        return False

    def add_product_by_index_to_cart(self, index):
        """Add a product to cart by its index (0-based)."""
        product_elements = self.get_products()
        if 0 <= index < len(product_elements):
            add_to_cart_button = product_elements[index].query_selector(SauceDemoLocators.ADD_TO_CART_BUTTON)
            if add_to_cart_button:
                add_to_cart_button.click()
                return True
        return False

    def click_shopping_cart(self):
        """Click on the shopping cart icon."""
        self.click_element(SauceDemoLocators.SHOPPING_CART_LINK)

    def click_menu_button(self):
        """Click on the menu button."""
        self.click_element(SauceDemoLocators.MENU_BUTTON)

    def click_logout_button(self):
        """Click on the logout button."""
        self.click_element(SauceDemoLocators.LOGOUT_BUTTON)

    def logout(self):
        """Perform logout from the application."""
        # Click the menu button to open the side menu
        self.click_menu_button()
        
        # Wait for the menu to appear
        self.page.wait_for_selector(SauceDemoLocators.LOGOUT_BUTTON, timeout=5000)
        
        # Click the logout button
        self.click_logout_button()

    def is_products_page_loaded(self):
        """Check if the products page is loaded by checking for visible products."""
        try:
            # Wait for product items to appear on the page
            self.page.wait_for_selector(SauceDemoLocators.INVENTORY_ITEMS, state="visible", timeout=10000)
            # Count visible product items
            count = self.page.locator(SauceDemoLocators.INVENTORY_ITEMS).count()
            return count > 0
        except:
            return False

    def sort_products(self, sort_option):
        """Sort products by a given option (az, za, lohi, hilo)."""
        sort_selector = "select[data-test='product-sort-container']"
        self.page.locator(sort_selector).select_option(sort_option)

    def get_cart_badge_count(self):
        """Get the count from the cart badge on the top right."""
        try:
            cart_badge = self.page.locator(".shopping_cart_badge")
            # Wait for the badge to be visible
            if cart_badge.is_visible():
                return int(cart_badge.inner_text())
            else:
                return 0
        except:
            # If the badge is not visible or has no text, return 0
            return 0