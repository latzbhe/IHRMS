from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def leave_records_setup(browser):
    actions = ActionChains(browser)
    hover_element = browser.find_element(By.ID, "attendance")
    time.sleep(5)
    actions.move_to_element(hover_element).perform()
    records = browser.find_element(By.XPATH, "//span[normalize-space()='Leave Records']")
    records.click()


def leave_records_test(browser):
    employee = browser.find_element(By.XPATH, "//span[normalize-space()='Leave Records']")
    assert employee.text == "Employee:", "Label Mismatched"

    year = browser.find_element(By.XPATH, "//label[normalize-space()='Year:']")
    assert year.text == "Year:", "Label Mismatched"

    month = browser.find_element(By.XPATH, "//label[normalize-space()='Month:']")
    assert month.text == "Month:", "Label Mismatched"

    print_records = browser.find_element(By.ID, "btnPrintLeaveRecord")
    assert print_records.text == "Print Leave Record", "Label Mismatched"

def leave_records_table(browser):
    records_table = browser.find_element(By.ID, "leaves-data-table")
    recheadings = records_table.find_elements(By.TAG_NAME, "th")
    recheadingtexts = [recheadings[0].text, recheadings[1].text, recheadings[2].text, recheadings[3].text,
                       recheadings[4].text]
    expectedrecheadings = ["PERIOD", "PARTICULARS", "VACATION LEAVE", "SICK LEAVE", "UNAUTHORIZED ABSENCE"]
    assert recheadingtexts == expectedrecheadings, "Table Headings Mismatched"