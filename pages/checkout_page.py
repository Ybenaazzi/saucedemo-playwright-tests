from .base_page import BasePage
from ..locators import SauceDemoLocators


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def enter_checkout_info(self, first_name, last_name, postal_code):
        """Enter checkout information."""
        self.fill_input(SauceDemoLocators.FIRST_NAME_INPUT, first_name)
        self.fill_input(SauceDemoLocators.LAST_NAME_INPUT, last_name)
        self.fill_input(SauceDemoLocators.POSTAL_CODE_INPUT, postal_code)

    def click_continue_button(self):
        """Click the continue button."""
        self.click_element(SauceDemoLocators.CONTINUE_BUTTON)

    def click_finish_button(self):
        """Click the finish button."""
        self.click_element(SauceDemoLocators.FINISH_BUTTON)

    def is_checkout_step_one_loaded(self):
        """Check if the first step of checkout page is loaded."""
        try:
            # Wait for checkout form fields to appear
            self.page.wait_for_selector(SauceDemoLocators.FIRST_NAME_INPUT, state="visible", timeout=10000)
            return (
                self.is_element_visible(SauceDemoLocators.FIRST_NAME_INPUT) and
                self.is_element_visible(SauceDemoLocators.LAST_NAME_INPUT) and
                self.is_element_visible(SauceDemoLocators.POSTAL_CODE_INPUT)
            )
        except:
            return False

    def is_checkout_step_two_loaded(self):
        """Check if the second step of checkout page is loaded."""
        try:
            # Look for overview elements
            overview_selector = "[data-test='checkout-step-two-container']"
            return self.page.locator(overview_selector).is_visible(timeout=10000)
        except:
            return False

    def is_checkout_complete_loaded(self):
        """Check if the checkout complete page is loaded."""
        try:
            # Look for completion elements
            complete_header = "h2[data-test='complete-header']"
            return self.page.locator(complete_header).is_visible(timeout=10000)
        except:
            return False

    def get_checkout_items(self):
        """Get items in the checkout overview."""
        item_selectors = ".cart_item"
        items = self.page.query_selector_all(item_selectors)
        checkout_items = []
        for item in items:
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
            
            checkout_items.append(item_details)
        return checkout_items