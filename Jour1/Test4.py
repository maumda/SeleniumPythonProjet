import time
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

#service_obj = Service("/Users/mauriciomiranda/Downloads/Drivers/chromedriver")
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
#driver = webdriver.Chrome(service=service_obj) #Créer objet de type Chrome
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
driver = webdriver.Chrome() #On remplace 2 lignes pour une! Juste en collant le chromedrive sur le dossier bin de Python

driver.get("https://login.salesforce.com/")
driver.maximize_window()
# 3) Entrer username (Admin)
driver.find_element(By.ID, "username").send_keys("mau_moda")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "password").send_keys("mau12345")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "Login").click()
# 6) recuperer le titre de la page(titre actuel)
act_title =  driver.title

# 7) Verifier le titre de la page: OrangeHRM  (attendu)
exp_title = "Login | Salesforce"
if act_title == exp_title:
    print("Le test Login  est passed")
else:
    print("Le test Login  est failed")

exp_msg_error=driver.find_element(By.ID,"chooser_error").text
print("Le message d'erreur est: " + exp_msg_error)

try:
    print(By.ID,"error")
except Exception as e:\
    print(repr(e))

time.sleep(4)
# 8) Fermer le navigateur
driver.close()