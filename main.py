"""
Treinamento Python RPA
Nome do Processo: RPA Challenge
Data de Criação: 20/03/2024
"""

from datetime import datetime
from pathlib import Path
from tasks.log import log_to_file
from tasks.chrome import make_chrome
from tasks.processamento import *
from tasks.wait_for_conditions import *
import pandas as pd

timestamp = datetime.now().strftime("%d_%m_%y-%H_%M_%S")
url_site = "https://rpachallenge.com/"

# Construir caminhos dentro do projeto da seguinte forma: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
PATH_LOG = BASE_DIR / 'logs' / f'log_{timestamp}.csv'

FILES = {'entrada': 'challenge.xlsx', 'driver': 'chromedriver.exe',}

# Flag para testes em desenvolvimento
DEBUG = True

def main():
    try:
        # INÍCIO
        log_to_file(f'Início do processamento', PATH_LOG)
        
        bot = make_chrome(BASE_DIR)
        log_to_file(f'Sessão com o webdriver estabelecida com sucesso', PATH_LOG)

        dados = pd.read_excel(BASE_DIR / 'files' / f"{FILES['entrada']}")
        log_to_file(f'Leitura da planilha realizada com sucesso.', PATH_LOG)

        # PROCESSAMENTO
        bot.get(url_site)

        # Verifica se o objeto existe na página
        if not object_exists(bot = bot, xpath = "//button[text() = 'Start']"): 
            raise Exception('Botão Start não existe')
        
        # Verifica o titulo da janela
        if not window_exists(bot = bot, title = "Rpa"): 
            raise Exception('Janela Rpa Challeng não existe')
        
        log_to_file(f'{url_site} carregado com sucesso', PATH_LOG)

        # Verifica estado da janela
        estado_janela = bot.execute_script(f"return document.readyState")
        if estado_janela != 'complete':
            raise Exception('Página não carregou')
        
        log_to_file('Página carregada com sucesso', PATH_LOG)
        
        bot.find_element('xpath', "//button[text() = 'Start']").click()
        log_to_file('Botão Start pressionado com sucesso', PATH_LOG)

        for index, row in dados.iterrows():
            preenche_formulario(bot, index, row, PATH_LOG)

        # FIM
        log_to_file(f"Fim do processamento", PATH_LOG)

    except Exception as mensagem_erro:
        log_to_file(mensagem_erro, PATH_LOG)
    
    finally:
        bot.get_screenshot_as_file(BASE_DIR / 'print' / f'sucesso_{timestamp}.png')
        bot.close()


if __name__ == "__main__":
    main()