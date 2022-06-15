import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Lancer le navigateur
driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

# Maximizer le navigateur
driver.maximize_window()

# On utilise le localisateur Link_Test et l'action click.
driver.find_element(By.LINK_TEXT, "Log in").click()

# On utilise le localisateur Partial Link_Test avec juste une partie du nom de l'élement et après l'action click.
#driver.find_element(By.PARTIAL_LINK_TEXT, "Regi").click()

driver.find_element(By.ID, "Email").send_keys("maucito12@outlook.com")
driver.find_element(By.ID, "Password").send_keys("F$#f437yf9")


driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()






time.sleep(4)
driver.close()
