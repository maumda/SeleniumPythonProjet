# Test Case
# Mauricio Miranda Franco.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

mondriver = webdriver.Chrome()

# Maximizer le navigateur
mondriver.maximize_window()
#Aller sur le site web Google
mondriver.get("https://www.google.com/")

#Trouver la barre de recherche et taper Selenium web driver
mondriver.find_element(By.XPATH,"/html/body/div/div[3]/form/div/div/div/div/div[2]/input").send_keys("Selenium web driver")

# Cliquer sur l'element de la lista
WebDriverWait(mondriver, 2).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/form/div/div/div[2]/div[2]/div[2]/ul/div/ul/li/div/div[2]/div/span"))).click()
time.sleep(4)
#Fermer le navigateur
mondriver.quit()
