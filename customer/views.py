from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from customer.forms import LoginForm, RegisterForm
from customer.models import Customer


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            return redirect('content:home')
    form = LoginForm
    return render(request, 'customer/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('content:home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            new_user = User.objects.create_user(username=username, password=password)
            Customer.objects.create(user=new_user, first_name=first_name, last_name=last_name)

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('content:home')

    form = RegisterForm
    return render(request, 'customer/register.html', {'form': form})
