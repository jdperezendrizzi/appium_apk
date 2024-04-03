import os
from datetime import datetime
import sys
import HtmlTestRunner

# Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pageCamdoctor import PageCamdoctor

# Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time

sys.path.append(r"/\\")


class TCCamdoctor(unittest.TestCase):

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
        self.page_camdoctor = PageCamdoctor(self.driver)

        #self.screenshot = Screenshot()

        self.driver.implicitly_wait(15)

    @unittest.skip('')
    def test_camdoctor_ver_medico(self):

        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_cam_doctor()
        self.page_camdoctor.click_aceptar_terminos()
        self.page_camdoctor.click_ver_medico()
        self.page_camdoctor.click_paciente()
        self.page_camdoctor.selecciona_especialidad_ver_medico()#no funciona
        self.page_camdoctor.click_siguiente()

    @unittest.skip('hecho')
    def test_camdoctor_agenda_turno(self):

        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_cam_doctor()
        self.page_camdoctor.click_aceptar_terminos()
        self.page_camdoctor.click_agenda_turno()
        self.page_camdoctor.click_paciente()
        self.page_camdoctor.selecciona_especialidad_turno()
        self.page_camdoctor.click_siguiente()



    @unittest.skip('hecho')
    def test_camdoctor_consultas_anteriores(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_cam_doctor()
        self.page_camdoctor.click_aceptar_terminos()
        self.page_camdoctor.click_ver_consultas()
        self.page_camdoctor.click_paciente()
        self.page_camdoctor.click_consulta()

        self.assertEqual(self.page_camdoctor.return_consulta(), "CLINICA ADULTOS")



