from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    image: models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Avatar')

    def __str__(self):
        return self.username