from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_valido_e_invalido(driver):
    """Teste completo: login válido → verifica página de produtos → logout → login inválido → verifica erro"""
    
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    # Abre a página de login
    login_page.open()
    
    # ================= LOGIN VÁLIDO =================
    login_page.perform_login("standard_user", "secret_sauce")
    
    # Valida que entrou na página de produtos
    assert inventory_page.is_products_page_displayed(), "Falha: Não entrou na página de produtos"
    print("✓ Login válido funcionou!")
    
    # Faz logout
    inventory_page.open_menu()
    inventory_page.click_logout()
    print("✓ Logout realizado com sucesso!")
    
    # ================= LOGIN INVÁLIDO =================
    login_page.perform_login("standard_user", "senha_errada")
    
    # Valida mensagem de erro
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text, f"Erro inesperado: {error_text}"
    print("✓ Login inválido funcionou! Mensagem de erro correta apareceu.")
    
    print("TESTE CONCLUÍDO COM SUCESSO!")