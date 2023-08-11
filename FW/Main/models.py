from django.db import models

class pages(models.Model):
    title = models.CharField('Название', max_length=250)
    text = models.TextField('Заметка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'