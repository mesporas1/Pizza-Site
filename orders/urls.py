from django.urls import path

from . import views

urlpatterns = [
    path("menu", views.menu, name="menu"),
    path("cart", views.cart, name="cart"),
    path("orders", views.orders, name="orders"),
    path("orders/<int:order_id>", views.order_details, name="order_details"),
    path("contact", views.contact, name="contact")
]
