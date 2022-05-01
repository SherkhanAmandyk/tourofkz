from django.db import models

class Ip(models.Model): # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100)

def __str__(self):
    return self.ip

class Place(models.Model):
    name = models.CharField('Название места', max_length=70)
    byName = models.CharField('Автор', max_length=40)
    byPhoto = models.ImageField('by Фото', upload_to='static/main/author/', null=True, blank=True)
    money = models.CharField('Цена', max_length=10)
    first = models.CharField('Особенность 1', max_length=40)
    second = models.CharField('Особенность 2', max_length=40)
    dateTime = models.DateTimeField('Дата')
    description = models.TextField('Описание')
    photo = models.ImageField('Фото', upload_to='static/main/', null=True, blank=True)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)

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



class Register(models.Model):
    name = models.CharField('Имя', max_length=70)
    surname = models.CharField('Фамилия', max_length=40)
    age = models.CharField('Возраст', max_length=3)
    country = models.CharField('Страна', max_length=40)
    city = models.CharField('Город', max_length=40)
    dateReg = models.DateTimeField('Дата рождения')
    email = models.CharField('E-mail', max_length=70)

    def __str__(self):
        return self.name



