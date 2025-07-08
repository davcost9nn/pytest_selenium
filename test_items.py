import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_items(browser):
    browser.get(link)
    time.sleep(30)

    try:
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert button.is_displayed(), "Кнопка не видна!"
    except NoSuchElementException:
        pytest.fail("Кнопка 'Добавить в корзину' не найдена на странице!")


