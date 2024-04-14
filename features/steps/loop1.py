from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#explicit examples
# driver.wait = WebDriverWait(driver, timeout=10)
# driver.wait.until(EC.element_to_be_clickable((By.Name, 'btnk'))).click

COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")

@given('Open Target product page')
def open_target_product(context):
    # open target
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com/p/men-39-s-packable-jacket-all-in-motion-8482/-/A-89823674?preselect=89391012#lnk=sametab")

    driver.implicitly_wait(5)

@when('loop through colors')
def colors(context):

    expected_colors = ['Black Onyx', 'Light Green', 'Teal Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

