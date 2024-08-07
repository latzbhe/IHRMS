from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def dtr_setup(browser):
    actions = ActionChains(browser)
    hover_element = browser.find_element(By.ID, "attendance")
    time.sleep(5)
    actions.move_to_element(hover_element).perform()
    dtr = browser.find_element(By.XPATH, "//span[@data-key='t-attendance-dtr']")
    dtr.click()


def dtr_employees(browser):
    employee = browser.find_element(By.XPATH, "//label[@for='selectEmployee']")
    assert employee.text == "Employee:", "Label Mismatch"

    year = browser.find_element(By.XPATH, "//label[normalize-space()='Year:']")
    assert year.text == "Year:", "Label Mismatch"

    month = browser.find_element(By.XPATH, "//label[normalize-space()='Month:']")
    assert month.text == "Month:", "Label Mismatch"

    print_dtr = browser.find_element(By.ID, "btnPrintDTR")
    assert print_dtr.text == "Print DTR"


def dtr_employee_table(browser):
    employee_table = browser.find_element(By.ID, "invitation-data-table")
    headings = employee_table.find_elements(By.XPATH, "//table[@id='invitation-data-table']//thead")
    expected_headings = ["#", "AM In", "AM Out", "PM In", "PM Out"]
    heading_texts = [headings[0].text, headings[1].text, headings[2].text, headings[3].text, headings[4].text]
    assert expected_headings == heading_texts, "Table Headings Mismatched"


def leave_credits(browser):
    label = browser.find_element(By.XPATH, "//h5[normalize-space()='Leave Credits']")
    assert label.text == "Leave Credits", "Label Mismatch"

    credits_table = browser.find_element(By.XPATH, "(//table[@id='tbl_empinfo'])[1]")
    headings1 = credits_table.find_elements(By.TAG_NAME, "th")
    expectedheadings1 = ["Leave Type", "Balance", "Pending", "Projected"]
    headingtexts = [headings1[0].text, headings1[1].text, headings1[2].text, headings1[3].text]
    assert expectedheadings1 == headingtexts, "Table Headings Mismatched"

    tablerows = credits_table.find_elements(By.TAG_NAME, "tr")[0]
    cells = tablerows.find_elements(By.TAG_NAME, "td")
    cell_labels = [cell.text.strip() for cell in cells]
    expected_labels = ["Mandatory/Force Leave", "Sick Leave", "Vacation Leave"]
    if cell_labels == expected_labels:
        print("Row Labels Matched")
    else:
        print("Row Labels Unmatched")

    other_leave = browser.find_element(By.XPATH, "(//table[@id='tbl_empinfo'])[2]")
    headings2 = other_leave.find_elements(By.TAG_NAME, "th")
    expectedheadings2 = ["Other Leave Type", "Balance", "Pending", "Projected"]
    headingtexts2 = [headings2[0].text, headings2[1].text, headings2[2].text, headings2[3].text]
    assert headingtexts2 == expectedheadings2, "Table Headings Mismatched"

    cto_table = browser.find_element(By.XPATH, "(//table[@id='tbl_cto'])[1]")
    headings3 = cto_table.find_elements(By.TAG_NAME, "th")
    expectedheadings3 = ["", "Balance", "Pending", "Projected"]
    headingtexts3 = [headings3[0].text, headings3[1].text, headings3[2].text, headings3[3].text]
    assert headingtexts3 == expectedheadings3, "Table Headings Mismatched"

    cto_row = cto_table.find_elements(By.TAG_NAME, "tr")[0]
    cells1 = cto_row.find_elements(By.TAG_NAME, "td")
    cells1labels = [cell.text.strip() for cell in cells1]
    expectedlabel = ["CTO"]
    if cells1labels == expectedlabel:
        print("Row Labels Matched")
    else:
        print("Row Labels Unmatched")

    monetization_table = browser.find_element(By.XPATH, "(//table[@id='tbl_cto'])[2]")
    heading4 = monetization_table.find_elements(By.TAG_NAME, "th")
    headingtexts4 = [heading4[0].text, heading4[1].text, heading4[2].text]
    expectedheadings4 = ["", "VL", "SL"]
    assert headingtexts4 == expectedheadings4, "Table Headings Mismatched"

    monetization_row = monetization_table.find_elements(By.TAG_NAME, "tr")[0]
    cells2 = monetization_row.find_elements(By.TAG_NAME, "td")
    cells2labels = [cell.text.strip() for cell in cells2]
    expectedlabel2 = ["Monetization"]
    if cells2labels == expectedlabel2:
        print("Row Labels Matched")
    else:
        print("Row Labels Unmatched")


