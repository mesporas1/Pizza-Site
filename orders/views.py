from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .models import Food, Order, OrderDetail

# Create your views here.
def index(request):
    context = {
        "page_text": "This is Pinnochio's Pizza home!"
    }
    return render(request, "orders/index.html", context)

def menu(request):
    context = {
        "page_text": "This is Pinnochio's Pizza menu!",
        "pizzas": Food.objects.filter(item__name = 'Pizza'),
        "subs": Food.objects.filter(item__name = 'Sub'),
        "pastas": Food.objects.filter(item__name = 'Pasta'),
        "salads": Food.objects.filter(item__name = 'Salad'),
        "dinners": Food.objects.filter(item__name = 'Dinner Platter')
    }
    return render(request, "orders/menu.html", context)

def cart(request):
    context = {
        "page_text": "This is your shopping cart!"
    }
    return render(request, "orders/index.html", context)

def orders(request):
    
    context = {
        "page_text": "This is your submitted orders!",
        "orders": Order.objects.filter(user__exact = request.user.id)
    }
    return render(request, "orders/orders.html", context)    

def order_details(request, order_id):
    context = {
        "page_text": "Here is your order details!",
        "order_details": OrderDetail.objects.get(order_id = order_id)
    }
    return render(request, "orders/order_details.html", context)

def contact(request):
    context = {
        "page_text": "This is the contact page!"
    }
    return render(request, "orders/index.html", context)