from multiprocessing.spawn import import_main_path
from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('bag/', views.bag, name='bag'),
]