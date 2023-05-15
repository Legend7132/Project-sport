
import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'
search_text = 'Hello, world!'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

found_text = soup.find(text=search_text)

if found_text:
    print(f'Текст "{search_text}" найден на странице')
else:
    print(f'Текст "{search_text}" не найден на странице')
