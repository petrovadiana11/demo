from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50, verbose_name="имя")
    password = models.CharField(max_length=50, verbose_name="пароль")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Пользователи"