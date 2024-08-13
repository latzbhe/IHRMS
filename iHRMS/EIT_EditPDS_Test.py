from login import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
from selenium.common.exceptions import TimeoutException, NoSuchElementException

chrome_driver_path = r'C:\Users\user\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path))
driver.maximize_window()

driver.get("http://10.10.99.4/login")
login(driver, "hr_officer@pcaarrd.dost.gov.ph", "qweasdzxc")

driver.find_element(By.XPATH, "//html/body/div[2]/header[2]/div/div[1]/div[2]/nav/div/ul/li[2]/a").click()
try:
    filter_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "filter")))
    filter_element.click()
except UnexpectedAlertPresentException as e:
    alert = driver.switch_to.alert
    print(f"An unexpected alert appeared: {alert.text}")
    alert.accept()

driver.find_element(By.CSS_SELECTOR, ".btn.btn-soft-primary.small-button.edit-pds-btn").click()
# -----------------------------------------------------------------------------------------------------------------------------------------------
driver.find_element(By.ID, "printPDSButton").click()

WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
if len(driver.window_handles) == 2:
    print("System displayed the PDS in PDF format.")
else:
    print("Error")
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])
try:
    draft = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div[1]/div[1]/div[2]/h5/span').text
    assert draft == 'Draft', 'Shows Finalized'
except Exception as e:
    print(f"Error: {e}")
# -----------------------------------------------------------------------------------------------------------------------------------------------
# ASSERT NAV TAB
try:
    page_title = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div[1]/div[1]/div[1]/h5').text
    assert page_title == 'Edit Personal Data Sheet', 'Page Title error'
except Exception as e:
    print(f"Error: {e}")
try:
    nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[1]/a/i")
    navi_tab = driver.find_element(By.XPATH,
                                   '//*[@id="layout-wrapper"]/div[2]/div/div[1]/div[2]/div/ul/li[1]/a/span').text
    assert navi_tab == 'Part 1', 'Incorrect label'
    assert nav_tab.is_displayed(), 'Part1 button is not displayed'
    assert nav_tab.is_enabled(), 'Part1 button is not working'

    nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[2]/a")
    navi_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[2]/a").text
    assert navi_tab == 'Part 2', 'Incorrect Label'
    assert nav_tab.is_displayed(), 'Part 2 is not displayed'
    assert nav_tab.is_enabled(), 'Part 2 is not working'

    nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[3]/a")
    navi_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[3]/a").text
    assert navi_tab == 'Part 3', 'Incorrect Label'
    assert nav_tab.is_displayed(), 'Part 3 is not displayed'
    assert nav_tab.is_enabled(), 'Part 3 is not working'

    nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[4]/a")
    navi_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[4]/a").text
    assert navi_tab == 'Part 4', 'Incorrect Label'
    assert nav_tab.is_displayed(), 'Part 4 is not displayed'
    assert nav_tab.is_enabled(), 'Part 4 is not working'

    nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[5]/a")
    navi_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[5]/a").text
    assert navi_tab == 'Work Experience Sheet', 'Incorrect Label'
    assert nav_tab.is_displayed(), 'Work Experience Sheetis not displayed'
    assert nav_tab.is_enabled(), 'Work Experience Sheet is not working'

    nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[6]/a")
    navi_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[6]/a").text
    assert navi_tab == 'Attachments', 'Incorrect Label'
    assert nav_tab.is_displayed(), 'Attachment is not displayed'
    assert nav_tab.is_enabled(), 'Attachment is not working'

except Exception as e:
    print(f"Error: {e}")
# -------------------PART 1-----------------------
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="table2"]/tbody[1]'))
    )

    actual_text = element.text.strip()
    expected_items = ["CS Form No. 212", "Revised 2017", "PERSONAL DATA SHEET",
                      "WARNING: Any misrepresentation made in the Personal Data Sheet and the Work Experience Sheet shall cause the filing of administrative/criminal case/s against the person concerned.",
                      "READ THE ATTACHED GUIDE TO FILLING OUT THE PERSONAL DATA SHEET (PDS) BEFORE ACCOMPLISHING THE PDS FORM.",
                      "Print legibly. Tick appropriate boxes (☐) and use separate sheet if necessary. Indicate N/A if not applicable. DO NOT ABBREVIATE.",
                      "(Do not fill up. For CSC use only)"]

    for item in expected_items:
        assert item in actual_text, f"Expected item '{item}' not found in text '{actual_text}'"

    print("All expected words and numbers are present. ")

except Exception as e:
    print(f"An error occurred: {e}")
# -------------ASSERT LABELS-------------------------------------
try:
    assert "2. SURNAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[7]/td[1]').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'1:{e}')
try:
    assert "FIRST NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[8]/td[1]').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'2: {e}')
try:
    assert "MIDDLE NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[9]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'3:{e}')
try:
    assert "3. DATE OF BIRTH".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[10]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'4:{e}')
try:
    assert "4. PLACE OF BIRTH".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[11]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'5: {e}')
try:
    assert "5. SEX".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[12]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'6: {e}')
try:
    assert "6. CIVIL STATUS".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[13]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'7: {e}')
try:
    assert "7. HEIGHT (m)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[15]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'8: {e}')
try:
    assert "8. WEIGHT (kg)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[16]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'9: {e}')

try:
    assert "9. BLOOD TYPE".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[17]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'10: {e}')
try:
    assert "10. GSIS ID NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[18]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'11: {e}')
try:
    assert "11. PAG-IBIG ID NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[19]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'12: {e}')
try:
    assert "13. SSS NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[21]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'13: {e}')
try:
    assert "12. PHILHEALTH NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[20]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'14: {e}')
try:
    assert "14. TIN NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[22]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'15: {e}')
try:
    assert "15. AGENCY EMPLOYEE NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[23]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'16: {e}')
try:
    assert "16. CITIZENSHIP".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[10]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'17: {e}')
try:
    assert "17. RESIDENTIAL ADDRESS".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[13]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'18: {e}')
try:
    assert "ZIP CODE".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[16]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'19: {e}')

try:
    assert "18. PERMANENT ADDRESS".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[17]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'20: {e}')
try:
    assert "ZIP CODE".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[20]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'22: {e}')
try:
    assert "19. TELEPHONE NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[21]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'23: {e}')
try:
    assert "	20. MOBILE NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[22]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'24: {e}')
try:
    assert ("21. EMAIL ADDRESS (if any)").strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[23]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'25: {e}')
try:
    assert "22. SPOUSE'S SURNAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[25]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'26: {e}')
try:
    assert "23. NAME OF CHILDREN ".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="children_tbody"]/tr/td[1]').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'27:{e}')
try:
    assert "FIRST NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[26]/td[1]').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'28: {e}')
try:
    assert "MIDDLE NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[27]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'29:{e}')
try:
    assert "OCCUPATION".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[28]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'30:{e}')
try:
    assert "EMPLOYER/BUSINESS NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[29]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'31: {e}')
try:
    assert "BUSINESS ADDRESS".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[30]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'32: {e}')
try:
    assert " TELEPHONE NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[31]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'33: {e}')
try:
    assert "24. FATHER'S SURNAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[32]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'34: {e}')
try:
    assert "FIRST NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[33]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'35: {e}')

try:
    assert "MIDDLE NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[34]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'36: {e}')
try:
    assert "25. MOTHER'S MAIDEN NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[35]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'37: {e}')
try:
    assert "SURNAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[36]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'38: {e}')
try:
    assert " FIRST NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[37]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'39: {e}')
try:
    assert "MIDDLE NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[38]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'40: {e}')
try:
    assert "26. LEVEL".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="educational_background_tbody"]/tr[2]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'41: {e}')
try:
    assert "NAME OF SCHOOL\n(Write in full)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="educational_background_tbody"]/tr[2]/td[2]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'42: {e}')
try:
    assert "BASIC EDUCATION/DEGREE/COURSE\n(Write in full)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="educational_background_tbody"]/tr[2]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'43: {e}')
try:
    assert "PERIOD OF ATTENDANCE".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="educational_background_tbody"]/tr[2]/td[4]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'44: {e}')
try:
    assert "HIGHEST LEVEL/ UNITS EARNED\n(if not graduated)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="educational_background_tbody"]/tr[2]/td[5]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'45: {e}')

try:
    assert "YEAR GRADUATED".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="educational_background_tbody"]/tr[2]/td[6]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'46: {e}')
try:
    assert "SCHOLARSHIP/\nACADEMIC\nHONORS\nRECEIVED".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="educational_background_tbody"]/tr[2]/td[7]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'47: {e}')
try:
    assert "SIGNATURE".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[3]/tr[2]/td/table/tbody/tr/td[1]/font').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'48: {e}')
try:
    assert "DATE".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[3]/tr[2]/td/table/tbody/tr/td[3]/font').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'49: {e}')
