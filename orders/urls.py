from django.urls import path

from . import views

urlpatterns = [
    path("menu", views.menu, name="menu"),
    path("cart", views.cart, name="cart"),
    path("orders", views.orders, name="orders"),
    path("contact", views.contact, name="contact")
]
