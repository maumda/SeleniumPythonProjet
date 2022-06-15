import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Créer une instance du web driver
driver = webdriver.Chrome()

# Maximizer le navigateur
driver.maximize_window()

 # Aller sur le site web
driver.get("http://demo.automationtesting.in/Frames.html")

# Trouver le bouton Single frame et le cliquer
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/div/div/ul/li/a").click()

#  Switcher sur le iFrame
driver.switch_to.frame("SingleFrame")
# Trouver la boîte de texte et envoyer une chaîne
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Mon premier text")
# Revenir au cadre par défaut
driver.switch_to.default_content()

# Deuxième Frame
# Trouver le bouton Iframe with in an iframe et le cliquer
driver.find_element(By.XPATH,"/html/body/section/div/div/div/div/div/div/ul/li[2]/a").click()
#  Switcher sur le premier iFrame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[contains(@src, 'MultipleFrames.html')]"))
#  Switcher sur le deuxième iFrame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[contains(@src, 'SingleFrame.html')]"))

# Trouver la boîte de texte et envoyer une chaîne
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("Mon déuxieme text")

time.sleep(2)
# Revenir au cadre par défaut
driver.switch_to.default_content()

#Fermer le navigateur
driver.quit()