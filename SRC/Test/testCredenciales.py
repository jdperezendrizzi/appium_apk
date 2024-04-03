import sys
import unittest
import time
from lib2to3.pgen2 import driver

from appium import webdriver
from selenium.webdriver.common.by import By
# from appium.webdriver.common.mobileby import By
from appium.options.android import UiAutomator2Options
from browserstack.local import Local  # Asegúrate de tener esta importación

# Set your BrowserStack access credentials here
userName = "josedanielpereze_I5UKfk"
accessKey = "hPB87qTygSSwRpUuGdzg"
# Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pageCredenciales import PageCredenciales

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
        "buildName": "TEST-APP-MEDIFE-Credenciales",
        "sessionName": "BStack local_test_Credenciales",
        "local": "true"
    }
})



class TCCredenciales(unittest.TestCase):
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

    # Config del driver
    def setUp(self):
        print("Configurando el entorno de prueba...")

        self.driver = webdriver.Remote(
            command_executor=f"http://{userName}:{accessKey}@hub-cloud.browserstack.com/wd/hub", options=options)

        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_credenciales = PageCredenciales(self.driver)

        self.driver.implicitly_wait(15)

    #@unittest.skip('hecho')
    def test_credenciales_vista(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_credenciales()
        self.page_credenciales.click_aceptar()
        self.page_credenciales.click_vista_credencial()
        self.assertEqual(self.page_credenciales.return_voluntario(), "Voluntario")

    def tearDown(self):
        #self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == '__main__':
    unittest.main()