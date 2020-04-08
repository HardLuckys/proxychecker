from django.urls import path
from . import views


urlpatterns = [
    path('', views.lol, name='lol')
]
