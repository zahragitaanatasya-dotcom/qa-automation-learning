from selenium import webdriver
from selenium.webdriver.common.by import by 

driver = webdriver.chrome()
driver.get ("https://www.google.com/")
search_box = driver.find_element(By.Name, "q")
search_box.send_keys("https://stagewallet.mobipaid.com/login")
search_box.send_keys(Keys.ENTER)
driver.quit()
