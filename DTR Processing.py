from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def processing_setup(browser):
    actions = ActionChains(browser)
    hover_element = browser.find_element(By.ID, "attendance")
    time.sleep(5)
    actions.move_to_element(hover_element).perform()
    processing = browser.find_element(By.XPATH, "//span[normalize-space()='DTR Processing']")
    processing.click()


def processing_test(browser):
    year = browser.find_element(By.XPATH, "//label[normalize-space()='Year:']")
    assert year.text == "Year:", "Label Mismatched"

    month = browser.find_element(By.XPATH, "//label[normalize-space()='Month:']")
    assert month.text == "Month:", "Label Mismatched"

    final_process = browser.find_element(By.XPATH, "//span[@class='float-end']")
    assert final_process.text == "Final Process DTR", "Label Mismatched"


def processing_table(browser):
    processingtable = browser.find_element(By.ID, "users-data-table")
    processingheadings = processingtable.find_elements(By.TAG_NAME, "th")
    processingheadingtexts = [processingheadings[1].text, processingheadings[2].text]
    expectedprocessingheadings = ["Employee", "Remarks"]
    assert processingheadingtexts == expectedprocessingheadings, "Table Headings Mismatched"
    