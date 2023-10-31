from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    id_telegram = models.PositiveBigIntegerField(
        verbose_name="ID телеграм"
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        null=True
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.last_name}"

    class Meta:
        verbose_name = "Пользователь телеграмма"
        verbose_name_plural = "Пользователи телеграмма"

        

class Contacts(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        verbose_name="Почта",
        null=True,blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона"
    )
    message = models.TextField(
        verbose_name="Введите ваше сообщение"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"