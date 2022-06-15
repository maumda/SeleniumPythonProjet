import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Créer une instance du web driver
driver = webdriver.Chrome()

# Maximizer le navigateur
driver.maximize_window()

 # Aller sur le site web
driver.get("https://opensource-demo.orangehrmlive.com/")

parentwindowId = driver.current_window_handle
print(parentwindowId)
# Résultat obtenu CDwindow-D26576B1278A30F1049283068CE88B48

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

# Recuperer la liste des fénetres ouvertes
windowhandleIds = driver.window_handles

parentwindowId = windowhandleIds[0]
childwindowId = windowhandleIds[1]
print("Parent Window ID : ",parentwindowId)
print("Child Window ID : ",childwindowId)

driver.switch_to.window(childwindowId)
print(driver.current_url)
title1 = driver.title

for winId in windowhandleIds:
    driver.switch_to.window(winId)
    if driver.title == title1:
        driver.close()

time.sleep(2)

#Fermer le navigateur
driver.quit()