from calendar import c
import unittest
from pyunitreport import HTMLTestRunner  
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class HelloWorld(unittest.TestCase):
#prepara el entorno para realizar la prueba
##Classmethod permite ejecutar en 1 venta 
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        goo = Service('primer_ejercicio\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=goo, options=options)
        driver = cls.driver
        driver.implicitly_wait(10)
#caso de prueba para automatizar tareas
    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
    def test_hello_world(self):
       driver = self.driver
       driver.get('https://www.wikipedia.org')

    
#acciones para finalizar, o evitar fuga de recursos. cerrando buscador.
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello-world-report'))
