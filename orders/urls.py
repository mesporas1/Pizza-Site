from django.urls import path

from . import views

urlpatterns = [
    path("menu", views.menu, name="menu"),
    path("menu/<int:food_id>", views.add_item, name="add_item"),
    path("cart", views.cart, name="cart"),
    path("cart/<int:cart_detail_id>", views.remove_item, name="remove_item"),
    path("orders", views.orders, name="orders"),
    path("orders/<int:order_id>", views.order_details, name="order_details"),
    path("contact", views.contact, name="contact")

]
