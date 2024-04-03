import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options
from browserstack.local import Local  # Asegúrate de tener esta importación
from appium.webdriver.common.mobileby import MobileBy
#from selenium import webdriver
import unittest
import time

# Set your BrowserStack access credentials here
userName = "josedanielpereze_I5UKfk"
accessKey = "hPB87qTygSSwRpUuGdzg"

# Importaciones de Page
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pagePublic import PagePublic

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
        "buildName": "TEST-APP-MEDIFE-WebExternas",
        "sessionName": "BStack local_test_WebExternas",
        "local": "true"
    }
})

class TCWebExternas(unittest.TestCase):
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

        # Config de Pages
        self.page_login = PageLogin(self.driver)
        self.page_public = PagePublic(self.driver)
        self.driver.implicitly_wait(15)

    def test_DNPDP(self):

        self.page_public.ir_a_menu()

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("DNPDP"))')

        self.page_public.ir_a_DNPDP()
        time.sleep(15)

        contextos = self.driver.contexts

        for contexto in contextos:
            if "WEBVIEW_chrome" in contexto:
                self.driver.switch_to.context(contexto)

        url_actual = self.driver.current_url
        self.assertEqual("https://www.argentina.gob.ar/aaip/datospersonales", url_actual)

        self.driver.quit()



