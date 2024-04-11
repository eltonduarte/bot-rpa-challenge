from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def object_exists(bot, xpath):
    """ Verifica se um elemento está presente no DOM de uma página. 
    Isso não significa necessariamente que o elemento esteja visível.
    Retorna True quando o título corresponde, False caso contrário.
    """
    
    try: 
        WebDriverWait(bot, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except:
        return False


def window_exists(bot, title):
    """ Verifica se o título da página contém o texto. 
    Retorna True quando o título corresponde, False caso contrário
    """
    
    try:
        WebDriverWait(bot, 5).until(EC.title_contains(title))
        return True
    except:
        return False

    