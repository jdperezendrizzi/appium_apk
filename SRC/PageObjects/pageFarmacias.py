import unittest
import time
from appium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class PageFarmacias:
    def __init__(self, my_driver):
        self.driver = my_driver

        # Elementos del Forma
        #Por localidad
        self.button_localidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="LOCALIDAD"]')
        self.select_plan = (By.XPATH, '//android.view.ViewGroup[@content-desc="PLATA"]')
        self.option_bronce = (By.XPATH, '//android.view.ViewGroup[@content-desc="BRONCE"]')
        self.select_localidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="Seleccioná una localidad"]/android.widget.TextView')
        self.option_mayo = (By.XPATH, '//android.view.ViewGroup[@content-desc="25 DE MAYO                              "]')
        self.select_provincia = (By.XPATH, '//android.view.ViewGroup[@content-desc="Seleccioná una provincia"]')
        self.option_buenos_aires = (By.XPATH, '//android.view.ViewGroup[@content-desc="BUENOS AIRES"]')
        self.button_buscar = (By.XPATH, '//android.view.ViewGroup[@content-desc="BUSCAR"]/android.widget.TextView')
        self.button_permiso = (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
        self.text_farmacia = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]")
        #por cercania

    def click_localidad(self):
        time.sleep(10)
        self.driver.find_element(*self.button_localidad).click()

    def seleccionar_plan(self):
        time.sleep(5)
        self.driver.find_element(*self.select_plan).click()
        time.sleep(5)
        self.driver.find_element(*self.option_bronce).click()

    def seleccionar_localidad(self):
        time.sleep(10)
        self.driver.find_element(*self.select_localidad).click()
        time.sleep(5)
        self.driver.find_element(*self.option_mayo).click()


    def click_permiso(self):
        time.sleep(5)
        self.driver.find_element(*self.button_permiso).click()

    def seleccionar_provincia(self):
        time.sleep(10)
        self.driver.find_element(*self.select_provincia).click()
        time.sleep(5)
        self.driver.find_element(*self.option_buenos_aires).click()

    def click_buscar(self):
        time.sleep(5)
        self.driver.find_element(*self.button_buscar).click()

    def return_farmacia(self):
        time.sleep(5)
        return self.driver.find_element(*self.text_farmacia).text
