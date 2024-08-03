from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download_mp3/', views.download_mp3, name='download_mp3'),
]
