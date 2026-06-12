"""
Configuration file for SauceDemo test automation framework with Playwright.
Contains all configurable parameters for the test suite.
"""

import os
from urllib.parse import urlparse


class Config:
    # Application settings
    BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
    
    # Test data settings
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30000"))  # Playwright uses milliseconds
    
    # Reporting settings
    REPORTS_DIR = os.getenv("REPORTS_DIR", "reports")
    LOGS_DIR = os.getenv("LOGS_DIR", "logs")
    
    # Screenshot settings
    SCREENSHOTS_ON_FAILURE = os.getenv("SCREENSHOTS_ON_FAILURE", "true").lower() == "true"
    SCREENSHOTS_DIR = os.getenv("SCREENSHOTS_DIR", "screenshots")
    
    # Viewport settings
    VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1920"))
    VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "1080"))
    
    # User credentials (these could also be loaded from environment variables or external files)
    STANDARD_USER = os.getenv("STANDARD_USER", "standard_user")
    LOCKED_USER = os.getenv("LOCKED_USER", "locked_out_user")
    PROBLEM_USER = os.getenv("PROBLEM_USER", "problem_user")
    PERFORMANCE_USER = os.getenv("PERFORMANCE_USER", "performance_glitch_user")
    ERROR_USER = os.getenv("ERROR_USER", "error_user")
    VISUAL_USER = os.getenv("VISUAL_USER", "visual_user")
    COMMON_PASSWORD = os.getenv("COMMON_PASSWORD", "secret_sauce")
    
    @classmethod
    def validate_config(cls):
        """Validate the configuration values."""
        if cls.DEFAULT_TIMEOUT <= 0:
            raise ValueError("DEFAULT_TIMEOUT must be greater than 0")
        
        parsed_url = urlparse(cls.BASE_URL)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError(f"Invalid BASE_URL: {cls.BASE_URL}")


# Validate configuration on import
Config.validate_config()