from django.urls import path
from . import views

urlpatterns = [
    path(
        "orders/create/",
        views.OrderCreateAPIView.as_view(),
        name="order-create",
    ),
    path(
        "orders/delete/<int:id>",
        views.OrderDeleteAPIView.as_view(),
        name="order-delete",
    ),
    path(
        "main-orders/create/",
        views.MainOrderCreateAPIView.as_view(),
        name="main-order-create",
    ),
    path(
        "main-orders/is-done/<int:id>",
        views.OrderIsDoneAPIView.as_view(),
        name="main-order-is-done",
    ),
    path(
        "add-to-wish-list/",
        views.AddToWishListAPIView.as_view(),
        name="add-to-wish-list",
    ),
    path(
        "remove-from-wish-list/",
        views.RemoveFromWishListAPIView.as_view(),
        name="remove-from-wish-list",
    ),
]