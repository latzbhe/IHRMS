from login import login
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException

chrome_driver_path = r'C:\Users\user\chromedriver-win64\chromedriver.exe'

driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path))
driver.maximize_window()

driver.get("http://10.10.99.4/login")
driver.maximize_window()

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
    alert = driver.switch_to.alert
    print(f"An unexpected alert appeared: {alert.text}")
    alert.accept()

time.sleep(5)
file_button = (WebDriverWait(driver, 10).until
   (EC.visibility_of_element_located((By.XPATH, "//*[@id='tbl_empinfo']/tbody/tr[1]/td[9]/center/a[3]/i"))))

file_button.click()

try:
    # Wait for an expected element on the 201 files page (appointment)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.NAME, "appointment")))
except Exception as e:
    print(f"Error: {e}")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    expected_guidelines = (
        "Attachment Uploading Guidelines\n"
        "File Naming:\n"
        "requirement_type_first_word_last_name_first_name.extension\n"
        "assumption_to_duty_dela_cruz_juan.pdf\n\n"
        "File Type:\n"
        "PDF only\n\n"
        "File Size:\n"
        "5 MB each\n\n"
        "Attachments with improper filename, filetype, and filesize will not be accepted."
    )
    try:
        guidelines_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[1]"))
        )

        actual_guidelines = guidelines_element.text

        assert actual_guidelines == expected_guidelines, \
            f'Expected guidelines:\n"{expected_guidelines}"\nbut got:\n"{actual_guidelines}"'

        print('Guidelines text is displayed correctly.')

    except TimeoutException:
        print('Timeout: The guidelines element was not found in time.')
    except NoSuchElementException as e:
        print(f'Error: Element not found. Details: {e}')
    # First: Appointment (Form 33)
    try:
        form_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[1]/b").text
        assert form_text == 'Appointment (Form 33)', 'itle is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[1]/small").text
        assert file_naming_text == 'File Naming: appointment_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, 'appointment')
        assert choose_file.is_displayed(), 'Choose File button is not displayed'
        assert choose_file.is_enabled(), 'Choose File button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/appointment_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary')]"))
        )

        driver.execute_script("arguments[0].click();", submit_button)
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div"))
        )
            element_text = success_message.text.strip()
            print(f"Element text after waiting: '{element_text}'")


        except TimeoutException as e:
            print(f"TimeoutException occurred: {e}")
        except AssertionError as e:
            print(f'Assertion: {e}')
        except Exception as e:
            print(f"Error: {e}")

    except Exception as e:
            print(f"Error in Appointment (Form 33): {e}")
    time.sleep(5)
    # Second: Assumption to Duty
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[2]/b").text
        assert first_text == 'Assumption to Duty', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[2]/small").text
        assert file_naming_text == 'File Naming: assumption_to_duty_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, 'assumption_to_duty')
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'


        pdf_file_path = 'C:/Users/user/Downloads/assumption_to_duty_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Assumption to Duty: {e}")
    time.sleep(5)
#-------------------------------------------------------------------------------------------------------------------------------------------
# Third: Clearance from Property and Money Accountabilities (for transferees)
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[3]/b").text
        assert first_text == 'Clearance from Property and Money Accountabilities (for transferees)', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[3]/small").text
        assert file_naming_text == 'File Naming: clearance_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, "clearance")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/clearance_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Clearance from Property and Money Accountabilities (for transferees): {e}")
    time.sleep(5)
#-------------------------------------------------------------------------------------------------------------------------
#FOURTH: 'Certificate of Eligibilities/Licenses'
    try:
        first_text = driver.find_element(By.XPATH,"//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[4]/b").text
        assert first_text == 'Certificate of Eligibilities/Licenses', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH,"//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[4]/small").text
        assert file_naming_text == 'File Naming: certificate_of_eligibilities_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME,"certificate_of_eligibilities")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/certificate_of_eligibilities_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button"))
        )

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
        print(f"Error in Certificate of Eligibilities/Licenses: {e}")
    time.sleep(5)
#---------------------------------------------------------------------------------------------------------------
    #Fiffth:Certificate of Leave Balances (for transferees)
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[5]/b").text
        assert first_text == 'Certificate of Leave Balances (for transferees)', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[5]/small").text
        assert file_naming_text == 'File Naming: leave_balances_last_name_first_name', 'File naming text is incorrect'
    except Exception as e:
            print(f"Error in Certificate of Leave Balances (for transferees): {e}")
    try:
        choose_file = driver.find_element(By.NAME, "leave_balances")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/leave_balances_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button"))
        )

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Certificate of Leave Balances (for transferees): {e}")
    time.sleep(5)
# ------------------------------------------------------------------------------------------------------------------
    #Sixth: Commendations, Certificate of Achievement, Awards, etc.
    try:
        form_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[6]/b").text
        assert form_text == 'Commendations, Certificate of Achievement, Awards, etc.', 'Title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[6]/small").text
        assert file_naming_text == 'File Naming: commendations_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, 'commendations')
        assert choose_file.is_displayed(), 'Choose File button is not displayed'
        assert choose_file.is_enabled(), 'Choose File button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/commendations_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary')]")))

        driver.execute_script("arguments[0].click();", submit_button)

    except Exception as e:
            print(f"Error in Commendations, Certificate of Achievement, Awards, etc.: {e}")
    time.sleep(5)
#------------------------------------------------------------------------------------------------------------------------------------
    # Seventh: Contract of Service (if applicable)
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[7]/b").text
        assert first_text == 'Contract of Service (if applicable)', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[7]/small").text
        assert file_naming_text == 'File Naming: contract_of_service_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, 'contract_of_service')
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/contract_of_service_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Contract of Service: {e}")
    time.sleep(5)
