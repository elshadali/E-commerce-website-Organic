from django.urls import path
from .views import BloqsListView, bloq_detail


urlpatterns = [
    path('bloqs/', BloqsListView.as_view(), name='bloq'),
    # path('bloqs/<slug:slug>', BloqDetailView.as_view(), name='bloq_detail'),
    path('bloqs/<slug:bloq_slug>', bloq_detail, name='bloq_detail')
]