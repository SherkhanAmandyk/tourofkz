from django.shortcuts import render
from .models import Cities
from main.models import Place

def city(request):
    city = Cities.objects.all()
    place = Place.objects.all()[:3]
    return render(request, 'main/city.html', {'city' : city,
                                              'place' : place})


def pageCity(request, page):
    page = int(page)
    city = Cities.objects.filter(id = page)
    name = []
    photo = []
    byName = []
    money = []
    dateTime = []
    description = []
    byPhoto = []
    for el in city:
        name.append(el.name)
        photo.append(str(el.photo_url))
        byName.append(str(el.byName))
        money.append(str(el.money))
        dateTime.append(str(el.dateTime)[:10])
        description.append(str(el.description))
        byPhoto.append(str(el.photo_url_by))

    return render(request, 'main/single-city.html', {'name' : name,
                                                    'photo' : photo,
                                                    'byName' : byName,
                                                    'money' : money,
                                                    'dateTime' : dateTime,
                                                    'description' : description,
                                                    'byPhoto' : byPhoto})

