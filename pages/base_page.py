from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Classe base que todas as páginas herdam. Contém métodos comuns."""

    def __init__(self, driver): #<------ Recebe o driver e cria o WebDriverWait.
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_element(self, locator): 
        """Espera até o elemento estar visível e retorna ele"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_and_click(self, locator):
        """Espera até o elemento estar clicável e clica"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_and_type(self, locator, text):
        """Espera o elemento, limpa e digita o texto"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)