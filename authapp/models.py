from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст пользователя', blank=True, null=True)
