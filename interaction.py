from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\Utilizador\Desktop\chrome_driver\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()


# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("THE")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("GOAT")
email = driver.find_element(By.NAME, "email")
email.send_keys("well_well_well@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

