
# TASK #5: Prepare Automation test cases for Employees Info Tab
# Duration: 29/07/2024   -   2/8/2024
# Written by: ROMEL ANDREI M. CLIMACOSA
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import Select
from login import login



chrome_driver_path = r'C:\Users\user\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path))


driver.maximize_window()

driver.get("http://10.10.99.4/login")

login(driver, "hr_officer@pcaarrd.dost.gov.ph", "qweasdzxc")

nav_bar_item = (WebDriverWait(driver, 10).until
   (EC.visibility_of_element_located((By.XPATH, "//html/body/div[2]/header[2]/div/div[1]/div[2]/nav/div/ul/li[2]/a"))))

nav_bar_item.click()

try:
        filter_element = WebDriverWait(driver, 10).until(
           EC.presence_of_element_located((By.ID, "filter"))
        )
        filter_element.click()

except UnexpectedAlertPresentException as e:
   # Handle the alert that appears
    alert = driver.switch_to.alert
    print(f"An unexpected alert appeared: {alert.text}")
    alert.accept()

#----------------------TEST CASE#1-------------------------------

dropdown_element= driver.find_element(By.ID, "filter")
dropdown_element.click()

select = Select(dropdown_element)

expected_options = [
        "Show All",
        "Active",
        "Inactive",
        "Posthumous",
        "Promote",
        "Resign",
        "Retired",
        "Study Leave",
        "Transfer"
    ]

#check if they match the expected options
actual_options = [option.text for option in select.options]

if actual_options == expected_options:
    print("TEST CASE# 1 - PASSED: The options are correct.")
else:
    print("TEST CASE# 1 - FAILED: The options are incorrect.")
    print(f"Expected: {expected_options}")
    print(f"Actual: {actual_options}")

#-------------------------Assert Header Label-----------------------
words_to_check = ["Status", "Name of Employee", "Age", "Office", "Place of Assignmnet", "Plantilla No.", "SG", "Action"]

for word in words_to_check :
    try:
        header_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,  "/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/table/thead"))
        )
        assert header_element.is_displayed(), f"'{word}' is not displayed in the table header"
        print(f"                    {word} is correctly displayed.")
    except Exception as e:
        print(f"Error: {e}")
#------------------------Assert Search Label-------------------------
try:
    search = driver.find_element(By.XPATH, '//*[@id="tbl_empinfo_filter"]/label').text
    assert search == 'Search:', 'Incorrect label name'
    print("Search Label")
except Exception as e:
    print(f'Error: {e}')

#-----------------------Assert Table Length--------------------------
try:
    table_length= driver.find_element(By.XPATH, '//*[@id="tbl_empinfo_length"]/label')
    label_text = table_length.text.strip()

    assert "Show" in label_text, 'The label does not contain "Show"'
    assert "entries" in label_text, 'The label does not contain "entries"'
    print('Correct Table Length label')
except Exception as e:
    print(f'Errorr: {e}')
#------------------------TEST CASE#2-9------------------------------

test_cases = [
    ("ACD", "normal"),                                        # STRING (Positive Testing)
    ("PCAANRRDB-A2-45-2011", "normal"),      # VARCHAR (Positive Testung)
    ("Ñ", "normal"),                                             #  "Ñ" (Positive Testing)
    ("-", "normal"),                                              # SPECIAL CHARACTER (Positive Testing)
    ("   Account", "normal"),                               # SPACE + STRING (Positive Testing)
    ("   FAD    ", "normal"),                                 # SPACE+ STRING + SPACE (Positive Testing)
    ("        ", "error"),                                          # SPACE (Negative Testing)
    ("", "error")                                                   # EMPTY (Negative TestingT)
]

def results_are_displayed():
    try:
        driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/table/tbody")
        return True
    except:
        return False

def verify_no_change():
    try:
        driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div")
        return True
    except:
        return False

for index, (keyword, expected) in enumerate(test_cases, start=2):
    output_message = f"TEST CASE# {index} - "

    search_input = driver.find_element(By.XPATH, "//html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/label/input")

    search_input.clear()                          #clear any existing text in the input
    search_input.send_keys(keyword)    #input the search keyword

    results_displayed = results_are_displayed()
    verify = verify_no_change()

    # Check the results based on expected outcomes
    if expected == "normal":
        if results_displayed:
            try:
                employee_items = driver.find_elements(By.XPATH,"//html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/table/tbody")
                keyword_found = any(keyword.strip().lower() in item.text.lower() for item in employee_items)
                if keyword_found:
                    print(f"{output_message}PASSED: The keyword '{keyword}' is valid.")
                else:
                    print(f"{output_message}FAILED: The keyword '{keyword}' was not found in the results but considered valid")
            except Exception as e:
                print(f"{output_message}FAILED: The keyword '{keyword}' is valid but encountered an issue while verifying results. Error: {e}")
        else:
            print(f"{output_message}FAILED: The keyword '{keyword}' is not valid.")
    elif expected == "error":
        if verify:
            print(f"{output_message}PASSED: '{keyword}', displays All information available as NO filter/parameter specified.")
        else:
            print(f"{output_message}FAILED: '{keyword}', Error ")
# ----------------------TEST CASE#10---------------------------
#pds view button
driver.find_element(By.CSS_SELECTOR, ".btn.btn-soft-primary.small-button.view-pds-btn").click()

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
if len(driver.window_handles) == 2:
        print("TEST CASE# 10- PASSED: System displayed the PDS in PDF format.")
else:
        print("TEST CASE# 10- FAILED: Error")
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])

#----------------------TEST CASE#11----------------------------
#pds edit button
edit = driver.find_element(By.CSS_SELECTOR, ".btn.btn-soft-primary.small-button.edit-pds-btn")
assert edit.is_displayed(), 'Edit button is displayed'
assert edit.is_enabled(), 'Edit button is enabled'
edit.click()
try:
    # Wait for an expected element on the edit page    (title)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[1]/div[1]/h5")))
    print("TEST CASE# 11- PASSED: System proceed to the Edit PDF page.")
except:
    print("TEST CASE# 11- PASSED: Error")
driver.back()

#----------------------TEST CASE#12----------------------------
#201 file upload
try:
    upload = driver.find_element(By.XPATH, '//*[@id="tbl_empinfo"]/tbody/tr[1]/td[9]/center/a[3]')
    assert upload.is_displayed(), 'Upload button is displayed'
    assert upload.is_enabled(), 'Upload button is enabled'
    upload.click()
except Exception as e:
    print(f'Error:{e}')
try:
    # Wait for an expected element on the 201 files page (appointment)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "appointment")))
    print("TEST CASE# 12- PASSED: System proceed to upload 201 files page.")
except:
    print("TEST CASE# 12- FAILED: Error")
driver.back()
#--------------------TEST CASE#13------------------------------

try:
    indicator = driver.find_element(By.XPATH, "//*[@id='tbl_empinfo_info']")
    print("TEST CASE# 13- PASSED: Page Indicator is displayed.")
except:
    print("TEST CASE# 13- FAILED: The Page Indicator is NOT displayed.")

#---------------------TEST CASE#14------------------------------

try:
    pagination_element = driver.find_element(By.XPATH, "//*[@id='tbl_empinfo_wrapper']/div[3]/div[2]")
    print("TEST CASE# 14- PASSED: The Pagination is displayed.")
except Exception as e:
    print("TEST CASE# 14- FAILED: The Pagination is NOT displayed.")


time.sleep(20)