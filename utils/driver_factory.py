# In Playwright, browser instances are handled differently
# This file can be kept for backward compatibility or repurposed
# Playwright handles browser lifecycle differently than Selenium

from playwright.sync_api import sync_playwright
from typing import Generator


class PlaywrightManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start_playwright(self, browser_type="chromium", headless=False, viewport={"width": 1920, "height": 1080}):
        """Start Playwright and launch browser."""
        self.playwright = sync_playwright().start()
        
        if browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=headless)
        elif browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(headless=headless)
        elif browser_type == "webkit":
            self.browser = self.playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_type}")
        
        self.context = self.browser.new_context(viewport=viewport)
        self.page = self.context.new_page()
        
        return self.page

    def close_playwright(self):
        """Close all Playwright instances."""
        if self.page:
            self.page.close()
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()


def get_browser_page(browser_type="chromium", headless=False):
    """Convenience function to get a browser page."""
    manager = PlaywrightManager()
    page = manager.start_playwright(browser_type=browser_type, headless=headless)
    return manager, page