import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class PageCredenciales:

    def __init__(self, my_driver):
        self.driver = my_driver

        #Credencialdigital

        self.button_aceptar = (By.XPATH, '//android.widget.TextView[@content-desc="btnModalcred"]')
        self.button_vista = (By.XPATH, '//android.widget.Button[@content-desc=""]/android.view.ViewGroup/android.widget.TextView')
        self.text_voluntario = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[10]')
        self.button_detalle_volver = (By.XPATH, '//android.widget.Button[@content-desc=""]')

        self.text_usr_credencial_2 = (By.XPATH, '//android.widget.TextView[contains(@text, "ABITANTE, VANINA PAOLA")]')

        self.text_du_detalle_credencial_2 = (By.XPATH, '//android.widget.TextView[contains(@text, "23326494")]')

        #Generar token


    def click_aceptar(self):
        time.sleep(10)
        self.driver.find_element(*self.button_aceptar).click()

    def click_vista_credencial(self):
        time.sleep(10)
        self.driver.find_element(*self.button_vista).click()
    def return_voluntario(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_voluntario)).text

    def click_detalle_volver(self):
        time.sleep(10)
        self.driver.find_element(*self.button_detalle_volver).click()

    def return_du_detalle_credencial_2(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_du_detalle_credencial_2)).text
