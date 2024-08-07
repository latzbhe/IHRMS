from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
browser.maximize_window()

actions = ActionChains(browser)

browser.get("http://10.10.99.4/login")

title = browser.title

browser.find_element(By.ID, "username")
Email = browser.find_element(By.ID, "username")
Email.send_keys("hr_officer@pcaarrd.dost.gov.ph")

browser.find_element(By.ID, "userpassword")
Password = browser.find_element(By.ID, "userpassword")
Password.send_keys("qweasdzxc")

browser.find_element(By.CSS_SELECTOR, "body > div.login-box > div.card > div > form > div:nth-child(4) > button").click()

Attendance = browser.find_element(By.ID, "attendance")

hover_element = browser.find_element(By.ID, "attendance")
time.sleep(5)
actions.move_to_element(hover_element).perform()
DTR = browser.find_element(By.CSS_SELECTOR, "#topnav-menu-content > ul > li:nth-child(3) > div > a:nth-child(1) > span")
DTR.click()
assert "DTR" in title, "Title Mismatch"

Employee = browser.find_element(By.ID, "selectEmployee")
selectEmployee = Select(Employee)
selectEmployee.select_by_index(0)

Year = browser.find_element(By.ID, "s_year")
selectYear = Select(Year)
selectYear.select_by_visible_text("2022")

Month = browser.find_element(By.ID, "s_mon")
selectMonth = Select(Month)
selectMonth.select_by_visible_text("May")

# PrintDTR
browser.find_element(By.ID, "btnPrintDTR").click()
browser.switch_to.window(browser.window_handles[1])
browser.close()

# AM-IN
browser.find_element(By.CSS_SELECTOR, "#invitation-data-table > tbody > tr:nth-child(1) > td:nth-child(2)").click()
browser.find_element(By.ID, "dtr_time").send_keys("0803")
browser.find_element(By.ID, "btn_dtr_add").click()

# AM-OUT
browser.find_element(By.CSS_SELECTOR, "#invitation-data-table > tbody > tr:nth-child(1) > td:nth-child(3)").click()
browser.find_element(By.ID, "dtr_time").send_keys("0803")
browser.find_element(By.ID, "btn_dtr_add").click()

# PM IN
browser.find_element(By.CSS_SELECTOR, "#invitation-data-table > tbody > tr:nth-child(1) > td:nth-child(4)").click()
browser.find_element(By.ID, "dtr_time").send_keys("0803")
browser.find_element(By.ID, "btn_dtr_add").click()

# PM OUT
browser.find_element(By.CSS_SELECTOR, "#invitation-data-table > tbody > tr:nth-child(1) > td:nth-child(5)").click()
browser.find_element(By.ID, "dtr_time").send_keys("0803")
browser.find_element(By.ID, "btn_dtr_add").click()

# Leave Credits

# Leave Request
Type = "#layout-wrapper > div.main-content > div > div.row.m-2 > div:nth-child(4) > div:nth-child(2) > div.card-header > span > button"
RequestType = browser.find_element(By.CSS_SELECTOR, Type)
LeaveType = Select(RequestType)
LeaveType.select_by_visible_text("Vacation Leave")

browser.find_element(By.ID, "leave_date_from").click()
Month = browser.find_element(By.CLASS_NAME, "flatpickr-monthDropdown-month")
selectMonth = Select(Month)
selectMonth.select_by_visible_text("August")
browser.find_element(By.CSS_SELECTOR, "body > div.flatpickr-calendar.rangeMode.animate.open.arrowTop.arrowLeft > div.flatpickr-innerContainer > div > div.flatpickr-days > div > span:nth-child(28)").click()

Duration = browser.find_element(By.ID, "leave_date_duration")
selectDuration = Select(Duration)
selectDuration.select_by_visible_text("Wholeday")
browser.find_element(By.ID, "btn_leave_add").click()
browser.find_element(By.LINK_TEXT, "Ok").click()

# Print Leave Request
browser.find_element(By.CLASS_NAME, "btn btn-success btn-sm").click()
browser.switch_to.window(browser.window_handles[1])
browser.close()

# Update Leave Request
browser.find_element(By.CLASS_NAME, "btn btn-info btn-sm").click()
Edit = browser.find_element(By.ID, "edit_leave_date_duration")
selectDuration = Select(Edit)
selectDuration.select_by_visible_text("AM")
browser.find_element(By.ID, "btn_leave_edit").click()
browser.find_element(By.CLASS_NAME, "swal2-confirm swal2-styled swal2-default-outline").click()

# Delete Leave Request
browser.find_element(By.CLASS_NAME, "btn btn-danger btn-sm").click()
browser.find_element(By.CLASS_NAME, "swal2-confirm swal2-styled swal2-default-outline").click()
browser.find_element(By.CLASS_NAME, "swal2-confirm swal2-styled").click()

# Travel Order Request
browser.find_element(By.LINK_TEXT, "File a Travel Order").click()
browser.find_element(By.LINK_TEXT, "CLose").click()
browser.find_element(By.CSS_SELECTOR, "#travelorder-data-table > tbody > tr > td:nth-child(5) > center > a").click()
browser.close()
EditTravel = "#travelorder-data-table > tbody > tr > td:nth-child(5) > center > button.btn.btn-info.btn-sm"
browser.find_element(By.CSS_SELECTOR, EditTravel).click()
browser.find_element(By.ID, "edit_travel_purpose").send_keys("To submit DOST ISSP")
browser.find_element(By.ID, "btn_travelorder_edit").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
DeleteTravel = "#travelorder-data-table > tbody > tr > td:nth-child(5) > center > button.btn.btn-danger.btn-sm"
browser.find_element(By.CSS_SELECTOR, DeleteTravel).click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()

