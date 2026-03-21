from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.utils.selenium_helpers import highlight


class HomePage:
    TITLE = (By.TAG_NAME, "h1")
    NAVBAR = (By.CSS_SELECTOR, "nav.navbar")
    LOGO_TEXT = (By.CSS_SELECTOR, "nav.navbar .logo-text")
    BACK_HOME_LINK = (By.LINK_TEXT, "Back to home page")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    PROFILE_LINK = (By.LINK_TEXT, "My profile")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def __init__(self, driver, base_url, home_path="/"):
        self.driver = driver
        self.base_url = base_url
        self.home_url = base_url + home_path

    def open(self):
        self.driver.get(self.home_url)

    def wait_for_page_loaded(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.TITLE)
        )

    def click_logout(self, timeout=15):
        logout_link = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )
        highlight(self.driver, logout_link, color="blue")
        logout_link.click()

    def click_login(self, timeout=5):
        login_link = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.LOGIN_LINK)
        )
        highlight(self.driver, login_link, color="blue")
        login_link.click()

    def click_register(self, timeout=5):
        register_link = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.REGISTER_LINK)
        )
        highlight(self.driver, register_link, color="blue")
        register_link.click()

    def click_profile(self, timeout=5):
        profile_link = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.PROFILE_LINK)
        )
        highlight(self.driver, profile_link, color="blue")
        profile_link.click()
