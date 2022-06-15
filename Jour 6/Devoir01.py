import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# Maximizer le navigateur
driver.maximize_window()
# Aller sur le site web
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# Trouver le bouton Prompt
driver.find_element(By.XPATH,"//button[contains(text(),'Prompt')]").click()
# Switch vers l'alert
alertWindow = driver.switch_to.alert
time.sleep(2)
# Envoyer du texte vers l'alerte
alertWindow.send_keys("Bonjour Mauricio")
time.sleep(2)
# Cliquer sur OK
alertWindow.accept()

time.sleep(2)
#Fermer le navigateur
driver.quit()