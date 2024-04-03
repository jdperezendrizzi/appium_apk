#Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time
import sys

#Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin
#from SRC.PageObjects.Modulos.pageHome import PageHome
from SRC.PageObjects.pageFacturacion import PageFacturacion

sys.path.append(r"/\\")


class TCFacturacion (unittest.TestCase):

    def setUp(self):
        '''# Carga de JSONS
        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as ambiente:
            self.ambiente_webtest = json.loads(ambiente.read())

        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"C:/QA_Automation/SRC/datos/User.Json") as usuario:
            self.dic_usuario = json.loads(usuario.read())

        # Config del driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # --headless #--start-maximized
        options.add_argument("incognito")  # --headless #--start-maximized
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.ambiente_webtest["ambiente"][0])'''

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

        self.driver.implicitly_wait(15)

        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)
        #self.page_home = PageHome(self.driver)
        self.page_facturacion = PageFacturacion(self.driver)

    #@unittest.skip("ahora no")
    def test_facturacion_pagar_efectivo(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.click_facturacion()
        self.page_facturacion.click_pagar()
        self.page_facturacion.click_efectivo()
        self.page_facturacion.click_galicia()
        self.assertEqual(self.page_facturacion.return_instrucciones_pago(),"INSTRUCCIONES PARA PAGO")


    def tearDown(self):
        #self.driver.close()
        self.driver.quit()
        print("Test Completo")
