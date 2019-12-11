from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='Время', auto_now_add=True)

    @property
    def get_product_cost(self):
        """
        Получение общей стоимости по одному продукту
        :return:
        """
        return self.product.price * self.quantity

    @property
    def get_total_quantity(self):
        """
        Получение общего количества товаров в корзине
        :return:
        """
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def get_total_cost(self):
        """
        Получение общей стоимости корзины
        :return:
        """
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.get_product_cost, _items)))
        return _total_cost

