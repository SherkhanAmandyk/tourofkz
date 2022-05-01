from django.shortcuts import render
from .models import News
from main.forms import NewsForms
from django.views.generic import UpdateView

def news(request):
    news = News.objects.all()
    return render(request, 'main/blog.html', {'news' : news})


def pageNews(request, page):
    page = int(page)
    news = News.objects.filter(id = page)
    name = []
    photo = []
    byName = []
    dateTime = []
    description = []
    byPhoto = []
    for el in news:
        name.append(el.name)
        photo.append(str(el.photo_url))
        byName.append(str(el.byName))
        dateTime.append(str(el.dateTime)[:10])
        description.append(str(el.description))
        byPhoto.append(str(el.photo_url_by))

    return render(request, 'main/single-news.html', {'name' : name,
                                                    'photo' : photo,
                                                    'byName' : byName,
                                                    'dateTime' : dateTime,
                                                    'description' : description,
                                                    'byPhoto' : byPhoto})


