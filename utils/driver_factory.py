"""
Driver factory module for creating and managing Playwright browser instances.
"""

from playwright.sync_api import sync_playwright
from saucedemo_tests.config import Config


class DriverFactory:
    """
    Factory class for creating and managing Playwright browser instances.
    """
    
    @staticmethod
    def create_browser(browser_type="chromium", headless=True):
        """
        Create a browser instance based on the specified type.
        
        Args:
            browser_type (str): Type of browser to create ('chromium', 'firefox', 'webkit')
            headless (bool): Whether to run browser in headless mode
        
        Returns:
            tuple: A tuple containing (playwright, browser, context, page)
        """
        playwright = sync_playwright().start()
        
        if browser_type.lower() == "chromium":
            browser = playwright.chromium.launch(headless=headless)
        elif browser_type.lower() == "firefox":
            browser = playwright.firefox.launch(headless=headless)
        elif browser_type.lower() == "webkit":
            browser = playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
        
        context = browser.new_context(
            viewport={'width': Config.VIEWPORT_WIDTH, 'height': Config.VIEWPORT_HEIGHT},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        page = context.new_page()
        
        return playwright, browser, context, page

    @staticmethod
    def close_browser(playwright, browser, context=None):
        """
        Close the browser and clean up resources.
        
        Args:
            playwright: The playwright instance
            browser: The browser instance
            context: The context instance (optional)
        """
        if context:
            context.close()
        browser.close()
        playwright.stop()