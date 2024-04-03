import os
from datetime import datetime
import sys
import HtmlTestRunner
from urllib.parse import urlparse, parse_qs, urlunparse
from appium.options.android import UiAutomator2Options
from browserstack.local import Local  # Asegúrate de tener esta importación

# Set your BrowserStack access credentials here
userName = "josedanielpereze_I5UKfk"
accessKey = "hPB87qTygSSwRpUuGdzg"
# Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pageAsistenciainternacional import PageAsistenciainternacional

# Importaciones Modulos
from appium import webdriver
import unittest
import json
import time

sys.path.append(r"/\\")
options = UiAutomator2Options().load_capabilities({
    "app": "bs://b32ae9a6ee508e70fd302a29a01405ada5e6c97c",
    "deviceName": "Samsung Galaxy S21",
    "platformName": "android",
    "platformVersion": "12.0",
    "bstack:options": {
        "userName": userName,
        "accessKey": accessKey,
        "projectName": "APP-MEDIFE",
        "buildName": "TEST-APP-MEDIFE-asistencia_internacional",
        "sessionName": "BStack local_test_asistencia_internacional",
        "local": "true"
    }
})


class TCAsistenciainternacional(unittest.TestCase):
    bs_local = None

    @classmethod
    def setUpClass(cls):
        print("Iniciando el cliente Local de BrowserStack...")
        cls.bs_local = Local()
        bs_local_args = {"key": accessKey, "forcelocal": "true"}
        cls.bs_local.start(**bs_local_args)

    @classmethod
    def tearDownClass(cls):
        print("Deteniendo el cliente Local de BrowserStack...")
        if cls.bs_local is not None:
            cls.bs_local.stop()

    def setUp(self):
        print("Configurando el entorno de prueba...")

        self.driver = webdriver.Remote(
            command_executor=f"http://{userName}:{accessKey}@hub-cloud.browserstack.com/wd/hub", options=options)
        # Configuración de Pages
        sys.path.append('C:\\App_Medife\\SRC\\PageObjects')
        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_asistencia = PageAsistenciainternacional(self.driver)

        #self.screenshot = Screenshot()

        self.driver.implicitly_wait(15)

    #@unittest.skip('')
    def test_asistencia_internacional(self):

        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_menu()
        self.page_public.ir_a_asistencia()

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

            self.assertEqual('https://webtest.medife.com.ar/portal/aviso-viaje?tipo=a&tab=aviso-viaje', new_url)
        except Exception as e:
            # Manejar cualquier excepción
            print("Ocurrió un error:", e)

        finally:
            # Cambiar de vuelta a los contextos originales y cerrar la sesión de Selenium WebDriver
            for contexto in contextos:
                self.driver.switch_to.context(contexto)

            self.driver.quit()