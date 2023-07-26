from product.models import CartItem
from django.db import models
from registration.models import CustomUser


class History(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    history = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    def __str__(self):
        return f'история заказов - {self.history}'

    class Meta:
        verbose_name = ('История')
        verbose_name_plural = ('Истории')

