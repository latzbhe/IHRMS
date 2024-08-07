from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()


def login(browser):
    browser.get("http://10.10.99.4/login")
    email = browser.find_element(By.ID, "username")
    email.send_keys("hr_officer@pcaarrd.dost.gov.ph")
    password = browser.find_element(By.ID, "userpassword")
    password.send_keys("qweasdzxc")
    browser.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()


def attendancetab(browser):
    attendance = browser.find_element(By.ID, "attendance")
    assert attendance.text == "Attendance", "Label Mismatch"
