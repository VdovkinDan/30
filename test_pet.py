from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Test:

    def test_prts(self):
        driver_service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=driver_service)
        driver.get('https://petfriends.skillfactory.ru')
        WDW(driver, 5).until(EC.presence_of_element_located(('xpath', "(//button)[2]")))
        driver.find_element('xpath', "(//button)[2]").click()
        WDW(driver, 5).until(EC.presence_of_element_located(('xpath', "//div//a")))
        driver.find_element('xpath', "//div//a").click()
        driver.find_element('id', 'email').send_keys('vdovkin@mail.ru')
        driver.find_element('id', 'pass').send_keys('123456')
        driver.find_element('xpath', '(//button)[2]').click()
        driver.find_element('xpath', "(//a[@class='nav-link'])[1]").click()
        images = driver.find_elements_by_css_selector('.card-deck .card-img-top')
        names = driver.find_elements_by_css_selector('.card-deck .card-title')
        descriptions = driver.find_elements_by_css_selector('.card-deck .card-text')
        for i in range(len(names)):
            assert images[i].get_attribute('src') != ''
            assert names[i].text != ''
            assert descriptions[i].text != ''
            assert ', ' in descriptions[i]
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0



