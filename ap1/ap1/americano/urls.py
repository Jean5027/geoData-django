from django.urls import path
from . import views

urlpatterns = [
    path("", views.index2, name="index2.html"),
    path("estados", views.estados, name='estadosus.html'),
    path("canada", views.canada, name='canada.html')
]

