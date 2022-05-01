from django.urls import path
from . import views

urlpatterns = [
    path('', views.traditional),
    path('<slug:page>', views.pageTrad),
]