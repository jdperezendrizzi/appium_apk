import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class PageFacturacion:
    def __init__(self, my_driver):

        self.driver = my_driver


        # Pagos
        self.button_pagar = (By.XPATH, '//android.widget.TextView[@content-desc="estCuenNcliText12"]')
        self.button_efectivo = (By.XPATH, '//android.widget.TextView[@content-desc="mpT12"]')
        self.button_galicia = (By.XPATH, '//android.view.ViewGroup[@content-desc="pagoEfectivoB"]/android.widget.ImageView')
        self.text_instrucciones = (By.XPATH, '//android.widget.TextView[@content-desc="pagoEgaliciaT"]')

    def click_pagar(self):
        time.sleep(10)
        self.driver.find_element(*self.button_pagar).click()

    def click_efectivo(self):
        time.sleep(10)
        self.driver.find_element(*self.button_efectivo).click()

    def click_galicia(self):
        time.sleep(10)
        self.driver.find_element(*self.button_galicia).click()
    def return_instrucciones_pago(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_instrucciones)).text
