from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


def requests_setup(browser):
    actions = ActionChains(browser)
    hover_element = browser.find_element(By.ID, "attendance")
    time.sleep(5)
    actions.move_to_element(hover_element).perform()
    requests = browser.find_element(By.XPATH, "//span[@data-key='t-attendance-request']")
    requests.click()


def leave_requests_labels(browser):
    leave_tab = browser.find_element(By.XPATH, "//a[@class='nav-link active']")
    assert leave_tab.text == "Leave", "Label Mismatched"

    leave_entries = browser.find_element(By.CSS_SELECTOR, "div[id='leaves-data-table_length'] label")
    assert leave_entries.text == "Show entries", "Label Mismatched"

    leave_search = browser.find_element(By.CSS_SELECTOR, "div[id='leaves-data-table_filter'] label")
    assert leave_search.text == "Search:", "Label Mismatched"

    request_table_info = browser.find_element(By.ID, "leaves-data-table_info")
    assert request_table_info.text == "Showing 0 to 0 of 0 entries", "Label Mismatched"

    req_prev = browser.find_element(By.ID, "leaves-data-table_previous")
    assert req_prev.text == "Previous"
    req_next = browser.find_element(By.ID, "leaves-data-table_next")
    assert req_next.text == "Next"


def leave_requests_table(browser):
    request_table = browser.find_element(By.ID, "leaves-data-table")
    reqheadings = request_table.find_elements(By.TAG_NAME, "th")
    reqheadingtexts = [reqheadings[0].text, reqheadings[1].text, reqheadings[2].text, reqheadings[3].text,
                       reqheadings[4].text]
    expectedreqheadings = ["Employee", "Duration", "Type", "Status", "Action"]
    assert reqheadingtexts == expectedreqheadings, "Table Headings Mismatched"


def travel_order_requests(browser):
    travel_tab = browser.find_element(By.XPATH, "//span[normalize-space()='Travel Order']")
    assert travel_tab.text == "Travel Order", "Label Mismatched"
    travel_tab.click()

    travel_entries = browser.find_element(By.CSS_SELECTOR, "div[id='travelorder-data-table_length'] label")
    assert travel_entries.text == "Show entries", "Label Mismatched"

    travel_search = browser.find_element(By.CSS_SELECTOR, "div[id='travelorder-data-table_filter'] label")
    assert travel_search.text == "Search:", "Label Mismatched"

    request_table_info = browser.find_element(By.ID, "travelorder-data-table_info")
    assert request_table_info.text == "Showing 0 to 0 of 0 entries", "Label Mismatched"

    req_prev = browser.find_element(By.ID, "travelorder-data-table_previous")
    assert req_prev.text == "Previous"
    req_next = browser.find_element(By.ID, "travelorder-data-table_next")
    assert req_next.text == "Next"


def travel_order_table(browser):
    request_table = browser.find_element(By.ID, "travelorder-data-table")
    reqheadings = request_table.find_elements(By.TAG_NAME, "th")
    reqheadingtexts = [reqheadings[0].text, reqheadings[1].text, reqheadings[2].text, reqheadings[3].text,
                       reqheadings[4].text]
    expectedreqheadings = ["Duration", "Place", "Purpose", "Status", "Action"]
    assert reqheadingtexts == expectedreqheadings, "Table Headings Mismatched"


def overtime_requests(browser):
    overtime_tab = browser.find_element(By.XPATH, "//a[@href='#overtime']")
    assert overtime_tab.text == "Overtime", "Label Mismatched"
    overtime_tab.click()

    overtime_entries = browser.find_element(By.CSS_SELECTOR, "div[id='overtime-data-table_length'] label")
    assert overtime_entries.text == "Show entries", "Label Mismatched"

    overtime_search = browser.find_element(By.CSS_SELECTOR, "div[id='overtime-data-table_filter'] label")
    assert overtime_search.text == "Search:", "Label Mismatched"

    request_table_info = browser.find_element(By.ID, "overtime-data-table_info")
    assert request_table_info.text == "Showing 0 to 0 of 0 entries", "Label Mismatched"

    req_prev = browser.find_element(By.ID, "overtime-data-table_previous")
    assert req_prev.text == "Previous"
    req_next = browser.find_element(By.ID, "overtime-data-table_next")
    assert req_next.text == "Next"


def overtime_table(browser):
    request_table = browser.find_element(By.ID, "overtime-data-table")
    reqheadings = request_table.find_elements(By.TAG_NAME, "th")
    reqheadingtexts = [reqheadings[0].text, reqheadings[1].text, reqheadings[2].text, reqheadings[3].text,
                       reqheadings[4].text, reqheadings[5].text]
    expectedreqheadings = ["Employee", "Date", "Purpose", "Output", "Status", "Action"]
    assert reqheadingtexts == expectedreqheadings, "Table Headings Mismatched"
