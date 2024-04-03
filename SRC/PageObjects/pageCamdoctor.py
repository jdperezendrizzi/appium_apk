import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException as ECIE, ElementNotInteractableException, \
    NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
from datetime import timedelta
import random


class PageCamdoctor:

    def __init__(self, my_driver):
        self.driver = my_driver

        #Ver medico ahora
        self.check_terminos = (By.XPATH, '//android.widget.CheckBox[@content-desc=""]')
        self.button_aceptar = (By.XPATH, '//android.view.ViewGroup[@content-desc="Aceptar"]')
        self.button_ver_medico = (By.XPATH, '//android.view.ViewGroup[@content-desc="Ver un médico ahora, Videollamada..."]')
        self.button_federico = (By.XPATH, '//android.view.ViewGroup[contains(@content-desc, "FEDERICO RAVA")]')
        self.button_especialidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="Seleccioná una especialidad"]/android.widget.TextView')
        self.button_odontologia= (By.XPATH, '//android.view.ViewGroup[@content-desc="ODONTOLOGIA"]/android.widget.TextView')

        #Agendá un turno
        self.button_agenda_turno= (By.XPATH, '//android.view.ViewGroup[@content-desc="Agendar un turno, Consultas programadas en..."]')
        self.button_chequeo= (By.XPATH, '//android.view.ViewGroup[@content-desc="CHEQUEO DE SALUD"]/android.widget.TextView')
        self.button_siguiente= (By.XPATH, '//android.widget.Button[@content-desc="SIGUIENTE0"]/android.widget.TextView')
        self.text_turno= (By.XPATH, '//android.widget.TextView[@text="No existen turnos disponibles en este momento, modifica tu consulta o vuelve a intentar más tarde."]')

        #Ver consultas anteriores
        self.button_ver_consultas= (By.XPATH, '//android.view.ViewGroup[@content-desc="Ver consultas anteriores , Accede a tu historial de consultas"]')
        self.button_consulta= (By.XPATH, '//android.view.ViewGroup[@content-desc="Consulta de CLINICA ADULTOS, 12/02/2021 11:37 hs"]')
        self.text_clinica = (By.XPATH, '//android.widget.TextView[@text="CLINICA ADULTOS"]')

    def click_aceptar_terminos(self):
        time.sleep(7)
        self.driver.find_element(*self.check_terminos).click()
        time.sleep(3)
        self.driver.find_element(*self.button_aceptar).click()

    def click_ver_medico(self):
        time.sleep(3)
        self.driver.find_element(*self.button_ver_medico).click()

    def click_ver_consultas(self):
        time.sleep(3)
        self.driver.find_element(*self.button_ver_consultas).click()


    def return_turno(self):
        time.sleep(5)
        return self.driver.find_element(*self.text_turno).text

    def return_consulta(self):
        time.sleep(5)
        return self.driver.find_element(*self.text_clinica).text

    def click_agenda_turno(self):
        time.sleep(3)
        self.driver.find_element(*self.button_agenda_turno).click()

    def click_paciente(self):
        time.sleep(3)
        self.driver.find_element(*self.button_federico).click()

    def click_consulta(self):
        time.sleep(3)
        self.driver.find_element(*self.button_consulta).click()

    def click_siguiente(self):
        time.sleep(3)
        self.driver.find_element(*self.button_siguiente).click()

    def selecciona_especialidad_turno(self):
        time.sleep(3)
        self.driver.find_element(*self.button_especialidad).click()
        time.sleep(3)
        self.driver.find_element(*self.button_chequeo).click()

    def selecciona_especialidad_ver_medico(self):
        time.sleep(3)
        self.driver.find_element(*self.button_especialidad).click()
        time.sleep(3)
        self.driver.find_element(*self.button_odontologia).click()


