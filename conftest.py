from selenium import webdriver
import pytest

@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
