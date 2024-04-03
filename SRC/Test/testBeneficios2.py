import os
from datetime import datetime
import sys
import HtmlTestRunner
from urllib.parse import urlparse, parse_qs, urlunparse
from appium.options.android import UiAutomator2Options
from browserstack.local import Local  # Asegúrate de tener esta importación
import time

# Set your BrowserStack access credentials here
userName = "josedanielpereze_I5UKfk"
accessKey = "hPB87qTygSSwRpUuGdzg"
# Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pageBeneficios import PageBeneficios

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
        "buildName": "TEST-APP-MEDIFE-Beneficios",
        "sessionName": "BStack local_test_Beneficios",
        "local": "true"
    }
})


class TCBeneficios(unittest.TestCase):
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

        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)


        #self.screenshot = Screenshot()

        self.driver.implicitly_wait(15)

    #@unittest.skip('')
    def test_beneficios(self):

        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')
        #self.page_login.ingresar_mail('medifeapptest58@medife.com.ar', 'Medife23')

        self.page_public.ir_a_menu()
        self.page_public.ir_a_beneficios()

        time.sleep(20)

        contextos = self.driver.contexts

        for contexto in contextos:
            if "WEBVIEW_chrome" in contexto:
                self.driver.switch_to.context(contexto)

        time.sleep(30)
        self.page_public.ir_a_chrome_button_beneficios_cuenta()

        self.assertEqual("IGNACIO FEDERICO RAVA", self.page_public.return_chrome_beneficios_usr())


        self.driver.quit()