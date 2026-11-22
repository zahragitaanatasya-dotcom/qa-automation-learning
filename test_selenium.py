
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. Membuka Google Chrome
driver = webdriver.Chrome()

# 2. Membuka website Google
driver.get("https://www.google.com")

# 3. Mencari kolom pencarian Google
search_box = driver.find_element(By.NAME, "q")

# 4. Mengetik kata kunci
search_box.send_keys("Selenium Python tutorial")

# 5. Menekan tombol Enter
search_box.send_keys(Keys.ENTER)

# 6. Menunggu browser tetap terbuka
input("Tekan Enter untuk menutup browser...")

# 7. Menutup browser
driver.quit()
