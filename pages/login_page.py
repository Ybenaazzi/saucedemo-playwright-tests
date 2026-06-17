from .base_page import BasePage
from saucedemo_tests.locators.saucedemo_locators import SauceDemoLocators


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = self.find_element(SauceDemoLocators.USERNAME_INPUT)
        self.password_input = self.find_element(SauceDemoLocators.PASSWORD_INPUT)
        self.login_button = self.find_element(SauceDemoLocators.LOGIN_BUTTON)
        self.error_message = self.find_element(SauceDemoLocators.ERROR_MESSAGE)

    def enter_username(self, username):
        """Enter username in the username field."""
        self.fill_input(SauceDemoLocators.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password in the password field."""
        self.fill_input(SauceDemoLocators.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click the login button."""
        self.click_element(SauceDemoLocators.LOGIN_BUTTON)

    def login(self, username, password):
        """Perform login with given credentials."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        """Get error message if login fails."""
        return self.get_inner_text(SauceDemoLocators.ERROR_MESSAGE)

    def is_error_message_visible(self):
        """Check if error message is visible."""
        return self.is_element_visible(SauceDemoLocators.ERROR_MESSAGE)

    def is_login_page_loaded(self):
        """Check if the login page is loaded."""
        return self.is_element_visible(SauceDemoLocators.USERNAME_INPUT)