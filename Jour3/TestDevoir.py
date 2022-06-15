# Test Case
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Lancer le navigateur
driver = webdriver.Chrome()

# Aller sur le site web
driver.get("https://www.saucedemo.com/")

# Maximizer le navigateur
driver.maximize_window()

# Soumettre des informations d'identification
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Cliquer sur le bouton de Login
driver.find_element(By.ID, "login-button").click()

# Ajouter produit au panier
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

# Aller sur le panier
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


time.sleep(2)

# Cliquer sur le bouton Checkout
driver.find_element(By.ID, "checkout").click()


# Remplir formulaire de Checkout
driver.find_element(By.ID, "first-name").send_keys("Mauricio")
driver.find_element(By.ID, "last-name").send_keys("Miranda  ")
driver.find_element(By.ID, "postal-code").send_keys("J3Z 2F5")

# Cliquer sur le bouton Continuer
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# Cliquer sur le bouton Finish
driver.find_element(By.ID, "finish").click()
time.sleep(4)

# Fermer le navigateur
driver.close()