try:
    assert ("21. EMAIL ADDRESS (if any)").strip() in driver.find_element(
        By.XPATH,
        '//*[@id="table2"]/tbody[1]/tr[23]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'50: {e}')

try:
    element_xpaths = {
        '1': '//*[@id="surname"]',
        '2': '//*[@id="first_name"]',
        '3': '//*[@id="middle_name"]',
        '4': '//*[@id="date_of_birth"]',
        '64': '//*[@id="place_of_birth"]',
        '5': '//*[@id="name_extension"]',
        '6': '//*[@id="height"]',
        '7': '//*[@id="weight"]',
        '8': '//*[@id="gsis_id_number"]',
        '9': '//*[@id="pagibig_id_number"]',
        '10': '//*[@id="philhealth_number"]',
        '11': '//*[@id="sss_number"]',
        '12': '//*[@id="tin_number"]',
        '13': '//*[@id="agency_employee_number"]',
        '14': '//*[@id="residential_house_number"]',
        '15': '//*[@id="residential_street"]',
        '16': '//*[@id="residential_subdivision_village"]',
        '17': '//*[@id="residential_zip_code"]',
        '18': '//*[@id="permanent_house_number"]',
        '19': '//*[@id="permanent_street"]',
        '20': '//*[@id="permanent_subdivision_village"]',
        '21': '//*[@id="permanent_zip_code"]',
        '22': '//*[@id="telephone_number"]',
        '23': '//*[@id="mobile_number"]',
        '24': '//*[@id="email_address"]',
        '25': '//*[@id="residential_street"]',
        '26': '//*[@id="residential_subdivision_village"]',
        '27': '//*[@id="residential_subdivision_village"]',
        '28': '//*[@id="spouse_first_name"]',
        '29': '//*[@id="pagibig_id_number"]',
        '30': '//*[@id="philhealth_number"]',
        '31': '//*[@id="sss_number"]',
        '32': '//*[@id="tin_number"]',
        '33': '//*[@id="agency_employee_number"]',
        '34': '//*[@id="residential_house_number"]',
        '35': '//*[@id="residential_street"]',
        '36': '//*[@id="residential_subdivision_village"]',
        '37': '//*[@id="residential_subdivision_village"]',
        '38': '//*[@id="spouse_first_name"]',
        '39': '//*[@id="pagibig_id_number"]',
        '40': '//*[@id="philhealth_number"]',
        '41': '//*[@id="spouse_surname"]',
        '42': '//*[@id="spouse_first_name"]',
        '43': '//*[@id="spouse_name_extension"]',
        '44': '//*[@id="spouse_middle_name"]',
        '45': '//*[@id="spouse_occupation"]',
        '46': '//*[@id="spouse_employer_business"]',
        '47': '//*[@id="spouse_business_address"]',
        '48': '//*[@id="spouse_telephone_number"]',
        '49': '//*[@id="father_surname"]',
        '50': '//*[@id="father_first_name"]',
        '51': '//*[@id="father_name_extension"]',
        '52': '//*[@id="father_middle_name"]',
        '53': '//*[@id="mother_surname"]',
        '54': '//*[@id="mother_first_name"]',
        '55': '//*[@id="mother_middle_name"]',
        '56': '//*[@id="add_educational_background"]',
        '57': '//*[@id="school_level"]',
        '58': '//*[@id="educational_background_tbody"]/tr[4]/td[2]/input',
        '59': '//*[@id="educational_background_tbody"]/tr[4]/td[3]/input',
        '60': '//*[@id="educational_background_tbody"]/tr[4]/td[4]/select',
        '61': '//*[@id="highest_level_units_earned"]',
        '62': '//*[@id="year_graduated"]',
        '63': '//*[@id="educational_background_tbody"]/tr[4]/td[8]/input',
        '65': '//*[@id="agree_part1"]',
        '66': '//*[@id="pds-part1"]/center/button[1]',
        '67': '//*[@id="pds-part1"]/center/button[2]',
        '68': '//*[@id="spouse_telephone_number"]',
        '69': '//*[@id="father_surname"]',
        '70': '//*[@id="father_first_name"]',
        '71': '//*[@id="select2-residential_province-container"]',
        '72': '//*[@id="select2-permanent_province-container"]',

    }
    for element_name, xpath in element_xpaths.items():
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        assert element.is_displayed(), f'{element_name} is not displayed'
        assert element.is_enabled(), f'{element_name} is not enabled'
except Exception as e:
    print(f"Error with {element_name}: {e}")
# ----------------------------------------------------------------------------------------
# Assert Dropdown Menu for blood type
try:
    driver.find_element(By.XPATH, '//*[@id="blood_type"]')

    # Define the expected options
    expected_options = [
        "Select a Blood Type",
        "A Positive (A+)",
        "A Negative (A-)",
        "B Positive (B+)",
        "B Negative (B-)",
        "AB Positive (AB+)",
        "AB Negative (AB-)",
        "O Positive (O+)",
        "O Negative (O-)"
    ]

    try:
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "blood_type"))
        )
        select = Select(select_element)
    except TimeoutException:
        print("Dropdown element not found within the timeout period.")
        driver.quit()
        exit()

    options_text = [option.text for option in select.options]

except NoSuchElementException as e:
    print(f"An error occurred: {e}")

# -----------------------------------------------------------------------------------------
# RADIO BUTTONS
try:
    male_radio = driver.find_element(By.ID, 'male')
    female_radio = driver.find_element(By.ID, 'female')
    male_label = driver.find_element(By.XPATH, '//label[@for="male"]')
    female_label = driver.find_element(By.XPATH, '//label[@for="female"]')

    assert male_radio.is_displayed(), "Male radio button is not displayed"
    assert male_radio.is_enabled(), "Male radio button is not enabled"

    assert female_radio.is_displayed(), "Female radio button is not displayed"
    assert female_radio.is_enabled(), "Female radio button is not enabled"

    assert male_label.text == "Male", "Male label text is incorrect"
    assert female_label.text == "Female", "Female label text is incorrect"
except Exception as e:
    print(f'Error: {e}')

try:
    single_radio = driver.find_element(By.ID, 'civil_Single')
    married_radio = driver.find_element(By.ID, 'civil_Married')
    single_label = driver.find_element(By.XPATH, '//input[@id="civil_Single"]/following-sibling::font')
    married_label = driver.find_element(By.XPATH, '//input[@id="civil_Married"]/following-sibling::font')

    assert single_radio.is_displayed(), "Single radio button is not displayed"
    assert single_radio.is_enabled(), "Single radio button is not enabled"

    assert married_radio.is_displayed(), "Married radio button is not displayed"
    assert married_radio.is_enabled(), "Married radio button is not enabled"

    assert single_label.text.strip() == "Single", "Single label text is incorrect"
    assert married_label.text.strip() == "Married", "Married label text is incorrect"
except Exception as e:
    print(f'Error: {e}')
try:
    widowed_radio = driver.find_element(By.ID, 'civil_Widowed')
    separated_radio = driver.find_element(By.ID, 'civil_Separated')
    widowed_label = driver.find_element(By.XPATH, '//input[@id="civil_Widowed"]/following-sibling::font')
    separated_label = driver.find_element(By.XPATH, '//input[@id="civil_Separated"]/following-sibling::font')

    assert widowed_radio.is_displayed(), "Widowed radio button is not displayed"
    assert widowed_radio.is_enabled(), "Widowed radio button is not enabled"

    assert separated_radio.is_displayed(), "Separated radio button is not displayed"
    assert separated_radio.is_enabled(), "Separated radio button is not enabled"

    assert widowed_label.text.strip() == "Widowed", "Widowed label text is incorrect"
    assert separated_label.text.strip() == "Separated", "Separated label text is incorrect"
except Exception as e:
    print(f'Error: {e}')
time.sleep(5)
action = ActionChains(driver)
try:
    filipino_radio = driver.find_element(By.ID, 'filipino')
    dual_radio = driver.find_element(By.ID, 'dual_citizenship')
    by_birth_radio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'by_birth'))
    )
    by_naturalization_radio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'by_naturalization'))
    )

    filipino_label = driver.find_element(By.XPATH, '//label[@for="filipino"]')
    dual_label = driver.find_element(By.XPATH, '//label[@for="dual_citizenship"]')
    by_birth_label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[@for="by_birth"]'))
    )
    by_naturalization_label = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[@for="by_naturalization"]'))
    )

    assert filipino_radio.is_displayed(), "Filipino radio button is not displayed"
    assert filipino_radio.is_enabled(), "Filipino radio button is not enabled"
    assert filipino_label.text.strip() == "Filipino", "Filipino label text is incorrect"

    assert dual_radio.is_displayed(), "Dual Citizenship radio button is not displayed"
    assert dual_radio.is_enabled(), "Dual Citizenship radio button is not enabled"
    assert dual_label.text.strip() == "Dual Citizenship", "Dual Citizenship label text is incorrect"

    time.sleep(5)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, dual_radio)
    action.move_to_element(dual_radio).click().perform()

    dual_options = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="table2"]/tbody[1]/tr[10]/td[4]/div[1]'))
    )
    citizenship_country_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="table2"]/tbody[1]/tr[10]/td[4]/div[2]/label'))
    )

    assert by_birth_radio.is_displayed(), "By birth radio button is not displayed"
    assert by_birth_radio.is_enabled(), "By birth radio button is not enabled"
    assert by_birth_label.text.strip() == "by birth", "by birth label text is incorrect"

    assert by_naturalization_radio.is_displayed(), "By naturalization radio button is not displayed"
    assert by_naturalization_radio.is_enabled(), "By naturalization radio button is not enabled"
    assert by_naturalization_label.text.strip() == "by naturalization", "by naturalization label text is incorrect"

    assert citizenship_country_input.is_displayed(), "By naturalization radio button is not displayed"
    assert citizenship_country_input.is_enabled(), "By naturalization radio button is not enabled"
    assert citizenship_country_input.text.strip() == "Pls. indicate country:", "by naturalization label text is incorrect"

    action.move_to_element(filipino_radio).click().perform()
    time.sleep(5)
    assert not dual_options.is_displayed(), "By dual citizenship options button is displayed even if  dual citizenship is not selected"
    assert not dual_options.is_enabled(), "By dual citizenshipoptions button is enabled even if  dual citizenship is not selected"

    assert not citizenship_country_input.is_displayed(), "By naturalization radio button is displayed even if  dual citizenship is not selected"
    assert not citizenship_country_input.is_enabled(), "By naturalization radio button is enabled even if  dual citizenship is not selected"

    print("Citizenship Radio Buttons passed.")

