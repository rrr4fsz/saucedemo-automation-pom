from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    """Página de produtos (inventory) do SauceDemo – contém ações e validações após login"""

    # Localizadores corretos
    PRODUCTS_TITLE = (By.XPATH, "//span[text()='Products']")  # XPath correto para o título
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")             # Botão hambúrguer
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")              # Link de logout

    def is_products_page_displayed(self):
        """Verifica se o título 'Products' está visível – confirma que o login deu certo"""
        try:
            self.wait_for_element(self.PRODUCTS_TITLE)
            return True
        except:
            return False

    def open_menu(self):
        """Abre o menu lateral clicando no botão hambúrguer"""
        self.wait_and_click(self.MENU_BUTTON)

    def click_logout(self):
        """Clica no link de Logout (deve ser chamado após open_menu)"""
        self.wait_and_click(self.LOGOUT_LINK)