
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# Browser setup
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


# Open local dashboard
def open_dashboard(browser):
    page = (
        Path(__file__)
        .with_name("test_dashboard.html")
        .resolve()
        .as_uri()
    )
    browser.get(page)


# Test 1: Verify dashboard title
def test_dashboard_title(browser):
    open_dashboard(browser)

    title = browser.find_element(By.ID, "dashboard-title")

    assert title.text == "Commercial Marketing Analytics Dashboard"


# Test 2: Verify KPI values
def test_dashboard_kpis(browser):
    open_dashboard(browser)

    assert browser.find_element(By.ID, "revenue").text == "958498.30"
    assert browser.find_element(By.ID, "orders").text == "1800"
    assert browser.find_element(By.ID, "customers").text == "250"
    assert browser.find_element(By.ID, "profit").text == "291887.70"


# Test 3: Verify campaign filter
def test_campaign_filter(browser):
    open_dashboard(browser)

    campaign = Select(
        browser.find_element(By.ID, "campaign-filter")
    )

    campaign.select_by_value("festive")

    assert browser.find_element(By.ID, "revenue").text == "158000"
    assert browser.find_element(By.ID, "profit").text == "41050"


# Test 4: Verify campaign filter reset
def test_campaign_filter_reset(browser):
    open_dashboard(browser)

    campaign = Select(
        browser.find_element(By.ID, "campaign-filter")
    )

    campaign.select_by_value("festive")
    campaign.select_by_value("all")

    assert browser.find_element(By.ID, "revenue").text == "958498.30"
    assert browser.find_element(By.ID, "profit").text == "291887.70"


# Test 5: Verify all KPI values are visible
def test_all_kpis_are_visible(browser):
    open_dashboard(browser)

    kpi_ids = [
        "revenue",
        "orders",
        "customers",
        "profit"
    ]

    for kpi_id in kpi_ids:
        element = browser.find_element(By.ID, kpi_id)

        assert element.is_displayed()
        assert element.text.strip() != ""


def test_dashboard_screenshot(browser):
    open_dashboard(browser)

    screenshot_folder = Path(__file__).with_name("artifacts")
    screenshot_folder.mkdir(exist_ok=True)

    screenshot_path = screenshot_folder / "dashboard_screenshot.png"

    saved = browser.save_screenshot(str(screenshot_path))

    assert saved
    assert screenshot_path.exists()

