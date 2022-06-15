import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# Maximizer le navigateur
driver.maximize_window()
# Aller sur le site web
driver.get("http://omayo.blogspot.com")
# DropList
drop_list = driver.find_element(By.ID,"drop1")
drop_list = Select(drop_list)

# Choisir le premier élément
drop_list.select_by_value("def")
time.sleep(2)
# Choisir le deuxième élément
drop_list.select_by_visible_text("doc 2")
time.sleep(2)
# Choisir le troisième élément
drop_list.select_by_index(3)
time.sleep(2)
# Choisir le quatrième élément
drop_list.select_by_visible_text("doc 4")
time.sleep(2)
# Revenir à la valeur par défaut
drop_list.select_by_index(0)


# Multiselect

multi = driver.find_element(By.ID,"multiselect1")
multi = Select(multi)
# Choisir le premier élément
multi.select_by_index(0)
time.sleep(2)
# Choisir le deuxième élément
multi.select_by_value("swiftx")
time.sleep(2)
# Choisir le troisième élément
multi.select_by_visible_text("Hyundai")
time.sleep(2)
# Choisir le quatrième élément
multi.select_by_index(3)
time.sleep(2)
# Désélectionner tous les éléments.
multi.deselect_all()
time.sleep(2)

#Fermer le navigateur
driver.close()