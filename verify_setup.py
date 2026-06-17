"""
Simple script to verify the test setup is working correctly.
"""
import sys
import os
from pathlib import Path

# Ensure project root is in sys.path for consistent imports
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

def verify_basic_functionality():
    print("Starting basic functionality verification...")
    
    # Import after setting up the path
    from playwright.sync_api import sync_playwright
    # Use relative imports that work with the package structure
    from pages.login_page import LoginPage
    from pages.products_page import ProductsPage
    from utils.test_data import TestData

    with sync_playwright() as p:
        try:
            # Launch browser
            browser = p.chromium.launch(headless=True)  # Use headless=True for CI environments
            page = browser.new_page()
            
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
                return False
                
            # Perform a simple login with standard user
            print("Performing login with standard user...")
            login_page.login(
                TestData.VALID_USER_CREDENTIALS["standard_user"]["username"],
                TestData.VALID_USER_CREDENTIALS["standard_user"]["password"]
            )
            
            # Wait for navigation to products page
            page.wait_for_url("**/inventory.html")
            page.wait_for_load_state("load")
            
            # Verify products page is loaded
            print("Verifying products page is loaded...")
            if products_page.is_products_page_loaded():
                print("✓ Products page loaded successfully")
            else:
                print("✗ Products page failed to load")
                return False
            
            # Get number of products
            product_count = len(products_page.get_products())
            print(f"✓ Found {product_count} products on the page")
            
            # Try to add first product to cart
            print("Adding first product to cart...")
            if products_page.add_product_by_index_to_cart(0):
                print("✓ Successfully added first product to cart")
            else:
                print("✗ Failed to add product to cart")
                # This might not be a failure if no products exist, so continue
            
            # Click on shopping cart
            print("Clicking on shopping cart...")
            products_page.click_shopping_cart()
            
            # Wait for cart page to load
            page.wait_for_url("**/cart.html")
            page.wait_for_load_state("load")
            
            print("✓ Navigation to cart successful")
            
            # Close browser
            print("Closing browser...")
            browser.close()
            
            return True
            
        except Exception as e:
            print(f"✗ Error during verification: {str(e)}")
            # Ensure browser is closed in case of error
            try:
                if 'browser' in locals():
                    browser.close()
            except:
                pass
            return False


if __name__ == "__main__":
    success = verify_basic_functionality()
    
    if success:
        print("\n✓ Verification completed successfully!")
        sys.exit(0)
    else:
        print("\n✗ Verification failed!")
        sys.exit(1)