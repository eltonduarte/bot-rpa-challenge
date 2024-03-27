from selenium import webdriver
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import ChromeOptions
from tasks.log import log
# from tasks.chrome import make_chrome


try:

    # Configurações do navegador
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)

    # Configurações do serviço e gerenciador
    servico = Service(ChromeDriverManager().install())
    log("Driver instalado com sucesso.")

    # Cria instância 
    bot = webdriver.Chrome(service=servico, options=opts)
    log("Sessão com driver estabelecida com sucesso.")

    # externalizar o webdriver
    # bot = make_chrome()

    # Leitura da planilha
    dados = pd.read_excel(r"C:\Users\elton.duarte\Downloads\python-rpa\rpa-challange\challenge.xlsx")
    log("Leitura da planilha realizada com sucesso.")

    # Entra no site
    bot.get("https://rpachallenge.com/")

    # https://www.w3schools.com/cssref/css_selectors.php
    # name = bot.execute_script('return document.querySelector("input[ng-reflect-name=labelFirstName]")')
    # name.send_keys('Duarte')

    # Verifica se a janela carregou
    pStrEstadoJanela = bot.execute_script(f"return document.readyState")

    if pStrEstadoJanela != "complete":
        raise Exception("Página não carregou.")
    
    log("Página carregada com sucesso.")

    # Clica no botão 'Start'
    bot.find_element('xpath', "//button[text() = 'Start']").click()
    log("Botão Start pressionado com sucesso.")

    for index, row in dados.iterrows():
        
        log(f"Round {index}")

        # Preenche o campo 'First Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelFirstName']").send_keys(row['First Name'])
        log("Campo 'First Name' preenchido com sucesso.")

        # Preenche o campo 'Last Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelLastName']").send_keys(row['Last Name '])
        log("Campo 'Last Name' preenchido com sucesso.")

        # Preenche o campo 'Phone Number'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelPhone']").send_keys(row['Phone Number'])
        log("Campo 'Phone Number' preenchido com sucesso.")

        # Preenche o campo 'Company Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelCompanyName']").send_keys(row['Company Name'])
        log("Campo 'Company Name' preenchido com sucesso.")

        # Preenche o campo 'Role in Company'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelRole']").send_keys(row['Role in Company'])
        log("Campo 'Role in Company' preenchido com sucesso.")

        # Preenche o campo 'Address'
        bot.find_element('xpath', "//label[text() = 'Address']//following-sibling::input").send_keys(row['Address'])
        log("Campo 'Address' preenchido com sucesso.")

        # Preenche o campo 'Email'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelEmail']").send_keys(row['Email'])
        log("Campo 'Email' preenchido com sucesso.")

        # Clica no botão 'Submit'
        bot.find_element('xpath', "//input[@type = 'submit' or @value = 'submit']").click()
       
except Exception as pStrMensagemErro:
    log(pStrMensagemErro)
    #bot.get_screenshot_as_file(r"C:\Users\epereiradua2\Downloads\python-basico\catho.png")