# Overtime Request
browser.find_element(By.LINK_TEXT, "File an Overtime Request").click()
browser.find_element(By.ID, "overtime_purpose").send_keys("To finalize DOST ISSP")
browser.find_element(By.ID, "overtime_output").send_keys("Finalized ISSP")
browser.find_element(By.ID, "btn_overtime_add").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.CSS_SELECTOR, "#overtime-data-table > tbody > tr > td:nth-child(5) > center > a").click()
browser.close()
UpdateOvertime = "#overtime-data-table > tbody > tr > td:nth-child(5) > center > button.btn.btn-info.btn-sm"
browser.find_element(By.CSS_SELECTOR, UpdateOvertime)
browser.find_element(By.ID, "btn_overtime_edit").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
DeleteOvertime = "#overtime-data-table > tbody > tr > td:nth-child(5) > center > button.btn.btn-danger.btn-sm"
browser.find_element(By.CSS_SELECTOR, DeleteOvertime).click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()

# Monetization Request
browser.find_element(By.LINK_TEXT, "File Monetization Request").click()
browser.find_element(By.ID, "vl_credit").send_keys("5")
browser.find_element(By.ID, "sl_credit").send_keys("1")
browser.find_element(By.ID, "btn_monetization_add").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.CSS_SELECTOR, "#monetization-data-table > tbody > tr > td:nth-child(4) > center > a").click()
browser.close()
DeleteMonetization = "#monetization-data-table > tbody > tr > td:nth-child(4) > center > button"
browser.find_element(By.CSS_SELECTOR, DeleteMonetization).click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()

# For Approval(Requests)
hover_element = browser.find_element(By.ID, "attendance")
time.sleep(5)
actions.move_to_element(hover_element).perform()
Requests = browser.find_element(By.CSS_SELECTOR, "#topnav-menu-content > ul > li:nth-child(3) > div > a:nth-child(2)")
Requests.click()
assert "For Approval" in title, "Title Mismatch"

browser.find_element(By.LINK_TEXT, "Leave").click()
browser.find_element(By.LINK_TEXT, "Travel Order").click()
browser.find_element(By.LINK_TEXT, "Overtime").click()

# DTR Processing
hover_element = browser.find_element(By.ID, "attendance")
time.sleep(5)
actions.move_to_element(hover_element).perform()
Processing = browser.find_element(By.LINK_TEXT, "DTR Processing")
Processing.click()
assert "DTR Processing" in title, "Title Mismatch"

table = browser.find_element(By.ID, "users-data-table")
headings = table.find_elements(By.TAG_NAME, "th")
expected_headings = ["Employee", "Remarks"]
heading_texts = [headings[1].text, headings[2].text]
assert heading_texts == expected_headings, "Title Mismatch"

checkboxes = table.find_elements(By.NAME, "userid[]")
checkboxes[2].click()

browser.find_element(By.ID, "btnProcess").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Ok").click()
browser.find_element(By.LINK_TEXT, "Revert DTR Process").click()

# Leave Records
hover_element = browser.find_element(By.ID, "attendance")
time.sleep(5)
actions.move_to_element(hover_element).perform()
LeaveRecords = browser.find_element(By.LINK_TEXT, "Leave Records")
LeaveRecords.click()
assert "Leave Records" in title, "Title Mismatch"

table1 = browser.find_element(By.ID, "leaves-data-table")
headings1 = table.find_elements(By.TAG_NAME, "th")
expected_headings1 = ["PERIOD", "PARTICULARS", "VACATION LEAVE", "SICK LEAVE", "UNAUTHORIZED ABSENCE"]
heading_texts1 = [headings1[0].text, headings1[1].text, headings1[2].text, headings1[3].text, headings1[4].text]
assert heading_texts1 == expected_headings1, "Title Mismatch"

browser.find_element(By.ID, "btnPrintLeaveRecord").click()
FromMonth = browser.find_element(By.ID, "fromMon")
StartMonth = Select(FromMonth)
StartMonth.select_by_visible_text("January")
ToMonth = browser.find_element(By.ID, "toMon")
EndMonth = Select(ToMonth)
EndMonth.select_by_visible_text("December")

FromYear = browser.find_element(By.ID, "fromYear")
StartYr = Select(FromYear)
StartYr.select_by_visible_text("2023")
ToYear = browser.find_element(By.ID, "toYear")
EndYr = Select(ToYear)
EndYr.select_by_visible_text("2024")

browser.find_element(By.LINK_TEXT, "Print").click()
browser.switch_to.window(browser.window_handles[1])
browser.close()
browser.find_element(By.LINK_TEXT, "Close").click()

Employee = browser.find_element(By.ID, "selectEmployee")
selectEmployee = Select(Employee)
selectEmployee.select_by_index(0)

Year = browser.find_element(By.ID, "s_year")
selectYear = Select(Year)
selectYear.select_by_visible_text("2024")

Month = browser.find_element(By.ID, "s_mon")
selectMonth = Select(Month)
selectMonth.select_by_visible_text("May")
