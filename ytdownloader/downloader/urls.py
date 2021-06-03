from django.urls import path, include
from . import views

app_name = 'downloader'

urlpatterns = [
    path('', views.home, name='home'),
    path('files/<str:specific_ytlink>/', views.file, name='file')
]
