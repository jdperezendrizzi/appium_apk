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


class PageAutorizaciones:

    def __init__(self, my_driver):
        self.driver = my_driver

        #solicitar
        self.button_solicitar= (By.XPATH, '//android.view.ViewGroup[@content-desc="SOLICITAR"]')
        self.button_entendido = (By.XPATH, '//android.view.ViewGroup[@content-desc=" ENTENDIDO "]')
        self.select_practica = (By.XPATH, '//android.view.ViewGroup[@content-desc="Seleccioná la práctica médica"]')
        self.option_practica = (By.XPATH, '//android.view.ViewGroup[@content-desc="Internación sin materiales"]')
        self.button_iniciar_autorizacion =(By.XPATH, '//android.view.ViewGroup[@content-desc="INICIAR AUTORIZACIÓN"]/android.widget.TextView')
        self.select_integrante = (By.XPATH, '//android.view.ViewGroup[@content-desc="Selecciona el integrante"]')
        self.option_integrante = (By.XPATH, '//android.view.ViewGroup[@content-desc="RAVA FEDERICO"]') # este no se si funque
        self.button_confirmar_asociado = (By.XPATH, '//android.view.ViewGroup[@content-desc="CONFIRMAR ASOCIADO"]')
        self.input_cantidad_sesiones = (By.XPATH, '//android.view.ViewGroup[@content-desc="5"]/android.widget.TextView')

        self.button_enviar_solicitud = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.Button")
        self.text_comprobante_solicitud = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]")
        self.button_institucion = (By.XPATH, '(//android.view.ViewGroup[@content-desc=""])[7]')
        self.input_institucion = (By.XPATH, "//*[contains(@class, 'EditText') and contains(@text, 'Ingrese Institución')]")
        self.button_fecha = (By.XPATH, "//android.widget.Button[not(contains(@content-desc, 'no disponible'))][1]")
        self.button_confirmar_datos = (By.XPATH, '//android.view.ViewGroup[@content-desc="CONFIRMAR DATOS"]')
        self.input_adjunto_1 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 1"]')
        self.input_adjunto_2 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 2"]')
        self.input_adjunto_3 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 3"]')
        self.input_adjunto_4 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 4"]')
        self.input_adjunto_5 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 5"]')
        self.input_adjunto_6 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 6"]')
        self.input_adjunto_7 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 7"]')
        self.input_adjunto_8 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 8"]')
        self.input_adjunto_9 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 9"]')
        self.input_adjunto_10 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 10"]')
        self.input_adjunto_11 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 11"]')
        self.input_adjunto_12 = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="addDocumentBtn 12"]')

        #salud mental
        self.card_salud_mental = (By.XPATH, '//android.view.ViewGroup[@content-desc="Salud mental"]/android.view.ViewGroup/android.widget.TextView')
        self.option_flap = (By.XPATH, '//android.view.ViewGroup[@content-desc="FLAP / Fisurados"]/android.widget.TextView')
        self.option_psicoterapia_individual = (By.XPATH, '//android.view.ViewGroup[@content-desc="Psicoterapia  Individual"]')
        self.button_inicio = (By.XPATH, '//android.view.ViewGroup[@content-desc="Inicio o Continuidad de Tratamiento, 8 prácticas"]')
        self.input_fecha_orden_mental = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 8"])')
        self.input_fecha_prueba_mental = (By.XPATH, '//android.widget.EditText[@resource-id="inputCalendarBtn id 223"]')
        self.button_email_mental = (By.XPATH, '//android.view.ViewGroup[@resource-id="btnHandleFieldEdition id 10"]')
        self.input_email_mental = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 10"]')
        self.input_prueba = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[4]/android.view.ViewGroup/com.horcrux.svg.SvgView/com.horcrux.svg.GroupView/com.horcrux.svg.PathView")
        self.button_prueba = (By.XPATH, "//android.widget.Button[not(contains(@content-desc, 'no disponible'))][1]")
        self.button_camara = (By.XPATH, '//android.view.ViewGroup[@content-desc="Cámara"]')
        self.button_permitir_medife = (By.ID, 'com.android.permissioncontroller:id/permission_allow_one_time_button')
        self.button_permitir_contenido = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
        self.button_captura= (By.XPATH, '//android.widget.ImageButton[@content-desc="Capturar"]')
        self.button_aceptar_foto = (By.ID, "com.motorola.camera3:id/stage1_layout")
        self.button_explorar = (By. XPATH, '//android.view.ViewGroup[@content-desc="Explorar Archivos..."]')
        self.button_archivo = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.GridView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView")
        self.button_enviar_sol = (By.XPATH, '//android.view.ViewGroup[@content-desc="ENVIAR SOLICITUD"]')

        #internacion/cirugia
        self.card_internacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="Internación / Cirugía"]')
        self.button_internac_sinmat =(By.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Internación sin materiales")]')
        self.option_internacion_sin = (By.XPATH, '//android.view.ViewGroup[@content-desc="Internación sin materiales"]')
        self.input_orden_internacion = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[7]/android.view.View")
        self.input_estudios_previos = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[9]/android.view.View/android.widget.TextView")
        self.button_internac_conmat = (By.XPATH, '//android.view.ViewGroup[contains(@content-desc, "Internación con materiales")]')
        self.input_fecha_orden_internacion = (By.XPATH, '//android.widget.EditText[@resource-id="inputCalendarBtn id 4"]')
        self.input_fecha_intern_internacion = (By.XPATH, '//android.widget.EditText[@resource-id="inputCalendarBtn id 46"]')
        self.button_telefono_internacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 6"]')
        self.input_telefono_internacion = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 6"]')
        self.button_email_internacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 7"]')
        self.button_institucion_internacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 5"]')
        self.input_email_internacion = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 7"]')
        self.input_institucion_internacion = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 5"]')

        # practicas medicas
        self.card_practicas_medicas = (By.XPATH, '//android.view.ViewGroup[@content-desc="Prácticas médicas"]')
        self.button_imagenes = (By.XPATH, '//android.view.ViewGroup[@content-desc="Imágenes, 7 prácticas"]')
        self.option_estudios_mamarios = (By.XPATH, '//android.view.ViewGroup[@content-desc="Estudios mamarios marcaciones"]')
        self.input_fecha_medicas = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 1"])')
        self.input_email_medicas = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 2"]')
        self.button_email_medicas = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 2"]')

        #salud sexual integral
        self.card_salud_sexual = (By.XPATH, '//android.view.ViewGroup[@content-desc="Salud sexual integral"]')
        self.button_anticoncepcion = (By.XPATH, '//android.view.ViewGroup[@content-desc="Anticoncepción, 4 prácticas"]')
        self.option_DIU = (By.XPATH, '//android.view.ViewGroup[@content-desc="DIU"]')
        self.button_email_salud_sexual = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 66"]')
        self.input_email_salud_sexual = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 66"]')
        self.button_telefono_salud_sexual = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 67"]')
        self.input_telefono_salud_sexual = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 67"]')
        self.button_medico_salud_sexual = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 69"]')
        self.input_medico_salud_sexual = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 69"]')
        self.button_tel_medico_salud_sexual = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 68"]')
        self.input_tel_medico_salud_sexual = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 68"]')
        self.button_matricula_salud_sexual = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 70"]')
        self.input_matricula_salud_sexual = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 70"]')

        #fertilidad
        self.card_fertilidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="Fertilidad"]')
        self.option_tratamientos = (By.XPATH, '//android.view.ViewGroup[@content-desc="Tratamientos, 2 prácticas"]/android.view.ViewGroup/android.widget.TextView[1]')
        self.option_baja_complejidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="Tratamientos de Baja Complejidad"]/android.widget.TextView')
        self.input_fecha_orden_fertilidad = (By.XPATH, '//android.widget.EditText[@resource-id="inputCalendarBtn id 37"]')
        self.button_email_fertilidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 39"]')
        self.input_email_fertilidad = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 39"]')
        self.button_telefono_fertilidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 38"]')
        self.input_telefono_fertilidad = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 38"]')

        #discapacidad
        self.card_discapacidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="Discapacidad"]')
        self.button_plan_anual = (By.XPATH, '//android.view.ViewGroup[@content-desc="Plan anual, 6 prácticas"]')
        self.option_rehabilitacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="Prestaciones de Rehabilitación"]')
        self.input_certif_discapacidad = (By.XPATH, '(//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandle"])')
        self.button_telefono_discapacidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 40"]')
        self.input_telefono_discapacidad = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 40"]')
        self.button_email_discapacidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 41"]')
        self.input_email_discapacidad = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 41"]')
        self.button_nombre_discapacidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 42"]')
        self.input_nombre_discapacidad = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 42"]')
        self.button_telpres_discapacidad = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 43"]')
        self.input_telpres_discapacidad = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 43"]')

        #Traslados programados
        self.card_traslados_programados = (By.XPATH, '//android.view.ViewGroup[@content-desc="Traslados programados"]/android.view.ViewGroup/android.widget.TextView')
        self.button_traslados = (By.XPATH, '//android.view.ViewGroup[@content-desc="Traslados programados, 2 prácticas"]/android.view.ViewGroup/android.widget.TextView[1]')
        self.input_orden_medica = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.widget.TextView")
        self.option_traslados = (By.XPATH, '//android.view.ViewGroup[@content-desc="Traslados programados"]/android.widget.TextView')
        self.button_email_traslados = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 45"]')
        self.input_email_traslados = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 45"]')
        self.input_fecha_traslados = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 44"])')


        #diabetes
        self.card_diabetes = (By.XPATH, '//android.view.ViewGroup[@content-desc="Diabetes"]')
        self.button_empadronamiento = (By.XPATH, '//android.view.ViewGroup[@content-desc="Empadronamiento, 1 práctica"]')
        self.input_lab_diab = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.view.View")
        self.input_medicformdiab = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.widget.TextView")
        self.option_empadronamiento = (By.XPATH, '//android.view.ViewGroup[@content-desc="Empadronamiento"]')
        self.button_telefono_diabetes = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 78"]')
        self.input_telefono_diabetes = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 78"]')
        self.input_email_diabetes = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 77"]')
        self.button_email_diabetes = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 77"]')

        #Medicación
        self.card_medicacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="Medicación"]')
        self.button_leches = (By.XPATH, '//android.view.ViewGroup[@content-desc="Leches, 1 práctica"]')
        self.option_leches = (By.XPATH, '//android.view.ViewGroup[@content-desc="Leches"]')
        self.input_formulario_310 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[8]/android.view.View/android.widget.TextView')
        self.input_email_medicacion = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 71"]')
        self.button_email_medicacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 71"]')
        self.button_telefono_medicacion = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 72"]')
        self.input_telefono_medicacion = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 72"]')

        #solicitud de receta
        self.card_solicitud_receta = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[6]/android.view.View/android.view.View/android.widget.TextView")
        self.button_receta_web = (By.XPATH, '//android.view.View[@content-desc="Receta desde la web"]/android.widget.TextView')
        self.input_docu_receta = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View/android.widget.TextView')

        #bariátrica
        self.card_bariatrica = (By.XPATH, '//android.view.ViewGroup[@content-desc="Bariátrica"]')
        self.button_bariatrica = (By.XPATH, '//android.view.ViewGroup[@content-desc="Bariátrica, 1 práctica"]')
        self.option_bariatrica = (By.XPATH, '//android.view.ViewGroup[@content-desc="Bariátrica"]')
        self.input_email_bar = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 28"]')
        self.button_email_bar = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 28"]')
        self.input_fecha_bar = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 25"])')
        self.input_fecha_cirugia_bar = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 26"])')
        self.input_institucion_bar = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 27"]')
        self.button_institucion_bar = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 27"]')

        #Insumos
        self.card_insumos = (By.XPATH, '//android.view.ViewGroup[@content-desc="Insumos"]/android.view.ViewGroup/android.widget.TextView')
        self.button_descartables = (By.XPATH, '//android.view.ViewGroup[@content-desc="Descartables, 1 práctica"]/android.view.ViewGroup/android.widget.TextView[1]')
        self.input_orden_insumos = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[8]/android.view.View/android.widget.TextView")
        self.option_descartables = (By. XPATH, '//android.view.ViewGroup[@content-desc="Descartables"]')
        self.input_fecha_insumos = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 19"])')
        self.button_email_insumos = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 20"]')
        self.input_email_insumos = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 20"]')
        self.input_telefono_insumos = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 21"]')
        self.button_telefono_insumos = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 21"]')

        #Prácticas odontológicas
        self.card_practicas_odontologicas = (By.XPATH, '//android.view.ViewGroup[@content-desc="Prácticas odontológicas"]/android.view.ViewGroup/android.widget.TextView')
        self.button_flap = (By.XPATH, '//android.view.ViewGroup[@content-desc="FLAP / Fisurados, 1 práctica"]/android.view.ViewGroup/android.widget.TextView[1]')
        self.input_fecha_odonto = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 14"])')
        self.input_fecha_internacion_odonto = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 17"])')
        self.input_localidad_odonto = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 16"]')
        self.button_localidad_odonto = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 16"]')
        self.input_prueba_odonto = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 203"]')
        self.button_prueba_odonto = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 203"]')
        self.input_email_odonto = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 15"]')
        self.button_email_odonto = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 15"]')

        #Órtesis
        self.card_ortesis =(By.XPATH, '//android.view.ViewGroup[@content-desc="Órtesis"]')
        self.button_otras_ortesis = (By.XPATH, '//android.view.ViewGroup[@content-desc="Otras órtesis, 1 práctica"]/android.view.ViewGroup/android.widget.TextView[1]')
        self.option_otras_ortesis = (By.XPATH, '//android.view.ViewGroup[@content-desc="Otras órtesis"]')
        self.input_fecha_ortesis = (By.XPATH, '(//android.widget.EditText[@resource-id="inputCalendarBtn id 32"])')
        self.input_email_ortesis = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 34"]')
        self.button_email_ortesis = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 34"]')
        self.input_telefono_ortesis = (By.XPATH, '//android.widget.EditText[@resource-id="textInput id 33"]')
        self.button_telefono_ortesis = (By.XPATH, '//android.view.ViewGroup[@content-desc="" and @resource-id="btnHandleFieldEdition id 33"]')

        #consultar
        self.button_consultar = (By.XPATH, '//android.view.ViewGroup[@content-desc="mpB0"]/android.view.ViewGroup/android.view.ViewGroup[1]')

    def click_solicitar(self):
        time.sleep(10)
        self.driver.find_element(*self.button_solicitar).click()
    def click_card_salud_mental(self):
        time.sleep(7)
        self.driver.find_element(*self.card_salud_mental).click()

    def click_inicio_tratamiento(self):
        time.sleep(7)
        self.driver.find_element(*self.button_inicio).click()

    def click_card_internacion(self):
        time.sleep(7)
        self.driver.find_element(*self.card_internacion).click()

    def click_card_practicas_medicas(self):
        time.sleep(7)
        self.driver.find_element(*self.card_practicas_medicas).click()

    def click_card_salud_sexual(self):
        time.sleep(7)
        self.driver.find_element(*self.card_salud_sexual).click()

    def click_card_fertilidad(self):
        time.sleep(7)
        self.driver.find_element(*self.card_fertilidad).click()

    def click_card_traslados_programados(self):
        time.sleep(7)
        self.driver.find_element(*self.card_traslados_programados).click()

    def click_card_diabetes(self):
        time.sleep(7)
        self.driver.find_element(*self.card_diabetes).click()
    def click_card_medicacion(self):
        time.sleep(7)
        self.driver.find_element(*self.card_medicacion).click()
    def click_card_discapacidad(self):
        time.sleep(7)
        self.driver.find_element(*self.card_discapacidad).click()

    def click_card_solicitud_receta(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_solicitud_receta)).click()

    def click_card_bariatrica(self):
        time.sleep(7)
        self.driver.find_element(*self.card_bariatrica).click()

    def click_card_insumos(self):
        time.sleep(7)
        self.driver.find_element(*self.card_insumos).click()
    def click_card_odontologicas(self):
        time.sleep(7)
        self.driver.find_element(*self.card_practicas_odontologicas).click()

    def click_card_ortesis(self):
        time.sleep(7)
        self.driver.find_element(*self.card_ortesis).click()

    def click_otras_ortesis(self):
        time.sleep(7)
        self.driver.find_element(*self.button_otras_ortesis).click()

    def click_traslados(self):
        time.sleep(5)
        self.driver.find_element(*self.button_traslados).click()

    def click_descartables(self):
        time.sleep(5)
        self.driver.find_element(*self.button_descartables).click()

    def click_flap(self):
        time.sleep(5)
        self.driver.find_element(*self.button_flap).click()

    def click_entendido(self):
        time.sleep(5)
        self.driver.find_element(*self.button_entendido).click()

    def click_consultar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_consultar)).click()


    def seleccionar_practica_salud_mental(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_psicoterapia_individual).click()

    def seleccionar_practica_diabetes(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_empadronamiento).click()


    def seleccionar_practica_medicacion(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_leches).click()

    def seleccionar_practica_ortesis(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_otras_ortesis).click()


    def seleccionar_practica_bariatrica(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_bariatrica).click()

    def seleccionar_practica_discapacidad(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_rehabilitacion).click()

    def seleccionar_practica_odontologicas(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_flap).click()

    def seleccionar_practica_insumos(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(10)
        self.driver.find_element(*self.option_descartables).click()

    def seleccionar_practica_traslados(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_traslados).click()

    def seleccionar_practica_salud_sexual(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_DIU).click()

    def seleccionar_practica_internacion(self):
        time.sleep(7)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(7)
        self.driver.find_element(*self.option_internacion_sin).click()

    def seleccionar_practica_fertilidad(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_baja_complejidad).click()

    def seleccionar_practica_medicas(self):
        time.sleep(5)
        self.driver.find_element(*self.select_practica).click()
        time.sleep(5)
        self.driver.find_element(*self.option_estudios_mamarios).click()



    def click_iniciar_autorizacion(self):
        self.driver.find_element(*self.button_iniciar_autorizacion).click()

    def click_confirmar_datos(self):
        time.sleep(3)
        self.driver.find_element(*self.button_confirmar_datos).click()

    def seleccionar_integrante(self):
        time.sleep(10)
        self.driver.find_element(*self.select_integrante).click()
        time.sleep(10)
        self.driver.find_element(*self.option_integrante).click()
        time.sleep(5)
        self.driver.find_element(*self.button_confirmar_asociado).click()

    '''def ingresar_fecha_orden_medica(self, diasAtras):
        ahora = datetime.now()
        fecha = ahora - timedelta(days=diasAtras)
        fecha_sin_hora = fecha.strftime("%d/%m/%Y") #23/02/2023
        self.driver.find_element(*self.input_fecha_orden).send_keys(fecha_sin_hora)'''

    def ingresar_fecha_orden_insumos(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_insumos).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_medicas(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_medicas).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_orden_bar(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_bar).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_orden_ortesis(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_ortesis).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_orden_odonto(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_odonto).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_orden_salud_mental(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_orden_mental).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_orden_traslados(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_traslados).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_internacion_odonto(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_internacion_odonto).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_cirugia_bar(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_cirugia_bar).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_orden_internacion(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_orden_internacion).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()


    def ingresar_fecha_orden_fertilidad(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_orden_fertilidad).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_intern_internacion(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_intern_internacion).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_fecha_prueba_mental(self):
        time.sleep(5)
        self.driver.find_element(*self.input_fecha_prueba_mental).click()
        time.sleep(5)
        self.driver.find_element(*self.button_fecha).click()

    def ingresar_cant_sesiones(self):
        time.sleep(3)
        self.driver.find_element(*self.input_cantidad_sesiones).click()

    def ingresar_email_odonto(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_odonto).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_odonto).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_odonto).click()

    def ingresar_email_medicas(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_medicas).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_medicas).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_medicas).click()

    def ingresar_email_diabetes(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_diabetes).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_diabetes).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_diabetes).click()

    def ingresar_email_medicacion (self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_medicacion).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_medicacion).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_medicacion).click()

    def ingresar_email_ortesis(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_ortesis).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_ortesis).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_ortesis).click()

    def ingresar_email_bariatrica(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_bar).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_bar).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_bar).click()

    def ingresar_email_internacion(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_internacion).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_internacion).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_internacion).click()

    def ingresar_email_discapacidad(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_discapacidad).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_discapacidad).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_discapacidad).click()

    def ingresar_email_fertilidad(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_fertilidad).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_fertilidad).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_fertilidad).click()

    def ingresar_email_salud_sexual(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_salud_sexual).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_salud_sexual).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_salud_sexual).click()

    def ingresar_email_traslados(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_traslados).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_traslados).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_traslados).click()

    def ingresar_email_asociado_salud_mental(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_mental).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_mental).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_mental).click()

    def ingresar_email_insumos(self, mail):
        time.sleep(3)
        self.driver.find_element(*self.button_email_insumos).click()
        time.sleep(3)
        self.driver.find_element(*self.input_email_insumos).send_keys(mail)
        time.sleep(2)
        self.driver.find_element(*self.button_email_insumos).click()

    def ingresar_prueba_odonto(self, prueba):
        time.sleep(3)
        self.driver.find_element(*self.button_prueba_odonto).click()
        time.sleep(3)
        self.driver.find_element(*self.input_prueba_odonto).send_keys(prueba)
        time.sleep(2)
        self.driver.find_element(*self.button_prueba_odonto).click()


    def adjuntar_salud_mental(self):
        time.sleep(5)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(5)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(3)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_medicas(self):
        time.sleep(5)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(5)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(3)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(5)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(5)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(3)
        self.driver.find_element(*self.button_archivo).click()


    def adjuntar_ortesis(self):
        time.sleep(5)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(5)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(3)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(5)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(5)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(3)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_practicas_odonto(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(7)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_fertilidad(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_3).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_4).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_5).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_6).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_7).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
    def adjuntar_salud_sexual(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_3).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_internacion(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_docu_discapacidad(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_3).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_4).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_5).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_6).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_7).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_8).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_9).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_10).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_11).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_salud_sexual(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_3).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
    def adjuntar_docu_bariatrica(self):
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_3).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_4).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_5).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_6).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_7).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_8).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_9).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(2)
        self.driver.find_element(*self.input_adjunto_10).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()


    def adjuntar_diabetes(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(7)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_docu_insumos(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(7)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_traslados(self):
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(3)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(3)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(2)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_medicacion(self):
        time.sleep(5)
        self.driver.find_element(*self.input_adjunto_1).click()
        time.sleep(5)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(3)
        self.driver.find_element(*self.button_archivo).click()
        time.sleep(5)
        self.driver.find_element(*self.input_adjunto_2).click()
        time.sleep(5)
        self.driver.find_element(*self.button_explorar).click()
        time.sleep(3)
        self.driver.find_element(*self.button_archivo).click()

    def adjuntar_docu_receta(self, adjunto):
        docu_receta = self.driver.find_element(*self.input_docu_receta)
        docu_receta .send_keys(adjunto['doc_adicional'])

    def click_enviar_solicitud(self):
        time.sleep(3)
        self.driver.find_element(*self.button_enviar_sol).click()

    def return_comprob_solic_autorizacion(self):
        time.sleep(5)
        return self.driver.find_element(*self.text_comprobante_solicitud).text

    def click_internac_sinmat(self):
        time.sleep(5)
        self.driver.find_element(*self.button_internac_sinmat).click()

    def click_imagenes(self):
        time.sleep(3)
        self.driver.find_element(*self.button_imagenes).click()

    def click_anticoncepcion(self):
        time.sleep(3)
        self.driver.find_element(*self.button_anticoncepcion).click()

    def click_leches(self):
        time.sleep(3)
        self.driver.find_element(*self.button_leches).click()
    def click_tratamientos(self):
        time.sleep(3)
        self.driver.find_element(*self.option_tratamientos).click()

    def click_plan_anual(self):
        time.sleep(3)
        self.driver.find_element(*self.button_plan_anual).click()
    def click_empadronamiento(self):
        time.sleep(3)
        self.driver.find_element(*self.button_empadronamiento).click()
    def click_receta_web(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_receta_web)).click()

    def click_bariatrica(self):
        time.sleep(3)
        self.driver.find_element(*self.button_bariatrica).click()

    def ingresar_telefono_discapacidad(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_discapacidad).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_discapacidad).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_discapacidad).click()


    def ingresar_telefono_diabetes(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_diabetes).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_diabetes).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_diabetes).click()

    def ingresar_telefono_medicacion(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_medicacion).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_medicacion).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_medicacion).click()

    def ingresar_telefono_ortesis(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_ortesis).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_ortesis).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_ortesis).click()
    def ingresar_telefono_bar(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_bar).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_bar).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_bar).click()


    def ingresar_telefono_insumos(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_insumos).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_insumos).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_insumos).click()

    def ingresar_telefono_internacion(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_internacion).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_internacion).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_internacion).click()

    def ingresar_telefono_salud_sexual(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_salud_sexual).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_salud_sexual).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_salud_sexual).click()

    def ingresar_medico_salud_sexual(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_medico_salud_sexual).click()
        time.sleep(3)
        self.driver.find_element(*self.input_medico_salud_sexual).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_medico_salud_sexual).click()


    def click_autorizaciones(self, index):
        time.sleep(3)
        self.driver.find_element(By.XPATH, f'(//android.view.ViewGroup[@content-desc=""])[{index}]').click()

    def ingresar_telefono_fertilidad(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telefono_fertilidad).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_fertilidad).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telefono_fertilidad).click()

    def ingresar_nombre_discapacidad(self, nombre):
        time.sleep(3)
        self.driver.find_element(*self.button_nombre_discapacidad).click()
        time.sleep(3)
        self.driver.find_element(*self.input_nombre_discapacidad).send_keys(nombre)
        time.sleep(2)
        self.driver.find_element(*self.button_nombre_discapacidad).click()

    def ingresar_tel_pres_discapacidad(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_telpres_discapacidad).click()
        time.sleep(3)
        self.driver.find_element(*self.input_telpres_discapacidad).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_telpres_discapacidad).click()

    def ingresar_telefono_medico(self, telefono, index):
        time.sleep(3)
        self.driver.find_element(By.XPATH, f'(//android.view.ViewGroup[@content-desc=""])[{index}]').click()
        time.sleep(3)
        self.driver.find_element(*self.input_telefono_medico).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.click_blank).click()

    def ingresar_tel_medico_salud_sexual(self, telefono):
        time.sleep(3)
        self.driver.find_element(*self.button_tel_medico_salud_sexual).click()
        time.sleep(3)
        self.driver.find_element(*self.input_tel_medico_salud_sexual).send_keys(telefono)
        time.sleep(2)
        self.driver.find_element(*self.button_tel_medico_salud_sexual).click()

    def ingresar_matricula_salud_sexual(self, matricula):
        time.sleep(3)
        self.driver.find_element(*self.button_matricula_salud_sexual).click()
        time.sleep(3)
        self.driver.find_element(*self.input_matricula_salud_sexual).send_keys(matricula)
        time.sleep(2)
        self.driver.find_element(*self.button_matricula_salud_sexual).click()


    def ingresar_localidad_odonto(self, localidad):
        time.sleep(3)
        self.driver.find_element(*self.button_localidad_odonto).click()
        time.sleep(3)
        self.driver.find_element(*self.input_localidad_odonto).send_keys(localidad)
        time.sleep(2)
        self.driver.find_element(*self.button_localidad_odonto).click()


    def ingresar_institucion(self, institucion, index):
        time.sleep(3)
        self.driver.find_element(By.XPATH, f'(//android.view.ViewGroup[@content-desc=""])[{index}]').click()
        time.sleep(3)
        self.driver.find_element(*self.input_institucion).send_keys(institucion)
        time.sleep(2)
        self.driver.find_element(*self.click_blank).click()

    def ingresar_institucion_internacion(self, institucion):
        time.sleep(3)
        self.driver.find_element(*self.button_institucion_internacion).click()
        time.sleep(3)
        self.driver.find_element(*self.input_institucion_internacion).send_keys(institucion)
        time.sleep(2)
        self.driver.find_element(*self.button_institucion_internacion).click()

    def ingresar_institucion_bariatrica(self, institucion):
        time.sleep(3)
        self.driver.find_element(*self.button_institucion_bar).click()
        time.sleep(3)
        self.driver.find_element(*self.input_institucion_bar).send_keys(institucion)
        time.sleep(2)
        self.driver.find_element(*self.button_institucion_bar).click()


