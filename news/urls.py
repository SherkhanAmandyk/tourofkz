from django.urls import path
from . import views

urlpatterns = [
    path('', views.news),
    path('<slug:page>', views.pageNews),
]