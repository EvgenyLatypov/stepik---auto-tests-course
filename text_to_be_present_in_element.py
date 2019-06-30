from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)

browser = webdriver.Chrome('/chromedriver/chromedriver.exe', chrome_options=opt)
browser.implicitly_wait(15)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
)

browser.find_element_by_id('book').click()
x_element = browser.find_element_by_id('input_value')

x = float(x_element.text)
y = calc(x)

browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_id('solve').click()
