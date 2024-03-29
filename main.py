"""
Nome do Processo: RPA Challenge
Data de Criação: 20/03/2024

"""

from datetime import datetime
from pathlib import Path
from tasks.log import log_to_file
from tasks.chrome import make_chrome
from tasks.processamento import preenche_formulario
import pandas as pd

timestamp = datetime.now().strftime("%d_%m_%y-%H_%M_%S")
url_site = "https://rpachallenge.com/"

# Construir caminhos dentro do projeto da seguinte forma: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
PATH_LOG = BASE_DIR / 'logs' / f'log_{timestamp}.txt'

FILES = {'entrada': 'challenge.xlsx', 'driver': 'chromedriver.exe',}

# Flag para testes em desenvolvimento
DEBUG = True

try:
    log_to_file(f"Início do processamento", PATH_LOG)
    
    # Cria instância com o webdriver
    bot = make_chrome(BASE_DIR)
    log_to_file('Sessão com o webdriver estabelecida com sucesso', PATH_LOG)

    # Captura dados da planilha de entrada
    dados = pd.read_excel(BASE_DIR / 'files' / f"{FILES['entrada']}")
    log_to_file('Leitura da planilha realizada com sucesso.', PATH_LOG)

    # Entra no site do desafio
    bot.get(url_site)

    # Verifica se a janela carregou com sucesso
    estado_janela = bot.execute_script(f"return document.readyState")

    # Verifica se a página completou o carregamento
    if estado_janela != "complete":
        raise Exception("Página não carregou.")
    log_to_file("Página carregada com sucesso.", PATH_LOG)
    
    # Clica no botão 'Start'
    bot.find_element('xpath', "//button[text() = 'Start']").click()
    log_to_file("Botão Start pressionado com sucesso.", PATH_LOG)

    # Ciclo
    for index, row in dados.iterrows():
        preenche_formulario(bot, index, row, PATH_LOG)
    log_to_file(f"Fim do processamento", PATH_LOG)


except Exception as mensagem_erro:
    log_to_file(mensagem_erro, PATH_LOG)
    bot.get_screenshot_as_file(BASE_DIR / 'print' / f'erro_{timestamp}.png')


finally:
    bot.get_screenshot_as_file(BASE_DIR / 'print' / f'sucesso_{timestamp}.png')
    bot.close()