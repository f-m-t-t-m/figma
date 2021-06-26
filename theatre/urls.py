from django.urls import path
from . import views


urlpatterns = [
    path('', views.theatre, name='theatre'),
]