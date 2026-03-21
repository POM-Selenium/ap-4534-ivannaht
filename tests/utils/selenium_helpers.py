import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def highlight(driver: WebDriver, element: WebElement,
              duration: float = 0.3, color: str = "blue", thickness: str = "2px"):
    """Highlight a Selenium element by adding a colored border temporarily."""
    original_style = element.get_attribute("style")
    new_style = f"{original_style}; border: {thickness} solid {color}; border-radius: 3px;"

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                          element, new_style)
    time.sleep(duration)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                          element, original_style)