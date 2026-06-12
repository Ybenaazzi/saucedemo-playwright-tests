import pytest
from .utils.logger import get_logger
from .config import Config


@pytest.fixture(scope="function")
def logger():
    """Fixture to provide a logger instance for each test."""
    return get_logger(__name__)


def pytest_configure(config):
    """Configure pytest settings."""
    if not hasattr(config.option, 'htmlpath') or config.option.htmlpath is None:
        config.option.htmlpath = f"{Config.REPORTS_DIR}/test_report.html"


def pytest_html_report_title(report):
    """Customize the HTML report title."""
    report.title = "SauceDemo Test Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Add screenshot capability if needed
            pass