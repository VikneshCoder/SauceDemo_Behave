import time
from behave import given, when, then
from selenium.webdriver.common.by import By


@given('I am on the Demo Login Page')
def given_demo_login_page(context):
    context.driver.get("https://www.saucedemo.com/")

@when('I fill the account information for account "{user}" into the Username field and the Password field')
def fill_login_information(context, user):
    context.driver.find_element(By.ID, 'user-name').send_keys(user)
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

@when('I click the Login Button')
def click_login(context):
    context.driver.find_element(By.ID, 'login-button').click()

@then('I am redirected to the Main Page')
def verify_redirect(context):
    Title = context.driver.title
    assert "Swag Labs" == Title

@then('I verify the App Logo exists')
def verify_app_logo(context):
    logo = context.driver.find_element(By.XPATH, "//div[@class='app_logo']")
    assert logo.is_displayed(), "App logo is not displayed"

@then('I verify the Error Message contains the text "Sorry, this user has been banned."')
def verify_error_message(context):
    error_message = context.driver.find_element(By.XPATH, "//h3[contains(text(),'Epic sadface: Username and password do not match a')]")
    assert "Username and password do not match" in error_message.text

