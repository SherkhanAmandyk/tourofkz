from django.shortcuts import render
from .models import Traditional

def traditional(request):
    trad = Traditional.objects.all()
    return render(request, 'main/traditional.html', {'traditional' : trad})


def pageTrad(request, page):
    page = int(page)
    traditional = Traditional.objects.filter(id = page)
    name = []
    photo = []
    byName = []
    dateTime = []
    description = []
    byPhoto = []
    for el in traditional:
        name.append(el.name)
        photo.append(str(el.photo_url))
        byName.append(str(el.byName))
        dateTime.append(str(el.dateTime)[:10])
        description.append(str(el.description))
        byPhoto.append(str(el.photo_url_by))

    return render(request, 'main/single-traditional.html', {'name' : name,
                                                    'photo' : photo,
                                                    'byName' : byName,
                                                    'dateTime' : dateTime,
                                                    'description' : description,
                                                    'byPhoto' : byPhoto})

