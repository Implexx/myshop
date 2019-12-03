from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя сотрудника')
    position = models.CharField(max_length=32, verbose_name='Должность')
    picture = models.ImageField(upload_to='team', verbose_name='URL на картинку', blank=True, null=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', max_length=500, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=64)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    model = models.CharField(verbose_name='Модель', max_length=32)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    description = models.TextField(verbose_name='Описание', max_length=500)
    image = models.ImageField(verbose_name='Фото', upload_to='products', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)


class Review(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя клиента')
    text = models.TextField(verbose_name='Текст отзыва', blank=True)
    rating = models.PositiveIntegerField(verbose_name='Рейтинг товара', default=0)
    date = models.DateField(verbose_name='Дата отзыва', auto_now_add=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.date)


class BrandLogo(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название бренда')
    image = models.ImageField(upload_to='brands')

    def __str__(self):
        return self.name
