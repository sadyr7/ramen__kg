from registration.models import CustomUser
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Катерогии'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    # description = models.CharField(max_length=250)
    likes = modles.DecimalField(max_digits=10)

    def __str__(self):
        return f' ваш товар {self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_pel(self, total_price):
        total_price = self.quantity * self.product.price
        return total_price

    def __str__(self):
        return f"{self.user} - {self.product.title} - количество: {self.quantity} - цена {self.quantity * self.total_price}"

    class Meta:
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')
        unique_together = ('user', 'product')

    def save(self, *args, **kwargs):
        existing_cart_item = CartItem.objects.filter(user=self.user, product=self.product).first()

        if existing_cart_item:
            existing_cart_item.quantity += self.quantity
            existing_cart_item.save()
        else:
            super().save(*args, **kwargs)

