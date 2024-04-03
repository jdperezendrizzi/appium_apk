import unittest
import time
from appium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class PageCartilla:
    def __init__(self, my_driver):
        self.driver = my_driver

        # Elementos del Forma
        #cartilla
        self.button_cerrar = (By.ID,"")
        self.button_cartilla = (By.ID, "")
        self.button_especialidad = (By.ID, "")
        self.select_plan = (By.ID, "")
        self.select_rubro = (By.ID, "")
        self.select_especialidad = (By.ID, "")
        self.select_provincia = (By.ID, "")
        self.select_localidad = (By.ID, "")
        self.button_buscar = (By.ID, "")

    def click_cerrar(self):
        time.sleep(10)
        self.driver.find_element(*self.button_cerrar).click()

    def click_cartilla(self):
        time.sleep(10)
        self.driver.find_element(*self.button_cartilla).click()

    def click_especialidad(self):
        time.sleep(10)
        self.driver.find_element(*self.button_especialidad).click()

    def click_buscar(self):
        time.sleep(10)
        self.driver.find_element(*self.button_buscar).click()

    def seleccionar_plan_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_plan))
        plan = Select(select_element)
        options = plan.options

        if len(options) > (index + 1):
                plan.select_by_index(index)
        else:
            time.sleep(3)
            plan.select_by_index(index)

    def seleccionar_localidad_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_localidad))
        localidad = Select(select_element)
        options = localidad.options

        if len(options) > (index + 1):
                localidad.select_by_index(index)
        else:
            time.sleep(3)
            localidad.select_by_index(index)

    def seleccionar_provincia_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_provincia))
        provincia = Select(select_element)
        options = provincia.options

        if len(options) > (index + 1):
                provincia.select_by_index(index)
        else:
            time.sleep(3)
            provincia.select_by_index(index)

    def seleccionar_especialidad_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_especialidad))
        especialidad = Select(select_element)
        options = especialidad.options

        if len(options) > (index + 1):
                especialidad.select_by_index(index)
        else:
            time.sleep(3)
            especialidad.select_by_index(index)

    def seleccionar_rubro_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_rubro))
        rubro = Select(select_element)
        options = rubro.options

        if len(options) > (index + 1):
                rubro.select_by_index(index)
        else:
            time.sleep(3)
            rubro.select_by_index(index)