def leave_request(browser):
    request_label = browser.find_element(By.XPATH, "//h5[normalize-space()='Leave Request']")
    assert request_label.text == "Leave Request", "Label Mismatched"

    file_button = browser.find_element(By.XPATH, "//button[normalize-space()='File a Leave']")
    assert file_button.text == "File a Leave", "Label Mismatched"
    file_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(By.CLASS_NAME, "modal-content")
    )

    request_modal = browser.find_element(By.CLASS_NAME, "modal-content")
    assert request_modal.is_displayed(), "Modal is not displayed"
    browser.find_element(By.XPATH, "//div[@id='new-leaves-modal']//button[@type='button'][normalize-space()='Close']").click()

    reqentries = browser.find_element(By.XPATH, "//div[@id='leaves-data-table_length']//label[contains(text(),'Show')]")
    assert reqentries.text == "Show entries", "Label Mismatched"

    reqsearch = browser.find_element(By.XPATH, "//div[@id='leaves-data-table_filter']//label[contains(text(),'Search:')]")
    assert reqsearch.text == "Search:"

    request_table = browser.find_element(By.ID, "leaves-data-table")
    reqheadings = request_table.find_elements(By.TAG_NAME, "th")
    reqheadingtexts = [reqheadings[0].text, reqheadings[1].text, reqheadings[2].text, reqheadings[3].text]
    expectedreqheadings = ["Duration", "Type", "Status", "Action"]
    assert reqheadingtexts == expectedreqheadings, "Table Headings Mismatched"
    reqbody = request_table.find_element(By.TAG_NAME, "tbody")
    assert reqbody.text == "No data available in table", "Content Mismatch"

    request_table_info = browser.find_element(By.ID, "leaves-data-table_info")
    assert request_table_info.text == "Showing 0 to 0 of 0 entries"

    req_prev = browser.find_element(By.ID, "leaves-data-table_previous")
    assert req_prev.text == "Previous"
    req_next = browser.find_element(By.ID, "leaves-data-table_next")
    assert req_next.text == "Next"


def travel_order_request(browser):
    request_label = browser.find_element(By.XPATH, "//h5[normalize-space()='Travel Order Request']")
    assert request_label.text == "Travel Order Request", "Label Mismatched"

    file_button = browser.find_element(By.XPATH, "//button[normalize-space()='File a Travel Order']")
    assert file_button.text == "File a Travel Order", "Label Mismatched"
    file_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(By.CLASS_NAME, "modal-content")
    )

    request_modal = browser.find_element(By.CLASS_NAME, "modal-content")
    assert request_modal.is_displayed(), "Modal is not displayed"
    browser.find_element(By.XPATH, "//div[@id='new-travelorder-modal']//button[@type='button'][normalize-space()='Close']").click()

    reqentries = browser.find_element(By.XPATH, "//div[@id='travelorder-data-table_length']//label[contains(text(),'Show')]")
    assert reqentries.text == "Show entries", "Label Mismatched"

    reqsearch = browser.find_element(By.XPATH, "//div[@id='travelorder-data-table_filter']//label[contains(text(),'Search:')]")
    assert reqsearch.text == "Search:"

    request_table = browser.find_element(By.ID, "travelorder-data-table")
    reqheadings = request_table.find_elements(By.TAG_NAME, "th")
    reqheadingtexts = [reqheadings[0].text, reqheadings[1].text, reqheadings[2].text, reqheadings[3].text, reqheadings[4].text]
    expectedreqheadings = ["Duration", "Place", "Purpose", "Status", "Action"]
    assert reqheadingtexts == expectedreqheadings, "Table Headings Mismatched"
    reqbody = request_table.find_element(By.TAG_NAME, "tbody")
    assert reqbody.text == "No data available in table", "Content Mismatch"

    request_table_info = browser.find_element(By.ID, "travelorder-data-table_info")
    assert request_table_info.text == "Showing 0 to 0 of 0 entries"

    req_prev = browser.find_element(By.ID, "travelorder-data-table_previous")
    assert req_prev.text == "Previous"
    req_next = browser.find_element(By.ID, "travelorder-data-table_next")
    assert req_next.text == "Next"


