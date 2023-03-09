from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index.html"),
    path("portugal", views.portugal, name='portugal.html'),
    path("espanha", views.espanha, name='espanha.html')
]

