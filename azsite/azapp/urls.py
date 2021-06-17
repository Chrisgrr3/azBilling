from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('mca', views.mca),
    path('mosp', views.mosp),
    path('ea', views.ea),
    path('mpa', views.mpa)
]
