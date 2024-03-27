from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions

class nossa_classe:

    # Factory: Função que retorna um objeto
    @staticmethod
    def criar_navegador() -> webdriver.Chrome:
        _service = Service(executable_path=r"C:\Users\elton.duarte\Downloads\python-rpa\gui\chromedriver.exe")
        _options = ChromeOptions()
        _options.add_experimental_option("detach", True)
        navegador = webdriver.Chrome(service=_service, options=_options)
        return navegador
