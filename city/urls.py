from django.urls import path
from . import views

urlpatterns = [
    path('', views.city),
    path('<slug:page>', views.pageCity),
]