except Exception as e:
    print(f'Error: {e}')

try:

    time.sleep(3)
    actions = ActionChains(driver)

    disable = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/a[1]')
    actions.move_to_element(disable).click().perform()
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'blood_type')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    civil_others_radio = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'civil_Others'))
    )
    actions.move_to_element(target_element).perform()

    civil_status_others_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'civil_status_others'))
    )

    assert civil_others_radio.is_displayed(), "Civil Status radio button is not displayed"
    assert civil_others_radio.is_enabled(), "Civil Status radio button is not enabled"

    assert not civil_status_others_input.is_displayed(), "Text input 'Other Civil Status' should be hidden initially"
    actions.move_to_element(civil_others_radio).click().perform()

    civil_status_others_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'civil_status_others'))
    )

    assert civil_status_others_input.is_displayed(), "Text input 'Other Civil Status' is not displayed after clicking radio button"
    assert civil_status_others_input.is_enabled(), "Text input 'Other Civil Status' is not enabled"

    assert civil_status_others_input.get_attribute(
        "placeholder") == "Other Civil Status", "Text input placeholder is incorrect"

    single = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'civil_Single'))
    )
    action.move_to_element(single).click().perform()

    assert not civil_status_others_input.is_displayed(), "Text input is displayed even if 'Others' is not selected"
    assert not civil_status_others_input.is_enabled(), "Text input  is enabled even if 'Others' is not selected"

    print("Radio button and text input validation passed.")

except Exception as e:
    print(f'Error: {e}')

time.sleep(5)
# ----------------------------------------------------------------------------------------
# Other Buttons
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'add_children')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(5)
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_children"))
    )
    add_button.click()

    new_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="children_tbody"]/tr[2]'))
    )
    assert new_element.is_displayed() and new_element.is_displayed(), "Input boxes are not displayed and enabled after clicking the add button"

    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "delete-children"))
    )
    assert delete_button.is_displayed(), "Delete button is not visible."
    assert delete_button.is_enabled(), "Delete button is not enabled."
    delete_button.click()

    time.sleep(5)

    confirm_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[11]/div'))
    )
    assert confirm_message.is_displayed(), "Confirmation message is not displayed."

    confirmation_message_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-title"]'))
    ).text
    assert confirmation_message_title == 'Are you sure?', 'Wrong confirmation title message'

    confirmation_message_body = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert confirmation_message_body == 'You are about to delete this row. This action cannot be reverted!', 'Wrong confirmation body message'

    cancel_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[11]/div/div[6]/button[3]'))
    )
    assert cancel_button.is_displayed(), 'Cancel button is not displayed.'
    assert cancel_button.is_enabled(), 'Cancel button is not enabled.'

    yes_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div[6]/button[1]"))
    )
    assert yes_button.is_displayed(), 'Yes button is not displayed.'
    assert yes_button.is_enabled(), 'Yes button is not enabled.'
    action.move_to_element(yes_button).click().perform()

    comp_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[11]/div/h2'))
    ).text
    assert comp_message == 'Deleted!', 'Wrong completion title message'

    completion_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert completion_message == 'The row has been deleted.', 'Wrong completion message'

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div[6]/button[1]"))
    )
    assert ok_button.is_displayed(), 'OK button is not displayed.'
    assert ok_button.is_enabled(), 'OK button is not enabled.'
    action.move_to_element(ok_button).click().perform()

    print('Name of Children passed')
except Exception as e:
    print(f"Error: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.XPATH, '//*[@id="school_level"]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_educational_background"))
    )
    action.move_to_element(add_button).click().perform()

    new_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="educational_background_tbody"]/tr[9]'))
    )
    assert new_element.is_displayed() and new_element.is_displayed(), "Input boxes are not interactable after clicking the add button"

    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="educational_background_tbody"]/tr[9]/td[9]/button'))
    )
    assert delete_button.is_displayed(), "Delete button is not visible."
    assert delete_button.is_enabled(), "Delete button is not enabled."
    delete_button.click()

    time.sleep(5)

    confirm_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[11]/div'))
    )
    assert confirm_message.is_displayed(), "Confirmation message is not displayed."

    confirmation_message_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-title"]'))
    ).text
    assert confirmation_message_title == 'Are you sure?', 'Wrong confirmation title message'

    confirmation_message_body = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert confirmation_message_body == 'You are about to delete this row. This action cannot be reverted!', 'Wrong confirmation body message'

    cancel_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[11]/div/div[6]/button[3]'))
    )
    assert cancel_button.is_displayed(), 'Cancel button is not displayed.'
    assert cancel_button.is_enabled(), 'Cancel button is not enabled.'

    yes_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div[6]/button[1]"))
    )
    assert yes_button.is_displayed(), 'Yes button is not displayed.'
    assert yes_button.is_enabled(), 'Yes button is not enabled.'
    action.move_to_element(yes_button).click().perform()

    comp_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[11]/div/h2'))
    ).text
    assert comp_message == 'Deleted!', 'Wrong completion title message'

    completion_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert completion_message == 'The row has been deleted.', 'Wrong completion message'

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[11]/div/div[6]/button[1]"))
    )
    assert ok_button.is_displayed(), 'OK button is not displayed.'
    assert ok_button.is_enabled(), 'OK button is not enabled.'
    action.move_to_element(ok_button).click().perform()

    print('Education Background passed')
except Exception as e:
    print(f"Error: {e}")
try:
    action = ActionChains(driver)
    check_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'agree_part1')))
    assert check_box.is_displayed(), 'Not Displayed'
    assert check_box.is_enabled(), "Not Enabled'"
    time.sleep(5)
    action.move_to_element(check_box).perform()
    action.click(check_box).perform()
    time.sleep(5)
    assert check_box.is_selected(), "Checkbox was not checked after clicking."

    expected_name = "Ed E. Abshire"
    expected_date = datetime.now().strftime("%B %d, %Y")

    result_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'date_today_part1')))
    result_text = result_element.text.splitlines()

    assert result_text[0] == expected_name, f"Expected name '{expected_name}', but got '{result_text[0]}'"
    assert result_text[1] == expected_date, f"Expected date '{expected_date}', but got '{result_text[1]}'"
    time.sleep(5)
except Exception as e:
    print(f"31: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.XPATH, '//*[@id="pds-part1"]/center/button[1]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    save_button = driver.find_element(By.XPATH, '//*[@id="pds-part1"]/center/button[1]')
    assert save_button.is_displayed(), 'Not Displayed'
    assert save_button.is_enabled(), "Not Enabled'"
    assert "Save Draft".replace(" ", "") in save_button.text.replace(" ", ""), "Button text is incorrect"
    action.move_to_element(save_button).click().perform()
except Exception as e:
    print(f"Error: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.XPATH, '//*[@id="pds-part1"]/center/button[2]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    validation_button = driver.find_element(By.XPATH, '//*[@id="pds-part1"]/center/button[2]')
    assert validation_button.is_displayed(), 'Not Displayed'
    assert validation_button.is_enabled(), "Not Enabled'"
    assert "Validate & Finalize Part 1".replace(" ", "") in validation_button.text.replace(" ",
                                                                                           ""), "Button text is incorrect"
except Exception as e:
    print(f'Error: {e}')

# -------------------------------------------------------------------------------------------------------------------------------------------
print('-----PART 2-----')
driver.refresh()
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(3)
nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[2]/a")
nav_tab.click()

try:
    table_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'civil_service_eligibility_tbody'))
    )

    header_text = table_body.find_element(By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[1]/td/b/i').text
    assert "IV. CIVIL SERVICE ELIGIBILTY" in header_text, "Table header text is incorrect"

except Exception as e:
    print(f'Error: {e}')

try:
    assert "27. CAREER SERVICE/RA 1080 (BOARD/BAR) UNDER SPECIAL LAWS/CES/CSEE/".replace(" ",
                                                                                         "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[2]/td[1]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'1:{e}')
try:
    assert "BARANGAY ELIGIBILITY/DRIVER'S LICENSE".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[2]/td[1]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'2: {e}')
try:
    assert "RATING".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[2]/td[2]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'3:{e}')
