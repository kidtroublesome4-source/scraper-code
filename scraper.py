import csv
import requests
from bs4 import BeautifulSoup

def get_data():
    url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())

    
    books = []
    for article in soup.find_all('article', class_='product_pod'):
        title = article.find('h3').find('a')['title']
        price = article.find('p', class_='price_color').text.strip()
        books.append({'title': title, 'price': price})

    
    categories = []
    side = soup.find('div', class_='side_categories')
    for a in side.find_all('a'):
        cat = a.text.strip()
        if cat and cat != 'Books':
            categories.append(cat)

    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Price', 'Category'])
        for i, book in enumerate(books):
            writer.writerow([
                book['title'],
                book['price'],
                categories[i] if i < len(categories) else 'N/A',
            ])

    print('Data has been updated in output.csv')

get_data()
