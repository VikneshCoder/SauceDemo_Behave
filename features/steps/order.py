from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@given('I log in with valid credentials')
def log_in(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.find_element(By.ID, 'user-name').send_keys("standard_user")  # Replace with your username
    context.driver.find_element(By.ID, 'password').send_keys("secret_sauce")     # Replace with your password
    context.driver.find_element(By.ID, 'login-button').click()
@given('I am on the inventory page')
def given_inventory_page(context):
    context.driver.refresh()
    context.driver.get("https://www.saucedemo.com/inventory.html")


@when('user sorts products from high price to low price')
def sort_products(context):
    select = Select(context.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    select.select_by_visible_text('Price (high to low)')

@when('user adds highest priced product')
def add_highest_priced_product(context):
    products = context.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
    products[0].find_element(By.XPATH, "//button[contains(@class,'btn_small btn_inventory')]").click()

@when('user clicks on cart')
def click_cart(context):
    context.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

@when('user clicks on checkout')
def click_checkout(context):
    context.driver.find_element(By.ID, 'checkout').click()

@when('user enters first name "{first_name}"')
def enter_first_name(context, first_name):
    context.driver.find_element(By.ID, 'first-name').send_keys(first_name)

@when('user enters last name "{last_name}"')
def enter_last_name(context, last_name):
    context.driver.find_element(By.ID, 'last-name').send_keys(last_name)

@when('user enters zip code "{zip_code}"')
def enter_zip_code(context, zip_code):
    context.driver.find_element(By.ID, 'postal-code').send_keys(zip_code)

@when('user clicks Continue button')
def click_continue(context):
    context.driver.find_element(By.ID, 'continue').click()

@then('I verify in Checkout overview page if the total amount for the added item is "$49.99"')
def total_amount(context):
    Total = context.driver.find_element(By.CLASS_NAME, 'inventory_item_price')
    assert "$49.99" in Total.text, f"Expected total to be $49.99, but got {Total.text}"

@when('user clicks Finish button')
def click_finish(context):
    context.driver.find_element(By.ID, 'finish').click()

@then('Thank You header is shown in Checkout Complete page')
def verify_thank_you_header(context):
    Thank_You_Message = context.driver.find_element(By.CLASS_NAME, 'complete-header')
    assert "Thank you for your order!" in Thank_You_Message.text
