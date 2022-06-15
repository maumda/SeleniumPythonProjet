import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# Maximizer le navigateur
driver.maximize_window()
# Aller sur le site web
# driver.get("https://the-internet.herokuapp.com/basic_auth")

# Envoyer le user et password par URL
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(2)
# driver.find_element(By.XPATH, "html/body/div[2]/div/div/ul/li[3]/button").click()
#Fermer le navigateur
driver.quit()