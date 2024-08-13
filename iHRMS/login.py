from selenium.webdriver.common.by import By

def login(driver, username, password):
    try:
        username_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    except:
        print(f"An unexpected error occurred during login.")
