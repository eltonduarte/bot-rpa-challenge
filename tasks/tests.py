from tasks.chrome import nossa_classe
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# https://www.w3schools.com/cssref/css_selectors.php
# name = bot.execute_script('return document.querySelector("input[ng-reflect-name=labelFirstName]")')
# name.send_keys('Duarte')


url = "https://doodles.google/"
bot = nossa_classe.criar_navegador()
bot.get(url)


'''  
No código abaixo, o Selenium aguardará no máximo 10 segundos para que um elemento que corresponda aos critérios especificados seja encontrado
Espere para encontrar o input
Espere... até... o elemento esteja presente na tel 
''' 
    # search_input = WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
    # print(search_input)


pagina_carregada = WebDriverWait(bot, 1).until(EC.title_contains('Certsys'))

#teste
print(pagina_carregada)
    



