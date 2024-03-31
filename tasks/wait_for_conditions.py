from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def object_exists(bot, xpath):
    """ Verificaa se um elemento está presente no DOM de um
    página. Isso não significa necessariamente que o elemento esteja visível.
    retorna True quando o título corresponde, False caso contrário
    """
    try: 
        WebDriverWait(bot, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except:
        return False


def window_exists(bot, title):
    """ Verificar se o título da página contém o texto
    retorna True quando o título corresponde, False caso contrário
    """
    try:
        WebDriverWait(bot, 5).until(EC.title_contains(title))
        return True
    except:
        return False

    