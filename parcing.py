import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from product.models import Product  # Замените "myapp" на имя вашего Django приложения


class Command(BaseCommand):
    help = 'Parse products from koreamania.kg and save to the database'

    def handle(self, *args, **kwargs):
        url = 'https://koreamania.kg/category/ramen/'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products = soup.find_all('div', class_='product-item')

            for product in products:
                name = product.find('h4').text.strip()
                price = product.find('span', class_='price-new').text.strip()

                # Если есть дополнительные данные, которые нужно спарсить, добавьте их здесь
                # Например, описание продукта, изображение и т.д.

                # Сохранение продукта в базу данных Django
                Product.objects.create(name=name, price=price)

            self.stdout.write(self.style.SUCCESS('Successfully parsed and saved products.'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch the page. Status code: {}'.format(response.status_code)))
