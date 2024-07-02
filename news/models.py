from django.db import models
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=60)
    username = models.CharField('Автор', max_length=60)
    short_description = models.CharField('Краткое описание новости', max_length=250)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'