try:
    assert " (If Applicable)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[2]/td[2]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'4:{e}')
try:
    assert "DATE OF EXAMINATION/ CONFERMENT".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[2]/td[3]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'5: {e}')
try:
    assert "PLACE OF EXAMINATION/CONFERMENT".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[2]/td[4]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'6: {e}')
try:
    assert "LICENSE (if applicable)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[2]/td[5]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'7: {e}')
try:
    assert "NUMBER".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[3]/td[1]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'8: {e}')
try:
    assert "DATE OF VALIDITY".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[3]/td[2]').text.replace(" ",
                                                                                         ""), "The text is not present in the element"
except AssertionError as e:
    print(f'9: {e}')

try:
    assert "V. WORK EXPERIENCE".replace(
        " ", "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[1]/td/b/i').text.replace(" ",
                                                                                ""), "The text is not present in the element"
except AssertionError as e:
    print(f'10: {e}')
try:
    assert "28. INCLUSIVE DATES (mm/dd/yyyy)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[2]/td[1]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'11: {e}')
try:
    assert "FROM".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[3]/td[1]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'12: {e}')
try:
    assert "TO".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[3]/td[2]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'13: {e}')
try:
    assert "POSITION TITLE\n(Write in full/Do not abbreviate)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[2]/td[2]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'14: {e}')
try:
    assert "DEPARTMENT/AGENCY/ OFFICE/COMPANY\n(Write in full/Do not abbreviate)".replace(" ",
                                                                                          "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[2]/td[3]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'15: {e}')
try:
    assert "MONTHLY SALARY".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[2]/td[4]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'16: {e}')
try:
    assert 'SALARY/JOB/PAY GRADE (if applicable) & STEP (Format "00-0")/\nINCREMENT'.replace(" ",
                                                                                             "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[2]/td[5]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'17: {e}')
try:
    assert "GOV'T SERVICE (Y/N)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="work_experience_tbody"]/tr[2]/td[7]').text.replace(" ",
                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'18: {e}')
try:
    assert "SIGNATURE".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="pds-part2"]/center/div/table/tbody[4]/tr[2]/td/table/tbody/tr/td[1]').text.replace(" ",
                                                                                                               ""), "The text is not present in the element"
except AssertionError as e:
    print(f'19: {e}')

# Buttons, Checkbox, and Input Boxes
# ------------------------------------------------------------------------------------------------------------------------
try:
    wait = WebDriverWait(driver, 20)
    add_button = driver.find_element(By.ID, 'add_civil_service_eligibility')
    assert add_button.is_displayed(), 'Not Displayed'
    assert add_button.is_enabled(), "Not Enabled"
    add_button.click()
    input_box = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[4]')))
    assert input_box.is_displayed(), "Input box is not visible"

except Exception as e:
    print(f"20: {e}")
try:
    wait = WebDriverWait(driver, 20)
    add_button = driver.find_element(By.ID, 'add_work_experience')
    assert add_button.is_displayed(), 'Not Displayed'
    assert add_button.is_enabled(), "Not Enabled"
    add_button.click()
    input_box = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="work_experience_tbody"]/tr[4]')))
    assert input_box.is_displayed(), "Input box is not visible"
except Exception as e:
    print(f"21: {e}")

wait = WebDriverWait(driver, 10)
try:
    driver.implicitly_wait(5)

    actions = ActionChains(driver)

    add_button = driver.find_element(By.ID, "add_civil_service_eligibility")
    actions.move_to_element(add_button).click().perform()

    eligibility_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='eligibility[]']")))
    assert eligibility_field.is_displayed(), 'Not Displayed'
    assert eligibility_field.is_enabled(), "Not Enabled'"
    rating_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='rating[]']")))
    assert rating_field.is_displayed(), 'Not Displayed'
    assert rating_field.is_enabled(), "Not Enabled'"
    date_of_exam_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='date_of_exam[]']")))
    assert date_of_exam_field.is_displayed(), 'Not Displayed'
    assert date_of_exam_field.is_enabled(), "Not Enabled'"
    place_of_exam_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='place_of_exam[]']")))
    assert place_of_exam_field.is_displayed(), 'Not Displayed'
    assert place_of_exam_field.is_enabled(), "Not Enabled'"
    license_number_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='license_number[]']")))
    assert license_number_field.is_displayed(), 'Not Displayed'
    assert license_number_field.is_enabled(), "Not Enabled'"
    date_of_validity_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='date_of_validity[]']")))
    assert date_of_validity_field.is_displayed(), 'Not Displayed'
    assert date_of_validity_field.is_enabled(), "Not Enabled'"

    time.sleep(5)
    delete_button = driver.find_element(By.XPATH, '//*[@id="civil_service_eligibility_tbody"]/tr[4]/td[7]/button')
    actions.move_to_element(delete_button).click().perform()
    modal = driver.find_element(By.CSS_SELECTOR, '.swal2-popup')

    yes_button = modal.find_element(By.CSS_SELECTOR, '.swal2-confirm')
    assert yes_button.is_displayed(), "The 'Yes, delete it!' button is not visible."

    cancel_button = modal.find_element(By.CSS_SELECTOR, '.swal2-cancel')
    assert cancel_button.is_displayed(), "The 'Cancel' button is not visible."
    assert cancel_button.is_enabled(), "The 'Cancel' button is not working."
    yes_button.click()

    modal = driver.find_element(By.CSS_SELECTOR, '.swal2-popup')

    success_message = modal.find_element(By.CSS_SELECTOR, '.swal2-title')
    assert success_message.is_displayed(), "The success message is not visible."

    ok_button = modal.find_element(By.CSS_SELECTOR, '.swal2-confirm')
    assert ok_button.is_displayed(), "The 'OK' button is not visible."

    ok_button.click()
    print('Conf & Comp Message Passed')
except TimeoutException as e:
    print(f'26:{e}')

except AssertionError as e:
    print(f'26:{e}')

except Exception as e:
    print(f'26:{e}')

try:
    actions = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'inclusive_date_from_2')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    add_button = driver.find_element(By.ID, "add_work_experience")
    actions.move_to_element(add_button).click().perform()
    wait = WebDriverWait(driver, 10)

    from_date_input = wait.until(EC.visibility_of_element_located((By.ID, 'inclusive_date_from_2')))
    assert from_date_input.is_displayed(), "FROM date input is not displayed"
    assert from_date_input.is_enabled(), "FROM date input is not enabled"

    to_date_input = wait.until(EC.visibility_of_element_located((By.ID, "inclusive_date_to_2")))
    assert to_date_input.is_displayed(), "TO date input is not displayed"
    assert to_date_input.is_enabled(), "TO date input is not enabled"
except Exception as e:
    print(f'27: {e}')
try:
    wait = WebDriverWait(driver, 10)
    position_title_input = wait.until(EC.visibility_of_element_located((By.ID, "position_title")))
    assert position_title_input.is_displayed(), "Position Title input is not displayed"
    assert position_title_input.is_enabled(), "Position Title input is not enabled"

    office_input = wait.until(EC.visibility_of_element_located((By.ID, "agency_company")))
    assert office_input.is_displayed(), "Office input is not displayed"
    assert office_input.is_enabled(), "Office input is not enabled"

    salary_input = wait.until(EC.visibility_of_element_located((By.ID, "monthly_salary")))
    assert salary_input.is_displayed(), "Salary input is not displayed"
    assert salary_input.is_enabled(), "Salary input is not enabled"

    salary_grade_input = wait.until(EC.visibility_of_element_located((By.ID, "salary_grade")))
    assert salary_grade_input.is_displayed(), "Salary Grade input is not displayed"
    assert salary_grade_input.is_enabled(), "Salary Grade input is not enabled"

    appointment_status_input = wait.until(EC.visibility_of_element_located((By.ID, "status_of_appointment")))
    assert appointment_status_input.is_displayed(), "Appointment Status input is not displayed"
    assert appointment_status_input.is_enabled(), "Appointment Status input is not enabled"

    government_service_dropdown = wait.until(EC.visibility_of_element_located((By.ID, "is_government_service")))
    assert government_service_dropdown.is_displayed(), "Gov't Service dropdown is not displayed"
    assert government_service_dropdown.is_enabled(), "Gov't Service dropdown is not enabled"

except AssertionError as e:
    print(f'28: {e}')

try:
    # dropdown element sheck
    YN = driver.find_element(By.ID, 'is_government_service')

    expected_options = [
        "Y",
        "N",
    ]

    select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "is_government_service"))
    )
    select = Select(select_element)

    options_text = [option.text for option in select.options]
    time.sleep(5)
    assert YN.is_displayed() and YN.is_enabled(), 'The dropdown menu is not interactable'
    print('Y/N is displayed and enabled')
