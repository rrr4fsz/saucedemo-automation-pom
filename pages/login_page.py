from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Página de login do SauceDemo – contém todos os elementos e ações relacionadas ao login"""

    # Localizadores (tuplas com By e valor)
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self, url="https://www.saucedemo.com"):
        """Abre a página de login"""
        self.driver.get(url)

    def perform_login(self, username, password):
        """Preenche usuário/senha e clica no botão de login"""
        self.wait_and_type(self.USERNAME_FIELD, username)
        self.wait_and_type(self.PASSWORD_FIELD, password)
        self.wait_and_click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Retorna o texto da mensagem de erro"""
        error_element = self.wait_for_element(self.ERROR_MESSAGE)
        return error_element.text

    def is_error_displayed(self):
        """Verifica se a mensagem de erro está visível (útil para asserções)"""
        try:
            self.wait_for_element(self.ERROR_MESSAGE)
            return True
        except:
            return False