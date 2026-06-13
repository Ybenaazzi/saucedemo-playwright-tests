from playwright.sync_api import Page


def wait_for_page_load(page: Page, timeout: int = 15000):
    """
    Wait for a page to be fully loaded with multiple checks.
    
    Args:
        page: Playwright page object
        timeout: Maximum time to wait in milliseconds
    """
    # Wait for network idle state
    page.wait_for_load_state("networkidle", timeout=timeout)
    
    # Additional wait for DOM content to be loaded
    page.wait_for_load_state("domcontentloaded", timeout=timeout)
    
    # Small additional wait to ensure all dynamic content is loaded
    page.wait_for_timeout(1000)


def safe_click_element(page: Page, locator: str, timeout: int = 5000):
    """
    Safely click an element with proper waits and error handling.
    
    Args:
        page: Playwright page object
        locator: Element locator
        timeout: Maximum time to wait in milliseconds
        
    Returns:
        True if click was successful, False otherwise
    """
    try:
        element = page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        element.wait_for(state="enabled", timeout=timeout)
        element.scroll_into_view_if_needed()
        element.click(timeout=timeout)
        return True
    except Exception:
        return False


def safe_get_text(page: Page, locator: str, timeout: int = 5000):
    """
    Safely get text from an element with proper waits and error handling.
    
    Args:
        page: Playwright page object
        locator: Element locator
        timeout: Maximum time to wait in milliseconds
        
    Returns:
        Text content of the element or empty string if not found
    """
    try:
        element = page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element.inner_text()
    except Exception:
        return ""


def is_element_present_and_visible(page: Page, locator: str, timeout: int = 5000):
    """
    Check if an element is present and visible on the page.
    
    Args:
        page: Playwright page object
        locator: Element locator
        timeout: Maximum time to wait in milliseconds
        
    Returns:
        True if element is present and visible, False otherwise
    """
    try:
        element = page.locator(locator)
        element.wait_for(state="visible", timeout=timeout)
        return element.is_visible()
    except Exception:
        return False