except Exception as e:
    print(f'29: {e}')

try:
    actions = ActionChains(driver)
    delete_button = driver.find_element(By.XPATH, '//*[@id="work_experience_tbody"]/tr[4]/td[9]/button')
    actions.move_to_element(delete_button).click().perform()
    modal = driver.find_element(By.CSS_SELECTOR, '.swal2-popup')

    yes_button = modal.find_element(By.CSS_SELECTOR, '.swal2-confirm')
    assert yes_button.is_displayed(), "The 'Yes, delete it!' button is not visible."

    cancel_button = modal.find_element(By.CSS_SELECTOR, '.swal2-cancel')
    assert cancel_button.is_displayed(), "The 'Cancel' button is not visible."
    assert cancel_button.is_enabled(), "The 'Cancel' button is not working."
    yes_button.click()

    modal = driver.find_element(By.CSS_SELECTOR, '.swal2-popup')

    success_message = modal.find_element(By.CSS_SELECTOR, '.swal2-title')
    assert success_message.is_displayed(), "The success message is not visible."

    ok_button = modal.find_element(By.CSS_SELECTOR, '.swal2-confirm')
    assert ok_button.is_displayed(), "The 'OK' button is not visible."

    ok_button.click()
    print('Conf & Comp Message Passed')
except Exception as e:
    print(f"32: {e}")
try:
    action = ActionChains(driver)
    check_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'agree_part2')))
    assert check_box.is_displayed(), 'Not Displayed'
    assert check_box.is_enabled(), "Not Enabled'"

    action.move_to_element(check_box).perform()
    action.click(check_box).perform()
    time.sleep(5)
    assert check_box.is_selected(), "Checkbox was not checked after clicking."

    expected_name = "Ed E. Abshire"
    expected_date = datetime.now().strftime("%B %d, %Y")

    result_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'date_today_part2')))
    result_text = result_element.text.splitlines()

    assert result_text[0] == expected_name, f"Expected name '{expected_name}', but got '{result_text[0]}'"
    assert result_text[1] == expected_date, f"Expected date '{expected_date}', but got '{result_text[1]}'"
    time.sleep(3)
    check_box.click()
    assert not check_box.is_selected(), "Checkbox was not unchecked after clicking again."
except Exception as e:
    print(f"31: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.XPATH, '//*[@id="pds-part2"]/center/button[1]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    save_button = driver.find_element(By.XPATH, '//*[@id="pds-part2"]/center/button[1]')
    assert save_button.is_displayed(), 'Not Displayed'
    assert save_button.is_enabled(), "Not Enabled'"
    assert "Save Draft".replace(" ", "") in save_button.text.replace(" ", ""), "Button text is incorrect"
    action.move_to_element(save_button).click().perform()
except Exception as e:
    print(f"33: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.XPATH, '//*[@id="pds-part2"]/center/button[2]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    validation_button = driver.find_element(By.XPATH, '//*[@id="pds-part2"]/center/button[2]')
    assert validation_button.is_displayed(), 'Not Displayed'
    assert validation_button.is_enabled(), "Not Enabled'"
    assert "Validate & Finalize Part 2".replace(" ", "") in validation_button.text.replace(" ",
                                                                                           ""), "Button text is incorrect"
except Exception as e:
    print(f'34: {e}')

# PART#3---------------------------------------------------------------------------------------
print("-----PART 3-----")

nav_tab = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div[1]/div[2]/div/ul/li[3]/a/span")
nav_tab.click()

try:
    table_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'voluntary_work_tbody'))
    )

    header_text = table_body.find_element(By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[1]/td/b/i').text
    assert "VI. VOLUNTARY WORK OR INVOLVEMENT IN CIVIC/NON-GOVERNMENT/PEOPLE/VOLUNTARY ORGANIZATION/S" in header_text, "Table header text is incorrect"

    add_button = table_body.find_element(By.ID, 'add_voluntary_work')
    assert add_button.is_displayed(), "Add button is not displayed"
    assert add_button.is_enabled(), "Add button is not enabled"

except Exception as e:
    print(f'Error: {e}')

try:
    assert "29. NAME & ADDRESS OF ORGANIZATION\n(Write in full)".replace(" ",
                                                                         "") in driver.find_element(
        By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[2]/td[1]').text.replace(" ",
                                                                              ""), "The text is not present in the element"
except AssertionError as e:
    print(f'1:{e}')
try:
    assert "INCLUSIVE DATES\n(mm/dd/yyyy)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[2]/td[2]').text.replace(" ",
                                                                              ""), "The text is not present in the element"
except AssertionError as e:
    print(f'2: {e}')
try:
    assert "FROM".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[3]/td[1]').text.replace(" ",
                                                                              ""), "The text is not present in the element"
except AssertionError as e:
    print(f'3:{e}')
try:
    assert "TO".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[3]/td[2]').text.replace(" ",
                                                                              ""), "The text is not present in the element"
except AssertionError as e:
    print(f'4:{e}')
try:
    assert "NUMBER OF HOURS".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[2]/td[3]').text.replace(" ",
                                                                              ""), "The text is not present in the element"
except AssertionError as e:
    print(f'5: {e}')
try:
    assert "POSITION / NATURE OF WORK".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[2]/td[4]').text.replace(" ",
                                                                              ""), "The text is not present in the element"
except AssertionError as e:
    print(f'6: {e}')
try:
    header_text = driver.find_element(By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[2]/td').text
    assert "VII. LEARNING AND DEVELOPMENT (L&D) INTERVENTIONS/TRAINING PROGRAMS ATTENDED" in header_text, "Table header text is incorrect"

except AssertionError as e:
    print(f'7: {e}')
try:
    assert "30. TITLE OF LEARNING AND DEVELOPMENT INTERVENTIONS/TRAINING PROGRAMS\n(Write in full)".replace(" ",
                                                                                                            "") in driver.find_element(
        By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[3]/td[1]').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'8: {e}')
try:
    assert "INCLUSIVE DATES OF ATTENDANCE\n(mm/dd/yyyy)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[3]/td[2]').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'9: {e}')

try:
    assert "From".replace(
        " ", "") in driver.find_element(
        By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[4]/td[1]').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'10: {e}')
try:
    assert "To".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[4]/td[2]').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'11: {e}')
try:
    assert "NUMBER OF HOURS".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[3]/td[3]').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'12: {e}')
try:
    assert "Type of LD\n(Managerial/\nSupervisory/\nTechnical/etc)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[3]/td[4]').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'13: {e}')
try:
    assert "CONDUCTED/SPONSORED BY\n(Write in full)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[3]/td[5]').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'14: {e}')
try:
    assert "VIII. OTHER INFORMATION".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="other_information_tbody"]/tr[1]/td/b/i').text.replace(" ",
                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'15: {e}')
try:
    assert "31. SPECIAL SKILLS and HOBBIES".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="other_information_tbody"]/tr[2]/td[1]').text.replace(" ",
                                                                                 ""), "The text is not present in the element"
except AssertionError as e:
    print(f'16: {e}')
try:
    assert '32. NON-ACADEMIC DISTINCTIONS/RECOGNITON (Write in full)'.replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="other_information_tbody"]/tr[2]/td[2]').text.replace(" ",
                                                                                 ""), "The text is not present in the element"
except AssertionError as e:
    print(f'17: {e}')
try:
    assert "33. MEMBERSHIP IN ASSOCIATION/ORGANIZATION (Write in full)".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="other_information_tbody"]/tr[2]/td[3]').text.replace(" ",
                                                                                 ""), "The text is not present in the element"
except AssertionError as e:
    print(f'18: {e}')
try:
    assert "SIGNATURE".replace(" ", "") in driver.find_element(
        By.XPATH, '//*[@id="pds-part3"]/center/div/table/tbody[5]/tr[2]/td[1]/font').text.replace(" ",
                                                                                                  ""), "The text is not present in the element"
except AssertionError as e:
    print(f'19: {e}')

# Buttons, Checkboxes, Input Boxes------------------------------------------------------------------------------------------------------------
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'agree_part3')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    wait = WebDriverWait(driver, 10)

    check_box = wait.until(EC.visibility_of_element_located((By.ID, 'agree_part3')))
    assert check_box.is_displayed(), 'Not Displayed'
    assert check_box.is_enabled(), "Not Enabled'"

    action.move_to_element(check_box).perform()
    action.click(check_box).perform()
    time.sleep(3)
    assert check_box.is_selected(), "Checkbox was not checked after clicking."

    expected_name = "Ed E. Abshire"
    expected_date = datetime.now().strftime("%B %d, %Y")

    result_element = wait.until(EC.visibility_of_element_located((By.ID, 'date_today_part3')))
    result_text = result_element.text.splitlines()

    assert result_text[0] == expected_name, f"Expected name '{expected_name}', but got '{result_text[0]}'"
    assert result_text[1] == expected_date, f"Expected date '{expected_date}', but got '{result_text[1]}'"
    time.sleep(3)

except Exception as e:
    print(f"23: {e}")

