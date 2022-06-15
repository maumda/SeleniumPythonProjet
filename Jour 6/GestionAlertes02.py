import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# Maximizer le navigateur
driver.maximize_window()
# Aller sur le site web
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[contains(text(),'Confirm')]").click()
alertWindow = driver.switch_to.alert
print(alertWindow.text)
time.sleep(2)
# Cliquer sur le bouton OK
alertWindow.dismiss()

time.sleep(2)
# driver.find_element(By.XPATH, "html/body/div[2]/div/div/ul/li[3]/button").click()
#Fermer le navigateur
driver.quit()