from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

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
        "cart_details": CartDetail.objects.filter(cart_id__exact = cart.id),
        "cart": cart
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

@require_http_methods(["POST"])
def add_item(request, food_id):
    try:
        food = Food.objects.get(pk = request.POST["food"])
        cart = Cart.objects.get(user=request.user)
    except Food.DoesNotExist:
        return render(request, "orders/errors.html", {"message": "No food item"})
    except Cart.DoesNotExist:
        cart = Cart(user=request.user)
        cart.total += food.price
        cart.save()
        cartdetails = CartDetail(cart = cart, food = food, quantity = 1)
        cartdetails.save()
        toppings = request.POST.getlist("toppings")
        for topping in toppings:
            cartdetails.topping.add(topping)
        cartdetails.save()
        return HttpResponseRedirect(reverse("menu"))
    cart.total += food.price
    cart.save()
    cartdetails = CartDetail(cart = cart, food = food, quantity = 1)
    cartdetails.save()
    toppings = request.POST.getlist("toppings")
    for topping in toppings:
            cartdetails.topping.add(topping)
    cartdetails.save()
    return HttpResponseRedirect(reverse("menu"))

@require_http_methods(["POST"])
def remove_item(request, cart_detail_id):
    cartdetails = CartDetail.objects.get(pk = request.POST["food"])
    cart = Cart.objects.get(user=request.user)
    cart.total -= cartdetails.food.price
    cart.save()
    cartdetails.delete()
    return HttpResponseRedirect(reverse("cart"))

@require_http_methods(["POST"])
def submit_order(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return HttpResponseRedirect(reverse("cart"))
    order = Order(user=request.user)
    order.total = cart.total
    order.save()
    cartdetails = CartDetail.objects.filter(cart_id__exact = cart.id)
    for cartdetail in cartdetails:
        orderdetail = OrderDetail(order = order, food = cartdetail.food, quantity = cartdetail.quantity)
        orderdetail.save()
        toppings = cartdetail.topping.all()
        print(toppings)
        for topping in toppings:
            print(topping.id)
            orderdetail.topping.add(topping.id)
        orderdetail.save()
    context = {
        "page_text": "Here is the details to order #" + str(order.id) + "!",
        "order_details": OrderDetail.objects.filter(order_id__exact = order.id)
    }
    cart.total = 0
    cart.save()
    cartdetails.delete()
    return render(request, "orders/order_details.html", context)



def contact(request):
    context = {
        "page_text": "This is the contact page!"
    }
    return render(request, "orders/index.html", context)