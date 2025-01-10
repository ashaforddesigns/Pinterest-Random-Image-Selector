from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
# url = input("Insert link to board here")
# # url ="https://mx.pinterest.com/asha707af/cute-hair/" 
# r = requests.get(url)
# # print(r.status_code)

# # Parse the HTML
# soup = BeautifulSoup(r.text, features="html.parser") 
# images = soup.find_all("img")

# # print(soup.title) // gets board title

# def shuffle(url):
# # looks at photos given a board then selects one
    
#     return img["src"]


# for img in images:
#         print(img["src"])

driver = webdriver.Firefox()
url = input("Insert link to board here")
driver.get(url)
images = driver.find_elements(By.TAG_NAME, "img")

# Scroll to load more images
for _ in range(10): 
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
    time.sleep(3)  

for img in images:
    print(img.get_attribute("src"))


# url ="https://mx.pinterest.com/asha707af/cute-hair/" 


driver.close()