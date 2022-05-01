from django.db import models

class Cities(models.Model):
    name = models.CharField('Название места', max_length=70)
    byName = models.CharField('Автор', max_length=40)
    byPhoto = models.ImageField('by Фото', upload_to='static/main/author/', null=True, blank=True)
    money = models.CharField('Цена', max_length=10)
    dateTime = models.DateTimeField('Дата')
    description = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='static/main/', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    @property
    def photo_url_by(self):
        if self.byPhoto and hasattr(self.byPhoto, 'url'):
            return self.byPhoto.url
