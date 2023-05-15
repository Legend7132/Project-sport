
import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:8000/'
search_text = 'Hello, world!'

# Получаем HTML-код страницы
response = requests.get(url)
html = response.text

# Разбираем полученный код на отдельные элементы
soup = BeautifulSoup(html, 'html.parser')

# Ищем текст на странице
found_text = soup.find(text=search_text)

# Выводим результат
if found_text:
    print(f'Текст "{search_text}" найден на странице')
else:
    print(f'Текст "{search_text}" не найден на странице')
