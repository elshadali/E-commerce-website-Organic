from django.urls import path
from .views import search, index


urlpatterns = [
    path('', index, name='index'),
    path('search', search, name='search'),
]