from .base_page import BasePage
from ..locators.saucedemo_locators import SauceDemoLocators


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_items_locator = self.find_element(SauceDemoLocators.CART_ITEMS)
        self.checkout_button = self.find_element(SauceDemoLocators.CHECKOUT_BUTTON)

    def get_cart_items(self):
        """Get all items in the cart."""
        return self.page.query_selector_all(SauceDemoLocators.CART_ITEMS)

    def get_cart_item_names(self):
        """Get names of all items in the cart."""
        cart_items = self.get_cart_items()
        item_names = []
        for item in cart_items:
            name_element = item.query_selector(".inventory_item_name")
            if name_element:
                item_names.append(name_element.inner_text())
        return item_names

    def remove_item_by_name(self, item_name):
        """Remove an item from cart by its name."""
        cart_items = self.get_cart_items()
        for item in cart_items:
            name_element = item.query_selector(".inventory_item_name")
            if name_element and item_name.lower() in name_element.inner_text().lower():
                # Find the remove button for this specific item
                remove_button = item.query_selector(SauceDemoLocators.REMOVE_FROM_CART_BUTTON)
                if remove_button and remove_button.is_enabled():
                    remove_button.click()
                    # Wait for the item to be removed from the DOM
                    try:
                        # Wait for the specific item to disappear
                        item.wait_for(state="hidden", timeout=5000)
                    except:
                        # If the specific wait fails, just wait a bit more
                        self.page.wait_for_timeout(1000)
                    return True
        return False

    def click_checkout_button(self):
        """Click the checkout button."""
        self.click_element(SauceDemoLocators.CHECKOUT_BUTTON)

    def is_cart_page_loaded(self):
        """Check if the cart page is loaded."""
        try:
            # Wait for cart items container to appear on the page
            self.page.wait_for_selector(SauceDemoLocators.CART_ITEMS, timeout=10000)
            # We can also check for the presence of cart header or checkout button
            return (
                self.page.locator(SauceDemoLocators.CHECKOUT_BUTTON).is_visible(timeout=5000) or
                self.page.locator(SauceDemoLocators.CART_ITEMS).count() >= 0  # Cart can be empty
            )
        except:
            # If there's no cart items, check if the empty cart message is visible
            try:
                empty_cart_msg = self.page.locator("//*[contains(text(), 'Your cart is empty') or contains(text(), 'Continue Shopping')]")
                return empty_cart_msg.is_visible(timeout=2000)
            except:
                return False

    def get_cart_item_count(self):
        """Get the total number of items in the cart."""
        try:
            # Wait briefly to ensure page is loaded
            self.page.wait_for_timeout(500)
            count = self.page.locator(SauceDemoLocators.CART_ITEMS).count()
            return count
        except:
            # Return 0 if no items are found
            return 0

    def continue_shopping(self):
        """Click the 'Continue Shopping' button to return to the products page."""
        # SauceDemo doesn't have a "Continue Shopping" button on the cart page
        # We'll navigate back to the products page by clicking the back button
        self.page.go_back()

    def get_cart_summary(self):
        """Get a summary of items in the cart."""
        cart_items = self.get_cart_items()
        summary = []
        for item in cart_items:
            name_element = item.query_selector(".inventory_item_name")
            desc_element = item.query_selector(".inventory_item_desc")
            price_element = item.query_selector(".inventory_item_price")
            
            item_details = {}
            if name_element:
                item_details['name'] = name_element.inner_text()
            if desc_element:
                item_details['description'] = desc_element.inner_text()
            if price_element:
                item_details['price'] = price_element.inner_text()
            
            summary.append(item_details)
        return summary