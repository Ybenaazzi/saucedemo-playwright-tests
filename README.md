# SauceDemo Test Automation Framework

This is a comprehensive test automation framework for the SauceDemo application built with Python, Playwright, and Pytest.

## Project Structure

```
saucedemo_tests/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   └── inventory_page.py
├── locators/
│   ├── __init__.py
│   └── saucedemo_locators.py
├── utils/
│   ├── __init__.py
│   ├── test_data.py
│   ├── driver_factory.py
│   └── logger.py
├── data/
│   └── __init__.py
├── reports/
│   └── __init__.py
├── tests/
│   └── test_saucedemo.py
├── config.py
├── conftest.py
├── run_tests.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install Playwright browsers:
   ```
   playwright install
   ```
   Or use our test runner with the `--install-browsers` flag

## Running Tests

To run all tests with default settings (Chromium, headless):
```
pytest --browser=chromium
```

To run tests with HTML report:
```
pytest --browser=chromium --html=reports/test_report.html
```

To run tests in headed mode:
```
pytest --browser=chromium --headed
```

To run tests in parallel:
```
pytest --browser=chromium -n auto
```

To run using the test runner:
```
python run_tests.py --install-browsers
```

## Configuration

The framework uses a configuration file (`config.py`) and environment variables to manage settings:

### Configuration Options

- `BASE_URL`: The base URL of the application under test (default: https://www.saucedemo.com/)
- `REPORTS_DIR`: Directory for test reports (default: reports)
- `LOGS_DIR`: Directory for log files (default: logs)

### Using Environment Variables

You can override configuration settings using environment variables:

```bash
export BASE_URL="https://your-test-site.com"
pytest --browser=chromium
```

## Key Features

- Page Object Model (POM) design pattern
- Cross-browser support (Chromium, Firefox, WebKit)
- Comprehensive logging
- Test data management
- Headless/Headed execution options
- Parallel test execution support
- Detailed HTML reports
- Flexible configuration via config file and environment variables

## Utilities

- `test_data.py`: Centralized test data management
- `driver_factory.py`: Playwright browser management utilities
- `logger.py`: Logging functionality with file and console output
- `run_tests.py`: Test runner script with various execution options

## Playwright Specific Features

- Auto-waiting capabilities
- Robust element selection
- Network interception
- Device emulation
- Mobile testing support