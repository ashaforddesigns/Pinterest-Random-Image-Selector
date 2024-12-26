import requests
from bs4 import BeautifulSoup
r = requests.get("https://mx.pinterest.com/asha707af/cute-hair/")
print(r.status_code)