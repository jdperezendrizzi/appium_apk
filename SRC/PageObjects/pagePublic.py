import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PagePublic:
    def __init__(self, my_driver):
        self.driver = my_driver

        # Elementos del Forma
        self.link_mi_cuenta = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.GroupView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]')

        self.button_busca_farmacias = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[1]/android.view.ViewGroup/com.horcrux.svg.SvgView")
        self.button_consulta_cartilla = (By.XPATH, "")
        self.button_cam_doctor = (By.XPATH, '//android.widget.TextView[@text="Cam Doctor"]')
        self.button_urgencias = (By.XPATH, "")
        self.button_credenciales = (By.XPATH, '//android.view.ViewGroup[@content-desc="CREDENCIALES"]')
        self.button_token = (By.XPATH, "")
        self.button_autorizaciones = (By.XPATH, '//android.view.ViewGroup[@content-desc="AUTORIZACIONES"]')
        self.button_facturacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="FACTURACIÓN Y PAGOS"]')
        self.text_nombre_usr = (By.XPATH, '//android.view.ViewGroup[@content-desc=" Ignacio Federico "]/android.widget.TextView')
        self.button_menu = (By.XPATH, '//android.view.ViewGroup[@content-desc=""]')
        self.button_genera_token = (By.XPATH, '//android.widget.Button[@content-desc="Generá un Token"]')
        self.button_beneficios = (By.XPATH, '//android.widget.Button[@content-desc="Beneficios"]')
        self.button_consultas = (By.XPATH, '//android.widget.Button[@content-desc="Consultas y sugerencias"]')
        self.button_asistencia_internacional = (By.XPATH, '//android.widget.Button[@content-desc="Asistencia internacional"]')
        self.button_reserva_turnos = (By.XPATH, '//android.widget.Button[@content-desc="Reserva turnos"]')
        self.button_DNPDP = (By.XPATH, '//android.view.ViewGroup[@content-desc=", DNPDP"]/android.widget.TextView[2]')
        #self.chrome_button_beneficios_cuenta = (By.XPATH, '(//android.view.View)[5]')
        #self.chrome_button_beneficios_cuenta = (By.XPATH, '(//android.view.View[@content-desc="#"])[3]')
        self.chrome_button_beneficios_cuenta = (By.XPATH, '//p[contains(@class, "icon")]')

        self.chrome_beneficios_usr = (By.XPATH, '//div[contains(@class, "user-name")]')




    def click_facturacion(self):
        time.sleep(10)
        self.driver.find_element(*self.button_facturacion).click()

    def ir_a_menu(self):
        time.sleep(10)
        self.driver.find_element(*self.button_menu).click()
    def ir_a_mi_cuenta(self):
        time.sleep(20)
        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.GroupView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView[1]").click()

    def ir_a_autorizaciones(self):
        time.sleep(15)
        self.driver.find_element(*self.button_autorizaciones).click()
    def ir_a_busca_farmacias(self):
        time.sleep(10)
        self.driver.find_element(*self.button_busca_farmacias).click()

    def ir_a_genera_token(self):
        time.sleep(5)
        self.driver.find_element(*self.button_genera_token).click()

    def ir_a_beneficios(self):
        time.sleep(5)
        self.driver.find_element(*self.button_beneficios).click()

    def ir_a_consultas(self):
        time.sleep(5)
        self.driver.find_element(*self.button_consultas).click()

    def ir_a_consulta_cartilla(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_consulta_cartilla)).click()

    def ir_cam_doctor(self):
        self.driver.find_element(*self.button_cam_doctor).click()

    def ir_a_asistencia(self):
        self.driver.find_element(*self.button_asistencia_internacional).click()

    def ir_a_reserva_turnos(self):
        self.driver.find_element(*self.button_reserva_turnos).click()

    def ir_a_credenciales(self):
        time.sleep(20)
        self.driver.find_element(*self.button_credenciales).click()

    def return_nombre_usr(self):
        time.sleep(10)
        return self.driver.find_element(*self.text_nombre_usr).text
        # return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_nombre_usr)).text

    def ir_a_DNPDP(self):
        time.sleep(5)
        self.driver.find_element(*self.button_DNPDP).click()

    def ir_a_chrome_button_beneficios_cuenta(self):
        time.sleep(5)
        self.driver.find_element(*self.chrome_button_beneficios_cuenta).click()

    def return_chrome_beneficios_usr(self):
        time.sleep(10)
        return self.driver.find_element(*self.chrome_beneficios_usr).text






