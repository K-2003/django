from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')

def order(request):
    return render(request, 'main/order.html')

def login_view(request):
    return render(request, 'main/login.html')

def cart(request):
    return render(request, 'main/cart.html')
