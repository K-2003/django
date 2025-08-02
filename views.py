from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, OrderForm, ProfileForm
from .models import Order
import json

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('order')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('order')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('orders')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})

@login_required
def orders(request):
    all_orders = Order.objects.filter(user=request.user)
    for o in all_orders:
        try:
            data = json.loads(o.items)
        except:
            data = {}
        o.item_list = [(k.replace('_',' ').title(), int(v[0])) 
                       for k, v in data.items() if v and v[0].isdigit()]
    return render(request, 'orders.html', {'orders': all_orders})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_pw = form.cleaned_data.get('password')
            if new_pw:
                user.set_password(new_pw)
            user.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})
