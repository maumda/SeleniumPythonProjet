
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# Maximizer le navigateur
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")

drop_country = driver.find_element(By.ID,"input-country")
country = Select(drop_country)

# Sélection par texte visible
# country.select_by_visible_text("Mexico")

# Sélection par indice
# country.select_by_index(142)

# Inspecter le select avec la liste de pays et sélectionner par value
# country.select_by_value("142")

all_options = country.options
print(len(all_options))

 # for opt in (all_options):
 #     print(opt.text)

for opt in(all_options):
    if opt.text == "Mexico":
        opt.click()
        break


time.sleep(2)

#Fermer le navigateur
driver.close()