#-------------------------------------------------------------------------------------------------------------------------------------------
# Eighth: Designation Orders (if applicable)
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[8]/b").text
        assert first_text == 'Designation Orders (if applicable)', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[8]/small").text
        assert file_naming_text == 'File Naming: designation_orders_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, "designation_orders")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/designation_orders_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Designation Orders (if applicable): {e}")
    time.sleep(5)
#-------------------------------------------------------------------------------------------------------------------------
#Ninth: Disciplinary Action Documents (if any)
    try:
        first_text = driver.find_element(By.XPATH,"//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[9]/b").text
        assert first_text == 'Disciplinary Action Documents (if any)', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH,"//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[1]/div[9]/small").text
        assert file_naming_text == 'File Naming: disciplinary_action_documents_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME,"disciplinary_action_documents")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/disciplinary_action_documents_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
        print(f"Error in Disciplinary Action Documents (if any): {e}")
    time.sleep(5)
#-----------------------------------------------------------
    #10th: Marriage Contract/Certificate
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[1]/b").text
        assert first_text == 'Marriage Contract/Certificate', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[1]/small").text
        assert file_naming_text == 'File Naming: marriage_contract_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, "marriage_contract")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/marriage_contract_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Marriage Contract/Certificate: {e}")
    time.sleep(5)
#-------------------------------------------------------------------------------------------------------------
# 11th: Medical Certificate (CSC Form 211
    try:
        form_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[2]/b").text
        assert form_text == 'Medical Certificate (CSC Form 211)', 'Title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[2]/small").text
        assert file_naming_text == 'File Naming: medical_certificate_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, 'medical_certificate')
        assert choose_file.is_displayed(), 'Choose File button is not displayed'
        assert choose_file.is_enabled(), 'Choose File button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/medical_certificate_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary')]")))

        driver.execute_script("arguments[0].click();", submit_button)

    except Exception as e:
            print(f"Error in Medical Certificate (CSC Form 211): {e}")
    time.sleep(5)
#------------------------------------------------------------------------------------------------------
    # 12th: NBI Clearance
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[3]/b").text
        assert first_text == 'NBI Clearance', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[3]/small").text
        assert file_naming_text == 'File Naming: nbi_clearance_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, 'nbi_clearance')
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/nbi_clearance_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in NBI clearance: {e}")
    time.sleep(5)
#-------------------------------------------------------------------------------------------------------------------------------------------
# 13th: Notices of Salary Adjustments/Step Increments
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[4]/b").text
        assert first_text == 'Notices of Salary Adjustments/Step Increments', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[4]/small").text
        assert file_naming_text == 'File Naming: salary_adjustments_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, "salary_adjustments")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/salary_adjustments_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Notices of Salary Adjustments/Step Increments: {e}")
    time.sleep(5)
#-------------------------------------------------------------------------------------------------------------------------
#14th: Oath to Office
    try:
        first_text = driver.find_element(By.XPATH,"//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[5]/b").text
        assert first_text == 'Oath to Office', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH,"//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[5]/small").text
        assert file_naming_text == 'File Naming: oath_to_office_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME,"oath_to_office")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/oath_to_office_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))
        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
        print(f"Error in Oath to Office: {e}")
    time.sleep(5)
#-----------------------------------------------------------
    #15th:Position Description Form
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[6]/b").text
        assert first_text == 'Position Description Form', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[6]/small").text
        assert file_naming_text == 'File Naming: position_description_form_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, "position_description_form")
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'

        pdf_file_path = 'C:/Users/user/Downloads/position_description_form_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))
        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in Position Description Form: {e}")
    time.sleep(5)
#--------------------------------------------------------------------------------------------------------------------------------
# 16th: School Diplomas and Transcript of Records
    try:
        form_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[7]/b").text
        assert form_text == 'School Diplomas and Transcript of Records', 'itle is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[7]/small").text
        assert file_naming_text == 'File Naming: school_diplomas_last_name_first_name', 'File naming text is incorrect'

        # Assert the presence and enabled state of file upload button
        choose_file = driver.find_element(By.NAME, 'school_diplomas') # Adjust the selector as needed
        assert choose_file.is_displayed(), 'Choose File button is not displayed'
        assert choose_file.is_enabled(), 'Choose File button is not enabled'

        # Path to the PDF file you want to upload
        pdf_file_path = 'C:/Users/user/Downloads/school_diplomas_test_test.pdf'
        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)

    except Exception as e:
            print(f"Error in School Diplomas and Transcript of Records: {e}")
    time.sleep(5)
    # 17th: State of Assets, Liabilities, and Networth
    try:
        first_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[8]/b").text
        assert first_text == 'State of Assets, Liabilities, and Networth', 'Text title is incorrect'

        file_naming_text = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[8]/small").text
        assert file_naming_text == 'File Naming: assets_last_name_first_name', 'File naming text is incorrect'

        choose_file = driver.find_element(By.NAME, 'assets')
        assert choose_file.is_displayed(), 'Choose file button is not displayed'
        assert choose_file.is_enabled(), 'Choose file button is not enabled'


        pdf_file_path = 'C:/Users/user/Downloads/assets_test_test.pdf'

        choose_file.send_keys(pdf_file_path)

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")))

        driver.execute_script("arguments[0].click();", submit_button)
    except Exception as e:
            print(f"Error in State of Assets, Liabilities, and Networth: {e}")
    try:
        upload_file = driver.find_element(By.XPATH, "//*[@id='layout-wrapper']/div[2]/div/div/div/div/div[2]/form/div/div[2]/div[9]/button")
        assert upload_file.is_displayed(), 'Upload button is not displayed'
        assert upload_file.is_enabled(), 'Upload button is not enabled'
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)
finally:
    time.sleep(10)