try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'add_voluntary_work')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_voluntary_work"))
    )
    action.move_to_element(add_button).click().perform()

    new_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[5]'))
    )
    assert new_element.is_displayed() and new_element.is_displayed(), "Input boxes are not interactable after clicking the add button"

    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[5]/td[6]/button'))
    )
    assert delete_button.is_displayed(), "Delete button is not visible."
    assert delete_button.is_enabled(), "Delete button is not enabled."
    delete_button.click()

    time.sleep(5)

    confirm_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[12]/div'))
    )
    assert confirm_message.is_displayed(), "Confirmation message is not displayed."

    confirmation_message_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-title"]'))
    ).text
    assert confirmation_message_title == 'Are you sure?', 'Wrong confirmation title message'

    confirmation_message_body = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert confirmation_message_body == 'You are about to delete this row. This action cannot be reverted!', 'Wrong confirmation body message'

    cancel_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[12]/div/div[6]/button[3]'))
    )
    assert cancel_button.is_displayed(), 'Cancel button is not displayed.'
    assert cancel_button.is_enabled(), 'Cancel button is not enabled.'

    yes_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[12]/div/div[6]/button[1]"))
    )
    assert yes_button.is_displayed(), 'Yes button is not displayed.'
    assert yes_button.is_enabled(), 'Yes button is not enabled.'
    action.move_to_element(yes_button).click().perform()

    comp_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[12]/div/h2'))
    ).text
    assert comp_message == 'Deleted!', 'Wrong completion title message'

    completion_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert completion_message == 'The row has been deleted.', 'Wrong completion message'

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[12]/div/div[6]/button[1]"))
    )
    assert ok_button.is_displayed(), 'OK button is not displayed.'
    assert ok_button.is_enabled(), 'OK button is not enabled.'
    action.move_to_element(ok_button).click().perform()

    print('Voluntary Work passed')
except Exception as e:
    print(f"C-Error: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'add_trainings_attended')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_trainings_attended"))
    )
    action.move_to_element(add_button).click().perform()

    new_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[6]'))
    )
    assert new_element.is_displayed() and new_element.is_displayed(), "Input boxes are not interactable after clicking the add button"

    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[6]/td[7]/button'))
    )
    assert delete_button.is_displayed(), "Delete button is not visible."
    assert delete_button.is_enabled(), "Delete button is not enabled."
    delete_button.click()

    time.sleep(5)

    confirm_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[14]/div'))
    )
    assert confirm_message.is_displayed(), "Confirmation message is not displayed."

    confirmation_message_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-title"]'))
    ).text
    assert confirmation_message_title == 'Are you sure?', 'Wrong confirmation title message'

    confirmation_message_body = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert confirmation_message_body == 'You are about to delete this row. This action cannot be reverted!', 'Wrong confirmation body message'

    cancel_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[14]/div/div[6]/button[3]'))
    )
    assert cancel_button.is_displayed(), 'Cancel button is not displayed.'
    assert cancel_button.is_enabled(), 'Cancel button is not enabled.'

    yes_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[14]/div/div[6]/button[1]"))
    )
    assert yes_button.is_displayed(), 'Yes button is not displayed.'
    assert yes_button.is_enabled(), 'Yes button is not enabled.'
    action.move_to_element(yes_button).click().perform()

    comp_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[14]/div/h2'))
    ).text
    assert comp_message == 'Deleted!', 'Wrong completion title message'

    completion_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert completion_message == 'The row has been deleted.', 'Wrong completion message'

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[14]/div/div[6]/button[1]"))
    )
    assert ok_button.is_displayed(), 'OK button is not displayed.'
    assert ok_button.is_enabled(), 'OK button is not enabled.'
    action.move_to_element(ok_button).click().perform()

    print('L&D passed')
except Exception as e:
    print(f"C-Error: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'add_other_information')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_other_information"))
    )
    action.move_to_element(add_button).click().perform()

    new_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="other_information_tbody"]/tr[3]'))
    )
    assert new_element.is_displayed() and new_element.is_displayed(), "Input boxes are not interactable after clicking the add button"

    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="other_information_tbody"]/tr[3]/td[4]/button'))
    )
    assert delete_button.is_displayed(), "Delete button is not visible."
    assert delete_button.is_enabled(), "Delete button is not enabled."
    delete_button.click()

    time.sleep(5)

    confirm_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[14]/div'))
    )
    assert confirm_message.is_displayed(), "Confirmation message is not displayed."

    confirmation_message_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-title"]'))
    ).text
    assert confirmation_message_title == 'Are you sure?', 'Wrong confirmation title message'

    confirmation_message_body = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert confirmation_message_body == 'You are about to delete this row. This action cannot be reverted!', 'Wrong confirmation body message'

    cancel_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[14]/div/div[6]/button[3]'))
    )
    assert cancel_button.is_displayed(), 'Cancel button is not displayed.'
    assert cancel_button.is_enabled(), 'Cancel button is not enabled.'

    yes_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[14]/div/div[6]/button[1]"))
    )
    assert yes_button.is_displayed(), 'Yes button is not displayed.'
    assert yes_button.is_enabled(), 'Yes button is not enabled.'
    action.move_to_element(yes_button).click().perform()

    comp_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[14]/div/h2'))
    ).text
    assert comp_message == 'Deleted!', 'Wrong completion title message'

    completion_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert completion_message == 'The row has been deleted.', 'Wrong completion message'

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[14]/div/div[6]/button[1]"))
    )
    assert ok_button.is_displayed(), 'OK button is not displayed.'
    assert ok_button.is_enabled(), 'OK button is not enabled.'
    action.move_to_element(ok_button).click().perform()

    print('Add Other passed')
except Exception as e:
    print(f"C-Error: {e}")
try:
    wait = WebDriverWait(driver, 20)
    add_button = driver.find_element(By.ID, 'add_voluntary_work')
    assert add_button.is_displayed(), 'Not Displayed'
    assert add_button.is_enabled(), "Not Enabled"
    add_button.click()
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="voluntary_work_tbody"]/tr[5]')))
    assert input_box.is_displayed(), "Input box is not visible"
except Exception as e:
    print(f"20: {e}")
try:
    wait = WebDriverWait(driver, 20)
    add_button = driver.find_element(By.ID, 'add_trainings_attended')
    assert add_button.is_displayed(), 'Not Displayed'
    assert add_button.is_enabled(), "Not Enabled'"
    add_button.click()
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="trainings_attended_tbody"]/tr[6]')))
    assert input_box.is_displayed(), "Input box is not visible"
except Exception as e:
    print(f"21: {e}")
try:
    wait = WebDriverWait(driver, 20)
    add_button = driver.find_element(By.ID, 'add_other_information')
    assert add_button.is_displayed(), 'Not Displayed'
    assert add_button.is_enabled(), "Not Enabled'"
    add_button.click()
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="other_information_tbody"]/tr[3]')))
    assert input_box.is_displayed(), "Input box is not visible"
except Exception as e:
    print(f"22: {e}")
try:
    save_button = driver.find_element(By.XPATH, '//*[@id="pds-part3"]/center/button[1]')
    assert save_button.is_displayed(), 'Not Displayed'
    assert save_button.is_enabled(), "Not Enabled'"
    assert "Save Draft".replace(" ", "") in save_button.text.replace(" ", ""), "Button text is incorrect"
    action.move_to_element(save_button).click().perform()
except Exception as e:
    print(f"24: {e}")
try:
    validation_button = driver.find_element(By.XPATH, '//*[@id="pds-part3"]/center/button[2]')
    assert validation_button.is_displayed(), 'Not Displayed'
    assert validation_button.is_enabled(), "Not Enabled'"
    assert "Validate & Finalize Part 3".replace(" ", "") in validation_button.text.replace(" ",
                                                                                           ""), "Button text is incorrect"
except Exception as e:
    print(f"25: {e}")
time.sleep(5)
# PART 4
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
print('-----PART 4-----')
driver.execute_script("window.scrollTo(0, 0);")
nav_tab = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div[1]/div[2]/div/ul/li[4]/a')
nav_tab.click()

try:
    assert "34. Are you related by consanguinity or affinity to the appointing or recommending authority, or to the chief of bureau or office or to the person who has immediate supervision over you in the Office, Bureau or Department where you will be appointed.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[1]/td[1]').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'1:{e}')
try:
    assert "  a. within the third degree?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[2]/td[1]').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'2: {e}')
try:
    assert "b. Within the fourth degree (for Local Government Unit - Career Employees)?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[3]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'3:{e}')
try:
    assert "35. a. Have you ever been found guilty of any administrative offense?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[4]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'4:{e}')
try:
    assert " b. Have you been criminally charged before any court?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[5]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'5: {e}')
try:
    assert "36. Have you ever been convicted of any crime or violation of any law, decree, ordinance or regulation by any court or tribunal?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[6]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'6: {e}')
try:
    assert "37. Have you ever been separated from the service in any of the following modes: resignation, retirement, dropped from the rolls, dismissal, termination, end of term, finished contract or phased out (abolition) in the public or private sector?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[7]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'7: {e}')
