from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_logout_with_user_created_via_api(
        chrome_driver, login_page, registered_user, home_url, home_page):
    login_page.set_email(registered_user["email"])
    login_page.set_password(registered_user["password"])
    login_page.click_login()

    WebDriverWait(chrome_driver, 5).until(
        EC.url_to_be(home_url)
    )

    logout_link_element = WebDriverWait(chrome_driver, 5).until(
        EC.element_to_be_clickable(home_page.LOGOUT_LINK)
    )
    logout_link_element.click()

    login_link_element = WebDriverWait(chrome_driver, 5).until(
        EC.visibility_of_element_located(home_page.LOGIN_LINK)
    )

    assert login_link_element
