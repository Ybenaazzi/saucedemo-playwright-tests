"""
Simple script to verify the test setup is working correctly.
"""
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.test_data import TestData


def verify_basic_functionality():
    print("Starting basic functionality verification...")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # Use headless=False to see the browser
        page = browser.new_page()
        
        try:
            # Go to the login page
            print("Navigating to SauceDemo login page...")
            page.goto(TestData.BASE_URL)
            
            # Create page objects
            login_page = LoginPage(page)
            products_page = ProductsPage(page)
            
            # Verify login page is loaded
            print("Verifying login page is loaded...")
            if login_page.is_login_page_loaded():
                print("✓ Login page loaded successfully")
            else:
                print("✗ Login page failed to load")
                
            # Perform a simple login with standard user
            print("Performing login with standard user...")
            login_page.login(
                TestData.VALID_USER_CREDENTIALS["standard_user"]["username"],
                TestData.VALID_USER_CREDENTIALS["standard_user"]["password"]
            )
            
            # Wait for navigation to products page
            page.wait_for_url("**/inventory.html")
            page.wait_for_load_state("networkidle")
            
            # Verify products page is loaded
            print("Verifying products page is loaded...")
            if products_page.is_products_page_loaded():
                print("✓ Products page loaded successfully")
            else:
                print("✗ Products page failed to load")
            
            # Get number of products
            product_count = len(products_page.get_products())
            print(f"✓ Found {product_count} products on the page")
            
            # Try to add first product to cart
            print("Adding first product to cart...")
            if products_page.add_product_by_index_to_cart(0):
                print("✓ Successfully added first product to cart")
            else:
                print("✗ Failed to add product to cart")
            
            # Click on shopping cart
            print("Clicking on shopping cart...")
            products_page.click_shopping_cart()
            
            # Wait for cart page to load
            page.wait_for_url("**/cart.html")
            page.wait_for_load_state("networkidle")
            
            print("✓ Navigation to cart successful")
            
        except Exception as e:
            print(f"✗ Error during verification: {str(e)}")
        
        finally:
            # Close browser
            print("Closing browser...")
            browser.close()
    
    print("Verification complete!")


if __name__ == "__main__":
    verify_basic_functionality()