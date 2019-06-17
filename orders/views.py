from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "page_text": "This is Pinnochio's Pizza home!"
    }
    return render(request, "orders/index.html", context)

def menu(request):
    context = {
        "page_text": "This is Pinnochio's Pizza menu!"
    }
    return render(request, "orders/index.html", context)

def cart(request):
    context = {
        "page_text": "This is your shopping cart!"
    }
    return render(request, "orders/index.html", context)

def orders(request):
    context = {
        "page_text": "This is your submitted orders!"
    }
    return render(request, "orders/index.html", context)    

def contact(request):
    context = {
        "page_text": "This is the contact page!"
    }
    return render(request, "orders/index.html", context)