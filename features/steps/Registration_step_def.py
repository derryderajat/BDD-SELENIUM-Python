from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given(u'User is on Registration Page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Sign up']").click()
    
@when(u'User enter username {username}')
def step_impl(context, username):
    context.driver.find_element(By.XPATH, "//input[@placeholder='myusername']").send_keys(username)

@when(u'User enters email_id {email_id}')
def step_impl(context, email_id):
    context.driver.find_element(By.NAME, "fld_email").send_keys(email_id)

@when(u'User enters password {password}')
def step_impl(context, password):
    context.driver.find_element(By.NAME, "fld_password").send_keys(password)
    context.driver.find_element(By.NAME, "fld_cpassword").send_keys(password)

@when(u'User pick bod {bod}')
def step_impl(context, bod):
    date_picker_element = context.driver.find_element(By.ID, "datepicker")
    date_picker_element.send_keys(bod)
    date_picker_element.send_keys(Keys.RETURN)

@when(u'User choose Gender {gender}')
def step_impl(context, gender):
    select_element_gender = Select(context.driver.find_element(By.NAME, "sex"))
    select_element_gender.select_by_visible_text(str(gender).title())
@when(u'User choose {country} as country')
def step_impl(context, country):
    
    select_element_country = context.driver.find_element(By.NAME, "country")
    select_country = Select(select_element_country)
    
    # Tunggu hingga elemen pertama kali muncul dalam dropdown
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//option[normalize-space(.)='{country.title()}']"))
    )
    select_country.select_by_visible_text(country.title())
    time.sleep(3)

@when(u'User choose {state} as state')
def step_impl(context, state):
    # Tunggu sampai dropdown negara memperbarui opsi state
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.NAME, "state"), "Select State")
    )

    time.sleep(2)  # Tunggu tambahan jika diperlukan (bisa dihapus jika tidak perlu)
    
    select_element_state = context.driver.find_element(By.NAME, "state")
    select_state = Select(select_element_state)
    
    # Tunggu hingga opsi state yang diinginkan muncul dalam dropdown
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//option[normalize-space(.)='{state.title()}']"))
    )
    
    select_state.select_by_visible_text(state.title())
    option = select_state.first_selected_option
    context.driver.execute_script("arguments[0].scrollIntoView(true);", option)
    option.click()


@when(u'User choose {city} as city')
def step_impl(context, city):
    # Tunggu sampai dropdown state memperbarui opsi city
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.NAME, "city"), "Select City")
    )

    time.sleep(3)  # Tunggu tambahan jika diperlukan (bisa dihapus jika tidak perlu)
    
    select_element_city = context.driver.find_element(By.NAME, "city")
    select_city = Select(select_element_city)
    
    # Tunggu hingga opsi city yang diinginkan muncul dalam dropdown
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//option[normalize-space(.)='{city.title()}']"))
    )
    
    select_city.select_by_visible_text(city.title())
    option = select_city.first_selected_option
    context.driver.execute_script("arguments[0].scrollIntoView(true);", option)
    option.click()


   
@when(u'User enters {zipcode} zip code')
def step_impl(context, zipcode):
    context.driver.find_element(By.NAME, "zip").send_keys(zipcode)
    
@when(u'User clicks on Sign Up Button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Sign up' and @type='submit']").click()


@when(u'User check the terms and condition')
def step_impl(context):
    # Temukan elemen checkbox dengan nama "terms"
    checkbox = context.driver.find_element(By.NAME, "terms")
    # Periksa apakah checkbox saat ini sudah tercentang
    if not checkbox.is_selected():
        # Jika belum tercentang, centang checkbox
        checkbox.click()

@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")
    
    # Tunggu hingga halaman diarahkan dan elemen alert muncul
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert"))
    )

    alert_element = context.driver.find_element(By.CLASS_NAME, "alert")
    alert_text = alert_element.text
    assert "User is successfully Register" in alert_text, f"Expected 'User is successfully Register' in alert text, but got '{alert_text}'"
    assert "Now You can Login" in alert_text, f"Expected 'Now You can Login' in alert text, but got '{alert_text}'"
    