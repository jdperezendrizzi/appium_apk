import os
from datetime import datetime
import sys
import HtmlTestRunner
from selenium import webdriver
from appium.options.android import UiAutomator2Options
from browserstack.local import Local  # Asegúrate de tener esta importación

# Set your BrowserStack access credentials here
userName = "josedanielpereze_I5UKfk"
accessKey = "hPB87qTygSSwRpUuGdzg"

# Importaciones de Page
from SRC.PageObjects.pagePublic import PagePublic
from SRC.PageObjects.pageLogin import PageLogin
from SRC.PageObjects.pageAutorizaciones import PageAutorizaciones

# Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time

#Importaciones Helpers
#from SRC.Helpers.screenshot import Screenshot

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
        "buildName": "TEST-APP-MEDIFE-Autorizaciones",
        "sessionName": "BStack local_test_Atorizaciones",
        "local": "true"
    }
})

class TCAutorizaciones(unittest.TestCase):
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
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_autorizaciones = PageAutorizaciones(self.driver)

        #self.screenshot = Screenshot()

        self.driver.implicitly_wait(15)

    @unittest.skip('hecho')
    def test_autorizaciones_solicitar_salud_mental(self):

        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        self.page_autorizaciones.click_card_salud_mental()
        self.page_autorizaciones.click_inicio_tratamiento()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_salud_mental()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_salud_mental()
        self.page_autorizaciones.ingresar_cant_sesiones()
        self.page_autorizaciones.ingresar_email_asociado_salud_mental("test@test.com")
        self.page_autorizaciones.ingresar_fecha_prueba_mental()
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_salud_mental()
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(), "¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('hecho')
    def test_autorizaciones_solicitar_practicas_internacion(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        self.page_autorizaciones.click_card_internacion()
        #scroll
        self.page_autorizaciones.click_internac_sinmat()
        #scroll
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_internacion()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_internacion()
        self.page_autorizaciones.ingresar_fecha_intern_internacion()
        self.page_autorizaciones.ingresar_telefono_internacion("1156739865")
        self.page_autorizaciones.ingresar_email_internacion("test@test.com")
        self.page_autorizaciones.ingresar_institucion_internacion("clinica")
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_internacion()
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),"¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('falta scroll')
    def test_autorizaciones_solicitar_practicas_medicas(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        #scroll
        self.page_autorizaciones.click_card_practicas_medicas()
        self.page_autorizaciones.click_imagenes()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_medicas()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_medicas()
        self.page_autorizaciones.ingresar_email_medicas("test@test.com")
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_medicas()
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),
                         "¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('hecho')
    def test_autorizaciones_solicitar_practicas_salud_sexual(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        self.page_autorizaciones.click_card_salud_sexual()
        #aca va scroll
        self.page_autorizaciones.click_anticoncepcion()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_salud_sexual()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_email_salud_sexual("test@test.com")
        self.page_autorizaciones.ingresar_telefono_salud_sexual(1158748334)
        self.page_autorizaciones.ingresar_medico_salud_sexual("Ruben")
        self.page_autorizaciones.ingresar_tel_medico_salud_sexual(1158748332)
        self.page_autorizaciones.ingresar_matricula_salud_sexual("Fghdu123")
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_salud_sexual()
        #acá va scroll
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),   "¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('falta scroll')
    def test_autorizaciones_solicitar_practicas_fertilidad(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        #scroll
        self.page_autorizaciones.click_card_fertilidad()
        self.page_autorizaciones.click_tratamientos()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_fertilidad()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_fertilidad()
        self.page_autorizaciones.ingresar_email_fertilidad("test@test.com")
        self.page_autorizaciones.ingresar_telefono_fertilidad("1156739865")
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_fertilidad() #falta scroll en adjuntos
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),   "¡Tu solicitud fue iniciada con éxito!")

   # @unittest.skip('falta scroll')
    def test_autorizaciones_solicitar_discapacidad(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        #scroll
        self.page_autorizaciones.click_card_discapacidad()
        self.page_autorizaciones.click_plan_anual()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_discapacidad()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_telefono_discapacidad(1158748332)
        self.page_autorizaciones.ingresar_email_discapacidad("test@test.com")
        self.page_autorizaciones.ingresar_nombre_discapacidad("Roberto")
        self.page_autorizaciones.ingresar_tel_pres_discapacidad(1154678934)
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_docu_discapacidad() #aca van 2 scroll

        self.page_autorizaciones.click_enviar_solicitud()
        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),  "¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('cambio adjuntos-se repite campo VTV')
    def test_autorizaciones_solicitar_practicas_traslados(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        self.page_autorizaciones.click_card_traslados_programados()
        self.page_autorizaciones.click_traslados()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_traslados()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_traslados()
        self.page_autorizaciones.ingresar_email_traslados("test@test.com")
        self.page_autorizaciones.click_confirmar_datos()
        self.page_autorizaciones.adjuntar_traslados()

        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),
                         "¡Tu solicitud fue iniciada con éxito!")
   # @unittest.skip('falta scroll')
    def test_autorizaciones_solicitar_practicas_diabetes(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        #scroll
        self.page_autorizaciones.click_card_diabetes()
        self.page_autorizaciones.click_empadronamiento()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_diabetes()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_telefono_diabetes(1158748332)
        self.page_autorizaciones.ingresar_email_diabetes("test@test.com")
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_diabetes()
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),
                         "¡Tu solicitud fue iniciada con éxito!")
   # @unittest.skip('hecho')
    def test_autorizaciones_solicitar_practicas_medicacion(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        #scroll
        self.page_autorizaciones.click_card_medicacion()
        self.page_autorizaciones.click_leches()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_medicacion()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_email_medicacion("test@test.com")
        self.page_autorizaciones.ingresar_telefono_medicacion(1158748332)
        #scroll
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_medicacion()
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),
                     "¡Tu solicitud fue iniciada con éxito!")
   # @unittest.skip('no está mas')
    def test_autorizaciones_solicitar_receta(self):
        usr = self.diccionario_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_autorizaciones.click_solicitar()
        self.page_autorizaciones.click_card_solicitud_receta()
        self.page_autorizaciones.click_receta_web()
        self.page_autorizaciones.seleccionar_practica_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante(1)

        adjunto = {'doc_adicional': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}
        self.page_autorizaciones.adjuntar_docu_receta(adjunto)
        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),"Comprobante de Solicitud de autorización")

    #@unittest.skip('Falta scroll')
    def test_autorizaciones_solicitar_practicas_bariatrica(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        self.page_autorizaciones.click_card_bariatrica()
        self.page_autorizaciones.click_bariatrica()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_bariatrica()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_bar()
        self.page_autorizaciones.ingresar_fecha_cirugia_bar()
        self.page_autorizaciones.ingresar_email_bariatrica("test@test.com")
        self.page_autorizaciones.ingresar_institucion_bariatrica("clinica")
        #aca va el scroll
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_docu_bariatrica() #va scroll

        self.page_autorizaciones.click_enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),
                         "¡Tu solicitud fue iniciada con éxito!")

   # @unittest.skip('falta scroll en cards')
    def test_autorizaciones_solicitar_practicas_insumos(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        #scroll
        self.page_autorizaciones.click_card_insumos()
        self.page_autorizaciones.click_descartables()
        self.page_autorizaciones.click_entendido()
        self.page_autorizaciones.seleccionar_practica_insumos()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_insumos()
        self.page_autorizaciones.ingresar_email_insumos("test@test.com")
        self.page_autorizaciones.ingresar_telefono_insumos("1156739865")
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_docu_insumos()

        self.page_autorizaciones.click_enviar_solicitud()
        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),
                         "¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('falta scroll')
    def test_autorizaciones_solicitar_practicas_odontologicas(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        self.page_autorizaciones.click_card_odontologicas()
        self.page_autorizaciones.click_flap()
        self.page_autorizaciones.seleccionar_practica_odontologicas()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_odonto()
        self.page_autorizaciones.ingresar_fecha_internacion_odonto()
        self.page_autorizaciones.ingresar_localidad_odonto("lugar")
        self.page_autorizaciones.ingresar_prueba_odonto("prueba")
        self.page_autorizaciones.ingresar_email_odonto("test@test.com")
        #self.page_autorizaciones.scroll_formulario_odonto()

        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_practicas_odonto()
        #scroll en adjuntos
        self.page_autorizaciones.click_enviar_solicitud()
        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),"¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('Falta scroll')
    def test_autorizaciones_solicitar_practicas_ortesis(self):
        self.page_public.ir_a_mi_cuenta()
        self.page_login.ingresar_mail('medifeapptest86@medife.com.ar', 'Medife23')

        self.page_public.ir_a_autorizaciones()
        self.page_autorizaciones.click_autorizaciones(2)
        #aca va scroll
        self.page_autorizaciones.click_card_ortesis()
        self.page_autorizaciones.click_otras_ortesis()
        self.page_autorizaciones.seleccionar_practica_ortesis()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante()
        self.page_autorizaciones.ingresar_fecha_orden_ortesis()
        self.page_autorizaciones.ingresar_email_ortesis("test@test.com")
        self.page_autorizaciones.ingresar_telefono_ortesis("1156739865")
        self.page_autorizaciones.click_confirmar_datos()

        self.page_autorizaciones.adjuntar_ortesis()

        self.page_autorizaciones.click_enviar_solicitud()
        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(),
                         "¡Tu solicitud fue iniciada con éxito!")

    #@unittest.skip('no está mas')
    def test_autorizaciones_solicitar_medife_mama(self):
        usr = self.diccionario_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_medife_mama()
        self.page_autorizaciones.click_modificar_plan()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        time.sleep(5)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        time.sleep(10)
        self.page_autorizaciones.enviar_solicitud()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(),
                         "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_consultar(self):

        usr = self.diccionario_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_consultar_autorizacion()
        time.sleep(10)
        self.page_autorizaciones.click_ver_detalle()
        time.sleep(10)

        self.assertEqual(self.page_autorizaciones.return_detalle_de_autorizacion(), "Detalle de la autorización")

    def tearDown(self):
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
