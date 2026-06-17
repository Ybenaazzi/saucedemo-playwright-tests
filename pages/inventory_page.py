from .base_page import BasePage
from ..locators.saucedemo_locators import SauceDemoLocators


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_items = self.find_element(SauceDemoLocators.INVENTORY_ITEMS)
        self.shopping_cart_link = self.find_element(SauceDemoLocators.SHOPPING_CART_LINK)
        self.menu_button = self.find_element(SauceDemoLocators.MENU_BUTTON)

    def get_inventory_items(self):
        """Get all inventory items."""
        return self.page.query_selector_all(SauceDemoLocators.INVENTORY_ITEMS)

    def add_first_item_to_cart(self):
        """Add the first item to cart."""
        add_to_cart_buttons = self.page.query_selector_all(SauceDemoLocators.ADD_TO_CART_BUTTON)
        if add_to_cart_buttons:
            add_to_cart_buttons[0].click()

    def remove_first_item_from_cart(self):
        """Remove the first item from cart."""
        remove_buttons = self.page.query_selector_all(SauceDemoLocators.REMOVE_FROM_CART_BUTTON)
        if remove_buttons:
            remove_buttons[0].click()

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
        self.click_menu_button()
        self.click_logout_button()

    def is_inventory_page_loaded(self):
        """Check if the inventory page is loaded by checking for visible inventory items."""
        try:
            # Wait for inventory items to appear on the page
            self.page.wait_for_selector(SauceDemoLocators.INVENTORY_ITEMS, state="visible", timeout=10000)
            # Count visible inventory items
            count = self.page.locator(SauceDemoLocators.INVENTORY_ITEMS).count()
            return count > 0
        except:
            return False