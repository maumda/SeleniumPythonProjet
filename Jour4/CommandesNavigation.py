# Test Case
import time
from selenium import webdriver

# Lancer le navigateur
mondriver = webdriver.Chrome()

# Maximizer le navigateur
mondriver.maximize_window()

mondriver.get("https://demo.nopcommerce.com/")
time.sleep(2)

mondriver.get("https://www.google.com/")
time.sleep(2)

mondriver.back()
time.sleep(2)

mondriver.forward()
time.sleep(2)

mondriver.refresh()
time.sleep(2)

# Fermer le navigateur
# mondriver.close()