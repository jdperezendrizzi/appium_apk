import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException as ECIE, ElementNotInteractableException, \
    NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
from datetime import timedelta
import random


class PageGeneraToken:

    def __init__(self, my_driver):
        self.driver = my_driver

        #Generar Token
        self.button_elegi = (By.XPATH, '//android.view.ViewGroup[@content-desc="Elegir integrante del grupo"]')
        self.option_federico = (By.XPATH, '//android.view.ViewGroup[@content-desc="RAVA FEDERICO"]')
        self.button_genera = (By.XPATH, '//android.view.ViewGroup[@content-desc="GENERAR NUEVO TOKEN"]')
        self.text_generacion_token = (By.XPATH, '//android.widget.TextView[@text="Generación de TOKEN"]')

    def selecciona_integrante(self):
        time.sleep(3)
        self.driver.find_element(*self.button_elegi).click()
        time.sleep(3)
        self.driver.find_element(*self.option_federico).click()

    def click_genera_nuevo(self):
        time.sleep(3)
        self.driver.find_element(*self.button_genera).click()

    def return_generacion(self):
        time.sleep(5)
        return self.driver.find_element(*self.text_generacion_token).text

