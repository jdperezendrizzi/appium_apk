from datetime import datetime
import sys
import HtmlTestRunner

# Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pageCartilla import PageCartilla

# Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time

#Importaciones Helpers
#from SRC.Helpers.screenshot import Screenshot

sys.path.append(r"/\\")


class TCCartilla(unittest.TestCase):

    def setUp(self):

        # Config del driver
        options = {
            "platformName": "Android",
            "appium:platformVersion": "12",
            "appium:deviceName": "ZY22F89WP3",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.medife.mobile",
            "appium:appActivity": ".MainActivity"
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options)


        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_cartilla = PageCartilla(self.driver)

        #self.screenshot = Screenshot()

        self.driver.implicitly_wait(15)

    def test_consulta_cartilla_especialidad(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_consulta_cartilla()
        self.page_cartilla.click_cerrar()
        self.page_cartilla.click_cartilla()
        self.page_cartilla.click_especialidad()
        self.page_cartilla.seleccionar_plan_por_indice(1)
        self.page_cartilla.seleccionar_rubro_por_indice(1)
        self.page_cartilla.seleccionar_especialidad_por_indice(1)
        self.page_cartilla.seleccionar_provincia_por_indice(1)
        self.page_cartilla.seleccionar_localidad_por_indice(1)
        self.page_cartilla.click_buscar()