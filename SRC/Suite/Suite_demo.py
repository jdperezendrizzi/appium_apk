import unittest
import sys
sys.path.append(r"C:\App_Medife")
import HtmlTestRunner

# Importo los TestCase
from SRC.Test.testLogin import TCLogin
from SRC.Test.testCredenciales import TCCredenciales
from SRC.Test.testFacturacion import TCFacturacion


# Crear una instancia de TestLoader
test_loader = unittest.TestLoader()

## Carga de tests específicos
test_suite = unittest.TestSuite()
test_suite.addTest(TCLogin('test_login_mail'))
test_suite.addTest(TCCredenciales('test_credenciales_vista'))
test_suite.addTest(TCFacturacion('test_facturacion_pagar_efectivo'))


# Ejecuta la suite de pruebas
test_runner = unittest.TextTestRunner()
# test_runner.run(test_suite)
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Test Completos", add_timestamp=False).run(test_suite)
