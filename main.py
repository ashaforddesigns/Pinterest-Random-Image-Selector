import requests
from bs4 import BeautifulSoup
url = input("Insert link to board here")
# url ="https://mx.pinterest.com/asha707af/cute-hair/" 
r = requests.get(url)
# print(r.status_code)

# Parse the HTML
soup = BeautifulSoup(r.text, features="html.parser") 
images = soup.find_all("img")

# print(soup.title) // gets board title

def shuffle(url):
# looks at photos given a board then selects one
    
    return img["src"]


for img in images:
        print(img["src"])
