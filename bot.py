from datetime import datetime
from pathlib import Path
from tasks.log import log_to_file
from tasks.chrome import make_chrome
import pandas as pd

timestamp = datetime.now().strftime("%d_%m_%y-%H_%M_%S")
url_site = "https://rpachallenge.com/"

BASE_DIR = Path(__file__).resolve().parent
PATH_LOG = BASE_DIR / 'logs' / f'log_{timestamp}.txt'


try:
    # Cria instância com o webdriver
    bot = make_chrome(BASE_DIR)
    log_to_file('Sessão com o webdriver estabelecida com sucesso', PATH_LOG)

    # Captura dados da planilha de entrada
    dados = pd.read_excel(BASE_DIR / 'files' / 'challenge.xlsx')
    log_to_file('Leitura da planilha realizada com sucesso.', PATH_LOG)

    # Entra no site do desafio
    bot.get(url_site)

    # Verifica se a janela carregou com sucesso
    estado_janela = bot.execute_script(f"return document.readyState")

    if estado_janela != "complete":
        raise Exception("Página não carregou.")
    
    
    
    log_to_file("Página carregada com sucesso.", PATH_LOG)
    
    # Clica no botão 'Start'
    bot.find_element('xpath', "//button[text() = 'Start']").click()
    log_to_file("Botão Start pressionado com sucesso.", PATH_LOG)

    for index, row in dados.iterrows():
        
        log_to_file(f"Round {index}", PATH_LOG)

        # Preenche o campo 'First Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelFirstName']").send_keys(row['First Name'])
        log_to_file("Campo 'First Name' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Last Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelLastName']").send_keys(row['Last Name '])
        log_to_file("Campo 'Last Name' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Phone Number'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelPhone']").send_keys(row['Phone Number'])
        log_to_file("Campo 'Phone Number' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Company Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelCompanyName']").send_keys(row['Company Name'])
        log_to_file("Campo 'Company Name' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Role in Company'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelRole']").send_keys(row['Role in Company'])
        log_to_file("Campo 'Role in Company' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Address'
        bot.find_element('xpath', "//label[text() = 'Address']//following-sibling::input").send_keys(row['Address'])
        log_to_file("Campo 'Address' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Email'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelEmail']").send_keys(row['Email'])
        log_to_file("Campo 'Email' preenchido com sucesso.", PATH_LOG)

        # Clica no botão 'Submit'
        bot.find_element('xpath', "//input[@type = 'submit' or @value = 'submit']").click()

except Exception as mensagem_erro:
    log_to_file(mensagem_erro, PATH_LOG)
    bot.get_screenshot_as_file(BASE_DIR / 'print' / f'erro_{timestamp}.png')

finally:
    bot.close()