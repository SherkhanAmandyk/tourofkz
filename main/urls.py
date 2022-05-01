from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('place/<slug:page>', views.page),
    path('place/', views.place),
    path('registration/', views.register),
    path('new/', views.new),
    path('new/<int:pk>/update', views.updateNews.as_view()),
    path('new/<int:pk>/delete', views.deleteNews.as_view()),
    path('about/', views.about),
    path('send/',views.send_message),
]