def overtime_request(browser):
    request_label = browser.find_element(By.XPATH, "//h5[normalize-space()='Overtime Request']")
    assert request_label.text == "Overtime Request", "Label Mismatched"

    file_button = browser.find_element(By.XPATH, "//button[normalize-space()='File an Overtime Request']")
    assert file_button.text == "File a Travel Order", "Label Mismatched"
    file_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(By.CLASS_NAME, "modal-content")
    )

    request_modal = browser.find_element(By.CLASS_NAME, "modal-content")
    assert request_modal.is_displayed(), "Modal is not displayed"
    browser.find_element(By.XPATH, "//div[@id='new-overtime-modal']//button[@type='button'][normalize-space()='Close']").click()

    reqentries = browser.find_element(By.XPATH, "//div[@id='overtime-data-table_length']//label[contains(text(),'Show')]")
    assert reqentries.text == "Show entries", "Label Mismatched"

    reqsearch = browser.find_element(By.XPATH, "//div[@id='overtime-data-table_filter']//label[contains(text(),'Search:')]")
    assert reqsearch.text == "Search:"

    request_table = browser.find_element(By.ID, "overtime-data-table")
    reqheadings = request_table.find_elements(By.TAG_NAME, "th")
    reqheadingtexts = [reqheadings[0].text, reqheadings[1].text, reqheadings[2].text, reqheadings[3].text,
                       reqheadings[4].text]
    expectedreqheadings = ["Date", "Purpose", "Output", "Status", "Action"]
    assert reqheadingtexts == expectedreqheadings, "Table Headings Mismatched"
    reqbody = request_table.find_element(By.TAG_NAME, "tbody")
    assert reqbody.text == "No data available in table", "Content Mismatch"

    request_table_info = browser.find_element(By.ID, "overtime-data-table_info")
    assert request_table_info.text == "Showing 0 to 0 of 0 entries"

    req_prev = browser.find_element(By.ID, "overtime-data-table_previous")
    assert req_prev.text == "Previous"
    req_next = browser.find_element(By.ID, "overtime-data-table_next")
    assert req_next.text == "Next"


def monetization_request(browser):
    request_label = browser.find_element(By.XPATH, "//h5[normalize-space()='Monetization Request']")
    assert request_label.text == "Monetization Request", "Label Mismatched"

    file_button = browser.find_element(By.XPATH, "//button[normalize-space()='File Monetization Request']")
    assert file_button.text == "File Monetization Request", "Label Mismatched"
    file_button.click()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located(By.CLASS_NAME, "modal-content")
    )

    request_modal = browser.find_element(By.CLASS_NAME, "modal-content")
    assert request_modal.is_displayed(), "Modal is not displayed"
    browser.find_element(By.XPATH,
                         "//div[@id='new-monetization-modal']//div[@class='modal-footer']//button[1]").click()

    reqentries = browser.find_element(By.XPATH, "//div[@id='monetization-data-table_length']//label")
    assert reqentries.text == "Show entries", "Label Mismatched"

    reqsearch = browser.find_element(By.XPATH, "//div[@id='monetization-data-table_length']//label")
    assert reqsearch.text == "Search:"

    request_table = browser.find_element(By.ID, "monetization-data-table")
    reqheadings = request_table.find_elements(By.TAG_NAME, "th")
    reqheadingtexts = [reqheadings[0].text, reqheadings[1].text, reqheadings[2].text, reqheadings[3].text]
    expectedreqheadings = ["Date Filed", "VL", "SL", "Action"]
    assert reqheadingtexts == expectedreqheadings, "Table Headings Mismatched"
    reqbody = request_table.find_element(By.TAG_NAME, "tbody")
    assert reqbody.text == "No data available in table", "Content Mismatch"

    request_table_info = browser.find_element(By.ID, "monetization-data-table_info")
    assert request_table_info.text == "Showing 0 to 0 of 0 entries"

    req_prev = browser.find_element(By.ID, "monetization-data-table_previous")
    assert req_prev.text == "Previous"
    req_next = browser.find_element(By.ID, "monetization-data-table_next")
    assert req_next.text == "Next"
