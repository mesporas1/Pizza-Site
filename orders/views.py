from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Food, Order, OrderDetail, Cart, CartDetail, Topping

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
        "dinners": Food.objects.filter(item__name = 'Dinner Platter'),
        "toppings": Topping.objects.all()
    }
    return render(request, "orders/menu.html", context)

def cart(request):
    try:
        cart = Cart.objects.get(user = request.user)
    except Cart.DoesNotExist:
        return render(request,"orders/cart.html")
    context = {
        "page_text": "This is your shopping cart!",
        "cart_details": CartDetail.objects.filter(cart_id__exact = cart.id)
    }
    return render(request, "orders/cart.html", context)

def orders(request):
    
    context = {
        "page_text": "This is your submitted orders!",
        "orders": Order.objects.filter(user__exact = request.user.id)
    }
    return render(request, "orders/orders.html", context)    

def order_details(request, order_id):
    context = {
        "page_text": "Here is the details to order #" + str(order_id) + "!",
        "order_details": OrderDetail.objects.filter(order_id__exact = order_id)
    }
    return render(request, "orders/order_details.html", context)

def add_item(request, food_id):
    try:
        food = Food.objects.get(pk = request.POST["food"])
        cart = Cart.objects.get(user=request.user)
        print(request.POST["topping"])
        #topping = Topping.objects.get()
    except Food.DoesNotExist:
        return render(request, "orders/errors.html", {"message": "No food item"})
    except Cart.DoesNotExist:
        cart = Cart(user=request.user)
        cart.save()
        cartdetails = CartDetail(cart = cart, food = food, quantity = 1)
        #cartdetails.add(topping)
        cartdetails.save()
        return HttpResponseRedirect(reverse("menu"))
    cartdetails = CartDetail(cart = cart, food = food, quantity = 1)
    cartdetails.save()
    return HttpResponseRedirect(reverse("menu"))

def remove_item(request, cart_detail_id):
    cartdetails = CartDetail.objects.get(pk = request.POST["food"])
    cartdetails.delete()
    return HttpResponseRedirect(reverse("cart"))

def contact(request):
    context = {
        "page_text": "This is the contact page!"
    }
    return render(request, "orders/index.html", context)