try:
    assert "38. a. Have you ever been a candidate in a national or local election held within the last year (except Barangay election)?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[8]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'8: {e}')
try:
    assert "b. Have you resigned from the government service during the three (3)-month period before the last election to promote/actively campaign for a national or local candidate?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[9]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'9: {e}')

try:
    assert "39. Have you acquired the status of an immigrant or permanent resident of another country?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[10]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'10: {e}')
try:
    assert "40. Pursuant to: (a) Indigenous People's Act (RA 8371); (b) Magna Carta for Disabled Persons (RA 7277); and (c) Solo Parents Welfare Act of 2000 (RA 8972), please answer the following items:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[11]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'11: {e}')
try:
    assert "a. Are you a member of any indigenous group?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[12]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'12: {e}')
try:
    assert " b. Are you a person with disability?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[13]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'13: {e}')
try:
    assert " c. Are you a solo parent?".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[14]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'14: {e}')
try:
    assert "41. REFERENCES".strip() and "(Person not related by consanguinity or affinity to applicant / appointee)" in driver.find_element(
        By.XPATH,
        '//*[@id="reference_tbody"]/tr[1]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'15: {e}')
try:
    assert "(Person not related by consanguinity or affinity to applicant / appointee)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="reference_tbody"]/tr[1]/td[1]/span').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'16: {e}')
try:
    assert "NAME".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="reference_tbody"]/tr[2]/td[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'17: {e}')
try:
    assert "ADDRESS".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="reference_tbody"]/tr[2]/td[2]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'18: {e}')
try:
    assert "TEL NO.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="reference_tbody"]/tr[2]/td[3]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'19: {e}')

try:
    assert "Government Issued ID".strip() in driver.find_element(
        By.XPATH,
        '/html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div[4]/div/form/center/div/table/tbody[3]/tr[2]/td[1]/table/tbody/tr[1]/td/font[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'20: {e}')
try:
    assert "PLEASE INDICATE ID Number".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[3]/tr[2]/td[1]/table/tbody/tr[1]/td/font[2]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'22: {e}')
try:
    assert "I declare under oath that I have personally accomplished this Personal Data Sheet which is true, correct and complete statement pursuant to the provisions of pertinent laws, rules and regulations of the Republic of the Philippines. I authorize the agency head/authorized representative to verify/validate the contents stated herein. I agree that any misrepresentation made in this document and its attachments shall cause the filing of administrative/criminal case/s against me.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[3]/tr[2]/td[2]/table[1]/tbody/tr[1]/td/div/label').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'23: {e}')
try:
    assert "Signature(Sign inside the box)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[3]/tr[2]/td[2]/table[1]/tbody/tr[2]/td').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'24: {e}')
try:
    assert ("SUBSCRIBED AND SWORN").strip() in driver.find_element(
        By.XPATH,
        '/html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div[4]/div/form/center/div/table/tbody[3]/tr[3]/td/font').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'25: {e}')
try:
    assert "Person Administering Oath".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="pds-part4"]/center/div/table/tbody[3]/tr[4]/td/table/tbody/tr[2]/td').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'26: {e}')

# Buttos, Input boxes, and some labels

try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'within_the_third_degree_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'within_the_third_degree_yes')))

    input_box = driver.find_element(By.ID, 'within_the_third_degree_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            # Handle the case where no specific error message element is found
            print(f"Error message element expected but not found.")

    driver.find_element(By.ID, 'within_the_third_degree_no_radio').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'within_the_third_degree_yes')))
    assert not driver.find_element(By.ID,
                                   'within_the_third_degree_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"27: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'within_the_fourth_degree_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'within_the_fourth_degree_yes')))

    input_box = driver.find_element(By.ID, 'within_the_fourth_degree_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            # Handle the case where no specific error message element is found
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[3]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'within_the_fourth_degree_yes')))
    assert not driver.find_element(By.ID,
                                   'within_the_fourth_degree_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"28: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'administrative_offense_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'administrative_offense_yes')))

    input_box = driver.find_element(By.ID, 'administrative_offense_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            # Handle the case where no specific error message element is found
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[4]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'administrative_offense_yes')))
    assert not driver.find_element(By.ID,
                                   'administrative_offense_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"29: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'criminally_charged_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'date_filed')))

    cal_box = driver.find_element(By.ID, 'date_filed')
    if not cal_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            # Handle the case where no specific error message element is found
            print(f"Error message element expected but not found.")

    wait.until(EC.visibility_of_element_located((By.ID, 'criminally_charged_yes')))
    input_box = driver.find_element(By.ID, 'criminally_charged_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[5]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'criminally_charged_yes')))
    assert not driver.find_element(By.ID,
                                   'criminally_charged_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"30: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'convicted_crime_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'convicted_crime_yes')))

    input_box = driver.find_element(By.ID, 'convicted_crime_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH, '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[6]/td[2]/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'convicted_crime_yes')))
    assert not driver.find_element(By.ID,
                                   'convicted_crime_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"31: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'separated_from_the_service_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'separated_from_the_service_yes')))

    input_box = driver.find_element(By.ID, 'separated_from_the_service_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[7]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'separated_from_the_service_yes')))
    assert not driver.find_element(By.ID,
                                   'separated_from_the_service_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"32: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'candidate_in_election_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'candidate_in_election_yes')))

    input_box = driver.find_element(By.ID, 'candidate_in_election_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[8]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'candidate_in_election_yes')))
    assert not driver.find_element(By.ID,
                                   'candidate_in_election_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"33: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'resigned_from_the_government_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'resigned_from_the_government_yes')))

    input_box = driver.find_element(By.ID, 'resigned_from_the_government_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[9]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'resigned_from_the_government_yes')))
    assert not driver.find_element(By.ID,
                                   'resigned_from_the_government_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"34: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'acquired_status_immigrant_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'acquired_status_immigrant_yes')))

    input_box = driver.find_element(By.ID, 'acquired_status_immigrant_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[10]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'acquired_status_immigrant_yes')))
    assert not driver.find_element(By.ID,
                                   'acquired_status_immigrant_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"35: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'indigenous_group_member_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'indigenous_group_member_yes')))

    input_box = driver.find_element(By.ID, 'indigenous_group_member_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[12]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'indigenous_group_member_yes')))
    assert not driver.find_element(By.ID,
                                   'indigenous_group_member_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"36: {e}")
try:
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, 'person_with_disability_yes_radio').click()
    wait.until(EC.visibility_of_element_located((By.ID, 'person_with_disability_yes')))

    input_box = driver.find_element(By.ID, 'person_with_disability_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[13]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'person_with_disability_yes')))
    assert not driver.find_element(By.ID,
                                   'person_with_disability_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"37: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.XPATH, '//*[@id="solo_parent_yes_radio"]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(5)
    wait = WebDriverWait(driver, 10)

    solo = driver.find_element(By.ID, 'solo_parent_yes_radio')
    action.scroll_to_element(solo).click().perform()
    wait.until(EC.visibility_of_element_located((By.ID, 'solo_parent_yes')))

    input_box = driver.find_element(By.ID, 'solo_parent_yes')

    if not input_box.get_attribute('value'):
        try:
            error_indicator = driver.find_element(By.CSS_SELECTOR, '.ajs-message.ajs-error.ajs-visible')
            assert "This field is required." in error_indicator.text, "The expected error message is not displayed."
        except NoSuchElementException:
            print(f"Error message element expected but not found.")

    driver.find_element(By.XPATH,
                        '//*[@id="pds-part4"]/center/div/table/tbody[1]/tr[14]/td[2]/table/tbody/tr[1]/td/input[2]').click()
    wait.until(EC.invisibility_of_element_located((By.ID, 'solo_parent_yes')))
    assert not driver.find_element(By.ID,
                                   'solo_parent_yes').is_displayed(), "The input box for 'YES' is still visible when 'NO' is selected."
except Exception as e:
    print(f"38: {e}")
try:
    action = ActionChains(driver)
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'add_reference')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(5)
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_reference"))
    )
    action.move_to_element(target_element).click().perform()

    new_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="reference_tbody"]/tr[3]'))
    )
    assert new_element.is_displayed() and new_element.is_enabled(), "Input boxes are not interactable after clicking the add button"

    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="reference_tbody"]/tr[3]/td[4]/button'))
    )
    assert delete_button.is_displayed(), "Delete button is not visible."
    assert delete_button.is_enabled(), "Delete button is not enabled."
    action.move_to_element(delete_button).click().perform()

    time.sleep(5)

    confirm_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[10]/div'))
    )
    assert confirm_message.is_displayed(), "Confirmation message is not displayed."

    confirmation_message_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-title"]'))
    ).text
    assert confirmation_message_title == 'Are you sure?', 'Wrong confirmation title message'

    confirmation_message_body = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert confirmation_message_body == 'You are about to delete this row. This action cannot be reverted!', 'Wrong confirmation body message'

    cancel_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[10]/div/div[6]/button[3]'))
    )
    assert cancel_button.is_displayed(), 'Cancel button is not displayed.'
    assert cancel_button.is_enabled(), 'Cancel button is not enabled.'

    yes_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[10]/div/div[6]/button[1]"))
    )
    assert yes_button.is_displayed(), 'Yes button is not displayed.'
    assert yes_button.is_enabled(), 'Yes button is not enabled.'
    action.move_to_element(yes_button).click().perform()

    comp_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div/h2'))
    ).text
    assert comp_message == 'Deleted!', 'Wrong completion title message'

    completion_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="swal2-html-container"]'))
    ).text
    assert completion_message == 'The row has been deleted.', 'Wrong completion message'

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/div[6]/button[1]"))
    )
    assert ok_button.is_displayed(), 'OK button is not displayed.'
    assert ok_button.is_enabled(), 'OK button is not enabled.'
    action.move_to_element(ok_button).click().perform()

    print(' Reference passed')
