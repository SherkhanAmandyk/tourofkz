from django.shortcuts import render, redirect
from .models import Place, Register, Ip
from city.models import Cities
from .forms import NewsForms, RegisterForm
from news.models import News
from django.views.generic import UpdateView, DeleteView
from django.core.mail import send_mail
from django.core.mail import EmailMessage


def send_message(request):
    send_mail("Web programming","My content",
    "200103062@stu.sdu.edu.kz",
    ["200103062@stu.sdu.edu.kz","sherhanamandik03@gmail.com"],
    fail_silently=False,html_message="<b>Bold text</b><i>Italic text</i>")
    return render(request, 'main/successefull.html')    


def send_message(request):
    email = EmailMessage(
        'Test case','HELOOOO','200103062@stu.sdu.edu.kz',
        ['200103062@stu.sdu.edu.kz','sherhanamandik03@gmail.com'],
        headers={'Message-ID':'foo'},)
    email.attach_file('C:/Users/Infolife/Pictures/suret.png')
    email.send(fail_silently=False)
    return render(request,'main/successefull.html')
total_count = 0

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip
total_count = 0
def index(request):
    global total_count
    total_count = total_count + 1

    place = Place.objects.order_by('-dateTime')[:3]
    city = Cities.objects.order_by('-dateTime')[:4]
    return render(request, 'main/index.html', {'place' : place,
                                               'city' : city,
                                               'count' : total_count})

def page(request, page):
    page = int(page)
    place = Place.objects.filter(id = page)
    name = []
    photo = []
    byName = []
    money = []
    dateTime = []
    description = []
    byPhoto = []
    for el in place:
        name.append(el.name)
        photo.append(str(el.photo_url))
        byName.append(str(el.byName))
        money.append(str(el.money))
        dateTime.append(str(el.dateTime)[:10])
        description.append(str(el.description))
        byPhoto.append(str(el.photo_url_by))

    return render(request, 'main/single-place.html', {'name' : name,
                                               'photo' : photo,
                                               'byName' : byName,
                                               'money' : money,
                                               'dateTime' : dateTime,
                                               'description' : description,
                                                      'byPhoto' : byPhoto})


def place(request):
    place = Place.objects.all()
    return render(request, 'main/place.html', {'place' : place,})

def new(request):
    error = ''
    if request.method == 'POST':
        form = NewsForms(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Заполните форму корректно'

    form = NewsForms()
    news = News.objects.all()
    return render(request, 'main/new.html', {'form' : form,
                                             'error' : error,
                                             'news' : news})

class updateNews(UpdateView):
    model = News
    template_name = 'main/edit.html'
    form_class = NewsForms


class deleteNews(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'main/delete.html'


def about(request):
    return render(request, 'main/about.html')

def register(request):
    error = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            data = Register.objects.order_by('-id')[:1]
            data1 = []
            for el in data:
                data1.append(el.name)
            return render(request, 'main/register_done.html', {'data' : data1})
        else:
            error = 'Заполните форму корректно'

    form = RegisterForm()
    return render(request, 'main/register.html', {'form': form,
                                             'error': error,})





