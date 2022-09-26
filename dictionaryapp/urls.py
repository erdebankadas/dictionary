from django.urls import path
from . import views

urlpatterns = [
    path('dictionary', views.index, name='index'),
    path('search', views.search, name='search'),
    
]
