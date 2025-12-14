# SauceDemo Automation Framework

Framework de automação de testes **end-to-end** para o site demo [SauceDemo](https://www.saucedemo.com).

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.25-green)
![PyTest](https://img.shields.io/badge/PyTest-9.0-orange)
![POM](https://img.shields.io/badge/Page%20Object%20Model-Professional-lightgrey)

## Descrição
Projeto desenvolvido como portfólio profissional para demonstrar domínio em automação de testes web com boas práticas de mercado:
- **Page Object Model (POM)** para código limpo, reutilizável e fácil de manter
- Esperas inteligentes (Explicit Wait)
- Configuração robusta do driver (bloqueio de popups do Chrome)
- Testes com PyTest

## Funcionalidades automatizadas
- Login válido com validação da página de produtos
- Logout
- Login inválido com validação da mensagem de erro

## Estrutura do projeto
.
├── pages/                  # Page Objects (BasePage, LoginPage, InventoryPage)
├── tests/                  # Testes PyTest
├── conftest.py             # Configuração centralizada do driver
└── README.md


## Como executar localmente
```bash
git clone https://github.com/rrr4fsz/saucedemo-automation-pom.git
cd saucedemo-automation-pom
python -m venv venv
venv\Scripts\activate
pip install selenium pytest webdriver-manager
pytest tests/test_login.py -v -s
```

Autor
Rudson Rafael Bragança Bahiense
Analista de Sistemas | Quality Assurance | Automação de Testes
Rio de Janeiro – Dezembro 2025
GitHub: github.com/rrr4fsz
E-mail: Rudson.Bahiense@gmail.com
LinkedIn: /in/rudson-rafael-bragança-bahiense-a8ab78209.
