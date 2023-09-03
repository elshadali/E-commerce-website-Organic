from django.urls import path
from .views import contact_list


urlpatterns = [
    path('contact/', contact_list, name='contact')
]