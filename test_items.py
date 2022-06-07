import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exist_add_to_cart_button(browser):
    browser.get(link)
	# найти кнопку добавления товара в корзину
    WebDriverWait(browser, 3).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "Нет кнопки добавления в корзину")