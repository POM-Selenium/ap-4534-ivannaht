import os
from selenium.webdriver.support import expected_conditions as EC
import pytest
import requests
from uuid import uuid4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://127.0.0.1:8000")


@pytest.fixture(scope="session")
def api_base_url(base_url):
    return f"{base_url}/api/v1/user/"


@pytest.fixture(scope="session")
def chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(api_base_url):
    unique = uuid4().hex[:8]
    password = "pass1231**"

    data = {
        "first_name": "APIUser",
        "last_name": "Test",
        "middle_name": "Ui",
        "email": f"api_user_{unique}@test.com",
        "password": password,
        "role": "1",
        "is_active": True,
        "is_staff": False,
    }

    response = requests.post(api_base_url, json=data)
    assert response.status_code in (200, 201), response.text

    return {
        "email": data["email"],
        "password": password,
    }


@pytest.fixture
def login_path():
    return "/auth/login/"


@pytest.fixture
def home_url(base_url):
    return f"{base_url}/"


@pytest.fixture
def home_page(chrome_driver, home_url):
    page = HomePage(chrome_driver, home_url)
    page.open()
    page.wait_for_page_loaded()

    return page


@pytest.fixture
def login_page(chrome_driver, base_url, login_path, home_page, logout):
    home_page.click_login()
    page = LoginPage(chrome_driver, base_url, login_path)
    page.wait_for_page_loaded()

    return page


@pytest.fixture
def logout(chrome_driver, home_page):
    try:
        home_page.click_logout()

        WebDriverWait(chrome_driver, 5).until(
            EC.presence_of_element_located(home_page.LOGIN_LINK)
        )
    except Exception:
        pass
