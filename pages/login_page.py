from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    TITLE = (By.TAG_NAME, "h1")
    EMAIL_INPUT = (By.ID, "id_email")
    PASSWORD_INPUT = (By.ID, "id_password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.login-btn")
    ERROR_TEXT = (By.CSS_SELECTOR, ".error-text")
    REGISTER_LINK = (By.LINK_TEXT, "Register")
    BACK_HOME_LINK = (By.LINK_TEXT, "Back to home page")

    def __init__(self, driver, base_url, login_path):
        self.driver = driver
        self.base_url = base_url
        self.login_url = base_url + login_path

    def open(self):
        self.driver.get(self.login_url)

    def wait_for_page_loaded(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.TITLE)
        )

    def set_email(self, value):
        el = self.driver.find_element(*self.EMAIL_INPUT)
        el.clear()
        el.send_keys(value)

    def set_password(self, value):
        el = self.driver.find_element(*self.PASSWORD_INPUT)
        el.clear()
        el.send_keys(value)

    def click_login(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_text(self, timeout=5):
        el = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.ERROR_TEXT)
        )
        return el.text

    def click_register(self):
        self.driver.find_element(*self.REGISTER_LINK).click()

    def click_back_home(self):
        self.driver.find_element(*self.BACK_HOME_LINK).click()
        