import sys
from appium import webdriver

# Importaciones de Page
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pagePublic import PagePublic


# Importaciones Modulos
from selenium import webdriver
import unittest

sys.path.append(r"/\\")


class TCLogin(unittest.TestCase):

   def setUp(self):
       """
       # Carga de JSONS
       with open(r"C:/QA_Automation/SRC/datos/Config.Json") as ambiente:
           self.ambiente_webtest = json.loads(ambiente.read())

       with open(r"C:/QA_Automation/SRC/datos/Config.Json") as driver:
           self.driver_locate = json.loads(driver.read())

       with open(r"C:/QA_Automation/SRC/datos/User.Json") as usuario:
           self.diccionario_usuario = json.loads(usuario.read())"""

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
       self.page_login = PageLogin(self.driver)
       self.page_public = PagePublic(self.driver)
       self.driver.implicitly_wait(5)

   #@unittest.skip('ahora no')
   def test_login_mail(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar','Medife23')
        self.assertEqual(self.page_public.return_nombre_usr(), " Ignacio Federico ")
   @unittest.skip('ahora no')
   def test_login_documento(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.seleccionar_doc_por_indice(1)
        self.page_login.ingresar_documento("","")
        self.assertEqual(self.page_public.return_nombre_usr(), " Ignacio Federico ")
   @unittest.skip('ahora no')
   def test_login_google(self):
        self.page_public.ir_a_mi_cuenta()



if __name__ == '__main__':
  unittest.main()