import os
from datetime import datetime
import sys
import HtmlTestRunner
from urllib.parse import urlparse, parse_qs, urlunparse

# Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin

# Importaciones Modulos
from appium import webdriver
import unittest
import json
import time

sys.path.append(r"/\\")


class TCReservaturnos(unittest.TestCase):

    def setUp(self):

        # Config del driver
        options = {
            "platformName": "Android",
            "appium:platformVersion": "12",
            "appium:deviceName": "ZY22F89WP3",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.medife.mobile",
            "appium:appActivity": ".MainActivity",
            # Especifica la ruta al chromedriver descargado
            "chromedriverExecutable": "C:\App_Medife\SRC\chromedriver.exe"}

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options)


        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)

        #self.screenshot = Screenshot()

        self.driver.implicitly_wait(15)

    #@unittest.skip('')
    def test_reserva_turnos(self):

        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_menu()
        self.page_public.ir_a_reserva_turnos()


        try:
            time.sleep(7)
            contextos = self.driver.contexts

            for contexto in contextos:
                if "WEBVIEW" in contexto:
                    self.driver.switch_to.context(contexto)

            url_actual = self.driver.current_url

            parsed_url = urlparse(url_actual)
            query_params = parse_qs(parsed_url.query)
            del query_params['token']  # Eliminar el parámetro token

            # Reconstruir la URL sin el token
            new_query_string = '&'.join([f"{key}={','.join(value)}" for key, value in query_params.items()])
            new_url = urlunparse((
                parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string,
                parsed_url.fragment))

            self.assertEqual("https://webtest.medife.com.ar/portal/sucursales?tipo=a&tab=turnos", new_url)
        except Exception as e:
            # Manejar cualquier excepción
            print("Ocurrió un error:", e)

        finally:
            # Cambiar de vuelta a los contextos originales y cerrar la sesión de Selenium WebDriver
            for contexto in contextos:
                self.driver.switch_to.context(contexto)

            self.driver.quit()
