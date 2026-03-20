import os
import pytest
import requests
from uuid import uuid4

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage


def test_login_success_with_user_created_via_api(
    chrome_driver, login_page, registered_user, home_url
):
    login_page.set_email(registered_user["email"])
    login_page.set_password(registered_user["password"])
    login_page.click_login()
    WebDriverWait(chrome_driver, 5).until(
        EC.url_to_be(home_url)
    )
    assert chrome_driver.current_url == home_url


def test_login_fails_with_wrong_password(login_page, registered_user):
    login_page.set_email(registered_user["email"])
    login_page.set_password("wrong_password")
    login_page.click_login()
    error_text = login_page.get_error_text().lower()
    assert (
        "invalid" in error_text
        or "incorrect" in error_text
        or "email" in error_text
        or "password" in error_text
    )


def test_login_fails_with_not_existing_email(login_page):
    login_page.set_email("not_existing_user@test.com")
    login_page.set_password("somepassword123")
    login_page.click_login()
    error_text = login_page.get_error_text().lower()
    assert (
        "invalid" in error_text
        or "incorrect" in error_text
        or "email" in error_text
        or "password" in error_text
    )
