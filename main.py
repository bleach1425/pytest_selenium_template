from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import time

class TestCase:
    def test_login_system(self, selenium):
        options = Options()
        options.add_argument("--disable-notifications")
        # settings
        selenium.implicitly_wait(15)
        selenium.maximize_window()
        selenium.delete_all_cookies()

        # Work flow
        selenium.get("http://192.168.5.181:5000/auth/login")
        time.sleep(3)
        selenium.find_element_by_id("email").send_keys("asd@gmail.com")
        time.sleep(1)
        selenium.find_element_by_id("password").send_keys("asd")
        time.sleep(1)
        selenium.find_element_by_id("submit").click()


if __name__ == "__main__":
    pytest.main(["-s", 'main.py'])
