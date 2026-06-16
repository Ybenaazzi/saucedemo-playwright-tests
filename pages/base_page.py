from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def find_element(self, locator):
        """Find a single web element."""
        return self.page.locator(locator)

    def find_elements(self, locator):
        """Find multiple web elements."""
        return self.page.locator(locator)

    def click_element(self, locator):
        """Click on a web element."""
        self.page.locator(locator).click()

    def click_element_wait_for_navigation(self, locator, url=None):
        """Click on a web element and wait for navigation."""
        if url:
            with self.page.expect_navigation(url=url):
                self.page.locator(locator).click()
        else:
            with self.page.expect_navigation():
                self.page.locator(locator).click()

    def fill_input(self, locator, text):
        """Fill input field with text."""
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        """Get text from a web element."""
        return self.page.locator(locator).text_content()

    def get_inner_text(self, locator):
        """Get inner text from a web element."""
        return self.page.locator(locator).inner_text()

    def get_attribute(self, locator, attribute):
        """Get attribute value from a web element."""
        return self.page.locator(locator).get_attribute(attribute)

    def is_element_visible(self, locator):
        """Check if an element is visible on the page."""
        try:
            element = self.page.locator(locator)
            # Wait for the element to be visible first
            element.wait_for(state="visible", timeout=10000)
            return element.is_visible()
        except:
            return False

    def is_element_enabled(self, locator):
        """Check if an element is enabled."""
        try:
            element = self.page.locator(locator)
            return element.is_enabled(timeout=5000)
        except:
            return False

    def wait_for_element(self, locator):
        """Wait for an element to be visible."""
        self.page.locator(locator).wait_for(state="visible")

    def wait_for_url_to_contain(self, url_part):
        """Wait for the URL to contain a specific part."""
        self.page.wait_for_url(f"**/*{url_part}*")

    def get_current_url(self):
        """Get the current page URL."""
        return self.page.url

    def go_back(self):
        """Navigate back to the previous page."""
        self.page.go_back()

    def go_forward(self):
        """Navigate forward to the next page."""
        self.page.go_forward()

    def reload(self):
        """Reload the current page."""
        self.page.reload()

    def scroll_to_element(self, locator):
        """Scroll to an element."""
        self.page.locator(locator).scroll_into_view_if_needed()

    def hover_over_element(self, locator):
        """Hover over an element."""
        self.page.locator(locator).hover()

    def press_key(self, locator, key):
        """Press a key on an element."""
        self.page.locator(locator).press(key)

    def select_option(self, locator, option):
        """Select an option from a dropdown."""
        self.page.locator(locator).select_option(option)

    def check_checkbox(self, locator):
        """Check a checkbox."""
        self.page.locator(locator).check()

    def uncheck_checkbox(self, locator):
        """Uncheck a checkbox."""
        self.page.locator(locator).uncheck()