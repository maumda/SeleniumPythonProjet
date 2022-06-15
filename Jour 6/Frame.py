import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


# Maximizer le navigateur
driver.maximize_window()

 # Aller sur le site web
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

#  On doit switcher sur le iFrame
driver.switch_to.frame("packageListFrame")
# Cliquer sur une option
driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
# Sortir du frame
driver.switch_to.default_content()

# Switcher sur l'autre Frame
driver.switch_to.frame("packageFrame")
# Cliquer sur Web driver
driver.find_element(By.XPATH,"html/body/main/div/section/ul/li[14]/a/span").click()

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()


time.sleep(2)
# driver.find_element(By.XPATH, "html/body/div[2]/div/div/ul/li[3]/button").click()
#Fermer le navigateur
driver.quit()