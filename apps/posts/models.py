from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to=True,
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Посты'
        
