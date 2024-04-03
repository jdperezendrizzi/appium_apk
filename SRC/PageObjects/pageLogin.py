import unittest
import time
from appium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class PageLogin:
    def __init__(self, my_driver):
        self.driver = my_driver

        # Elementos del Forma
        #mail
        self.button_ingresa_mail = (By.XPATH, '//android.view.ViewGroup[@content-desc="Ingresá con tu E-Mail"]')
        self.input_mail = (By.XPATH, '//android.widget.EditText[@text="Usuario"]')
        self.input_pass = (By.XPATH, '//android.widget.EditText[@text="Contraseña"]')
        self.button_ingresar = (By.XPATH, '//android.widget.TextView[@text="Ingresar"]')
        #DNI
        self.button_ingresa_documento = (By.XPATH, '//android.view.ViewGroup[@content-desc="Ingresá con tu Documento"]')
        self.select_doc = (By.XPATH, '//android.view.ViewGroup[@content-desc="DNI"]/android.widget.TextView')
        self.input_numero_dni = (By.XPATH, '//android.widget.EditText[@text="Número Documento"]')
        self.input_pass_dni = (By.XPATH, '//android.widget.EditText[@text="Contraseña"]')
        self.button_registro =(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]")

    def ingresar_mail(self, usr, pwd):
        time.sleep(5)
        self.driver.find_element(*self.button_ingresa_mail).click()
        time.sleep(5)
        self.driver.find_element(*self.input_mail).send_keys(usr)
        time.sleep(2)
        self.driver.find_element(*self.input_pass).send_keys(pwd)
        time.sleep(2)
        self.driver.find_element(*self.button_ingresar).click()

    def seleccionar_doc_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_doc))
        doc = Select(select_element)
        options = doc.options

        if len(options) > (index + 1):
                doc.select_by_index(index)
        else:
            time.sleep(3)
            doc.select_by_index(index)

    def ingresar_documento(self, usr, pwd):

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_ingresa_documento)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_numero_dni)).send_keys(usr)
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_pass_dni)).send_keys(pwd)
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_registro)).click()