except Exception as e:
    print(f"39: {e}")

# WORK EXPERIENCE SHEET

# -------------------------------------------------------------------------------------------------------------------------------------------
print('-----WORK EXPERIENCE SHEET-----')
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(3)
nav_tab = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div[1]/div[2]/div/ul/li[5]/a/span')
action.move_to_element(nav_tab).click().perform()

try:
    container = driver.find_element(By.XPATH,
                                    '/html/body/div[2]/div[2]/div/div[1]/div[3]/div/div[1]/div/div/div[5]/div/div[1]/div/div/div[2]')
    target_element = driver.find_element(By.XPATH, '//*[@id="pds-part1"]/center/button[2]')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(3)
except Exception as e:
    print(f'Error: {e}')

try:
    assert "Attachment to CS Form No. 212".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="wes"]/div/b/i').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'1:{e}')
try:
    assert "WORK EXPERIENCE SHEET".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="wes"]/div/div[3]/div[1]/div/p/i').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'2: {e}')
try:
    assert "Instructions:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="wes"]/div/div[3]/div[1]/p/strong').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'3:{e}')
try:
    assert "Include only the work experiences relevant to the position being applied for.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="wes"]/div/div[3]/div[1]/ol/li[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'4:{e}')
try:
    assert "The duration should include start and finish dates, if known, month in abbreviated form, if known, and year in full. For the current position, use the word Present, e.g., 1998-Present. Work experience should be listed starting with the most recent/present employment.".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="wes"]/div/div[3]/div[1]/ol/li[2]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'5: {e}')
try:
    add_button = driver.find_element(By.ID, 'add-experience')
    assert add_button.is_displayed(), 'Not Displayed'
    assert add_button.is_enabled(), "Not Enabled'"
    assert "+ Add Work Experience".strip() in driver.find_element(
        By.ID, 'add-experience').text.strip(), "The text is not present in the element"
    time.sleep(3)
    action.move_to_element(add_button).click().perform()
except AssertionError as e:
    print(f'Error: {e}')

try:
    assert "Add Work Experience".strip() in driver.find_element(
        By.CLASS_NAME,
        'modal-title').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'6: {e}')
try:
    assert "Duration:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[1]').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'7: {e}')
try:
    assert "From:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[1]/div/div[1]').text.strip(), "The text is not present in the element"
    input_box = driver.find_element(By.ID, "duration_from")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'
except AssertionError as e:
    print(f'8: {e}')
try:
    checkbox = driver.find_element(By.ID, 'currently_employed')
    duration_to = driver.find_element(By.ID, 'duration_to')
    action.move_to_element(checkbox).click().perform()

    assert "To:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[1]/div/div[2]/label').text.strip(), "The text is not present in the element"
    input_box = driver.find_element(By.ID, "duration_to")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'

except AssertionError as e:
    print(f'9: {e}')

try:
    assert "Position:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[2]/label').text.strip(), "The text is not present in the element"
    input_box = driver.find_element(By.ID, "position")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'
except AssertionError as e:
    print(f'10: {e}')
try:
    assert "Name of Office/Unit:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[3]/label').text.strip(), "The text is not present in the element"
    input_box = driver.find_element(By.ID, "office-unit")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'
except AssertionError as e:
    print(f'11: {e}')
try:
    assert "Immediate Supervisor:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[4]/label').text.strip(), "The text is not present in the element"
    input_box = driver.find_element(By.ID, "supervisor")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'
except AssertionError as e:
    print(f'12: {e}')
try:
    assert "Name of Agency/Organization and Location:".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[5]/label').text.strip(), "The text is not present in the element"
    input_box = driver.find_element(By.ID, "agency")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'
except AssertionError as e:
    print(f'13: {e}')

try:
    assert "List of Accomplishments and Contributions (if any)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[6]/label').text.strip(), "The text is not present in the element"
    input_box = driver.find_element(By.ID, "accomplishments")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'
except AssertionError as e:
    print(f'14: {e}')
try:
    assert "Summary of Actual Duties".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[2]/form/div/div[7]/label').text.strip(), "The text is not present in the element"

    input_box = driver.find_element(By.ID, "duties")

    assert input_box.is_displayed(), 'not displayed'
    assert input_box.is_enabled(), 'not working'
except AssertionError as e:
    print(f'15: {e}')
try:
    assert "Save".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[3]/button[2]').text.strip(), "The text is not present in the element"
    save_button = driver.find_element(By.ID, "accomplishments")

    assert save_button.is_displayed(), 'not displayed'
    assert save_button.is_enabled(), 'not working'
    action.move_to_element(save_button).click().perform()
except AssertionError as e:
    print(f'16: {e}')
try:
    assert "Close".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="addWorkExperienceModal"]/div/div/div[3]/button[1]').text.strip(), "The text is not present in the element"

    close_button = driver.find_element(By.ID, "duties")

    assert close_button.is_displayed(), 'not displayed'
    assert close_button.is_enabled(), 'not working'
    driver.find_element(By.XPATH, '//*[@id="addWorkExperienceModal"]/div/div/div[3]/button[1]').click()
except AssertionError as e:
    print(f'17: {e}')

time.sleep(5)
# --------------------------------------------------------------------------------------------------------------------
print('-----ATTACHMENT-----')
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(5)
nav_tab = driver.find_element(By.XPATH, '//*[@id="layout-wrapper"]/div[2]/div/div[1]/div[2]/div/ul/li[6]/a')
action.move_to_element(nav_tab).click().perform()

try:
    assert "2x2 Picture".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="attachmentsForm"]/div/div[3]/div/div[2]/div[1]/label').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'1:{e}')
try:
    assert "Curriculum Vitae".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="attachmentsForm"]/div/div[3]/div/div[2]/div[2]/label').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'2: {e}')
try:
    assert "Transcript of Records".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="attachmentsForm"]/div/div[3]/div/div[2]/div[3]/label').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'3:{e}')
try:
    assert "Passport Size Picture".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="attachments"]/div[2]/div[1]/div/div[2]/div[1]/label').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'4:{e}')
try:
    assert "Certificate of Eligibility".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="attachments"]/div[2]/div[1]/div/div[2]/div[2]/label').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'5: {e}')

try:
    assert "Performance Evaluation Report".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="attachments"]/div[2]/div[1]/div/div[2]/div[3]/label').text.strip(), "The text is not present in the element"

except AssertionError as e:
    print(f'6: {e}')
try:
    assert "Employment Certificate (or Service Record)".strip() in driver.find_element(
        By.XPATH,
        '//*[@id="attachments"]/div[2]/div[1]/div/div[2]/div[4]/label').text.strip(), "The text is not present in the element"
except AssertionError as e:
    print(f'7: {e}')
try:
    assert " Submit Attachments".strip() in driver.find_element(
        By.ID,
        'upload-attachments').text.strip(), "The text is not present in the element"
    button = driver.find_element(By.ID, "upload-attachments")

    assert button.is_displayed(), 'not displayed'
    assert button.is_enabled(), 'not working'
except AssertionError as e:
    print(f'8: {e}')

try:
    element_xpaths = {
        '1': '//*[@id="2x2_picture"]',
        '2': '//*[@id="curriculum_vitae"]',
        '3': '//*[@id="transcript_of_records"]',
        '4': '//*[@id="passport_size_picture"]',
        '5': '//*[@id="performance_evaluation_report"]',
        '6': '//*[@id="employment_certificate"]',
        '7': '//*[@id="training_certificates"]',
    }
    for element_name, xpath in element_xpaths.items():
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        assert element.is_displayed(), f'{element_name} is not displayed'
        assert element.is_enabled(), f'{element_name} is not enabled'
except Exception as e:
    print(f"Error with {element_name}: {e}")

try:
    container = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div[3]')
    target_element = driver.find_element(By.ID, 'upload-attachments')
    driver.execute_script("arguments[0].scrollTop = arguments[1].offsetTop;", container, target_element)
    time.sleep(5)

    upload_file = driver.find_element(By.ID, 'upload-attachments')
    action.move_to_element(upload_file).click().perform()

    try:
        notification = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[9]"))
        )

        if notification.is_displayed():
            print("Notification is displayed ")
        else:
            print("Notification is not displayed")

    except Exception as e:
        print("Notification not found:", e)
except Exception as e:
    print(f"Error: {e}")

time.sleep(10)