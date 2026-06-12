#!/usr/bin/env python3
"""
Test runner script for SauceDemo tests with Playwright.
Provides various options for running tests with different configurations.
"""

import subprocess
import sys
import argparse
from pathlib import Path


def run_tests(browser="chromium", headed=False, html_report=True, parallel=False):
    """
    Run the test suite with specified options.
    
    Args:
        browser (str): Browser to use for tests (chromium, firefox, webkit)
        headed (bool): Whether to run tests in headed mode (vs headless)
        html_report (bool): Whether to generate HTML report
        parallel (bool): Whether to run tests in parallel
    """
    cmd = ["pytest"]
    
    # Add Playwright-specific options
    cmd.append(f"--browser={browser}")
    
    if headed:
        cmd.append("--headed")
    # Note: headless is the default in Playwright, so we don't need to explicitly add it
    
    if html_report:
        cmd.extend(["--html=reports/test_report.html", "--self-contained-html"])
    
    if parallel:
        cmd.append("-n auto")  # Requires pytest-xdist
    
    # Add verbose output
    cmd.append("-v")
    
    # Add specific test path
    cmd.append("tests/")
    
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        # Ensure the reports directory exists
        import os
        os.makedirs("reports", exist_ok=True)
        
        result = subprocess.run(cmd, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Tests failed with return code: {e.returncode}")
        print(f"Command output: {e.output if hasattr(e, 'output') else 'No output captured'}")
        return e.returncode
    except FileNotFoundError:
        print("Error: pytest or required packages are not installed or not in PATH")
        print("Please ensure you have run: pip install --only-binary=all -r requirements.txt")
        print("And: python -m playwright install")
        print("\nMake sure you are running these commands in the activated virtual environment.")
        print("Virtual environment activation on Windows: saucedemo_env\\Scripts\\activate")
        return 1
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return 1


def install_playwright_browsers():
    """Install required Playwright browsers."""
    try:
        import playwright
        from playwright._repo_version import version
        print(f"Playwright version: {version}")
        
        # Install browsers
        result = subprocess.run([sys.executable, "-m", "playwright", "install"], check=True)
        print("Playwright browsers installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing Playwright browsers: {e}")
        return False
    except ImportError:
        print("Playwright is not installed. Please run: pip install --only-binary=all -r requirements.txt")
        return False
    except Exception as e:
        print(f"Error installing Playwright browsers: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Run SauceDemo tests with Playwright")
    parser.add_argument(
        "--browser", 
        choices=["chromium", "firefox", "webkit"], 
        default="chromium",
        help="Browser to run tests on (default: chromium)"
    )
    parser.add_argument(
        "--headed", 
        action="store_true",
        help="Run tests in headed mode (default is headless)"
    )
    parser.add_argument(
        "--no-report", 
        action="store_true",
        help="Skip HTML report generation"
    )
    parser.add_argument(
        "--parallel", 
        action="store_true",
        help="Run tests in parallel"
    )
    parser.add_argument(
        "--install-browsers",
        action="store_true",
        help="Install Playwright browsers before running tests"
    )
    
    args = parser.parse_args()
    
    if args.install_browsers:
        if not install_playwright_browsers():
            sys.exit(1)
    
    print("Starting SauceDemo test suite with Playwright...")
    print(f"Browser: {args.browser}")
    print(f"Headed: {args.headed}")
    print(f"HTML Report: {not args.no_report}")
    print(f"Parallel: {args.parallel}")
    print("-" * 50)
    
    exit_code = run_tests(
        browser=args.browser,
        headed=args.headed,
        html_report=not args.no_report,
        parallel=args.parallel
    )
    
    sys.exit(exit_code)


if __name__ == "__main__":
    main()