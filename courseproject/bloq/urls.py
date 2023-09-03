from django.urls import path
from .views import BloqsListView


urlpatterns = [
    path('bloqs/', BloqsListView.as_view(), name='bloq')
]