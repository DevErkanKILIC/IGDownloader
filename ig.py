from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import os
import time

driverPath = 'yourChormeDriverPath'

usernameValue = 'yourUsername'
passwordValue = 'yourPassword'

targetURL = 'targetUrl' 

className = 'setClassName'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(driverPath)

driver.get('https://www.instagram.com')

time.sleep(5)

username_input = driver.find_element('name', 'username')
password_input = driver.find_element('name', 'password')
username_input.send_keys(usernameValue)
password_input.send_keys(passwordValue)
password_input.send_keys(Keys.ENTER)

time.sleep(5)

driver.get(targetURL)

time.sleep(2)

for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


driver.find_element(By.TAG_NAME,'body').send_keys(Keys.F12)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.F5)


posts = driver.find_elements(By.CLASS_NAME,className)


def download_file(url):
    response = requests.get(url)
    save_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(save_dir, exist_ok=True)

    file_number = len(os.listdir(save_dir)) + 1  
    filename = f"{file_number}.jpg"

    save_path = os.path.join(save_dir, filename)

    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"{filename} indirildi ve {save_path} dosyasına kaydedildi.")

network_requests = driver.execute_script("return window.performance.getEntries()")

counter = 1

for request in network_requests:
         if 'name' in request and 'fist' in request['name']:
          print(f"Link: {request['name']}")
          download_file(request['name'])

driver.quit()