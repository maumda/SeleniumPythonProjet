# Test Case
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Lancer le navigateur
mondriver = webdriver.Chrome()

# Maximizer le navigateur
mondriver.maximize_window()

mondriver.get("https://demo.nopcommerce.com/")


# Obtenir l'URL de la page
urlpage = mondriver.current_url
print(urlpage)

# Obtenir le title de la page
titlepage = mondriver.title
print(titlepage)

# Obtenir le code source de la page
codepage = mondriver.page_source
print(codepage)

time.sleep(2)
# Fermer le navigateur
mondriver.close()