from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_pensieri, name='lista_pensieri'),
]