from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


@staticmethod
def make_chrome(path) -> webdriver.Chrome:
   
    _service = Service(executable_path = path / 'files' / 'chromedriver.exe')
    _service_manager = Service(ChromeDriverManager().install())
    
    _options = ChromeOptions()
    _options.add_experimental_option("detach", True)
    
    _navegador = webdriver.Chrome(service = _service, options = _options)
   
    return _navegador
