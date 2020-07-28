from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from django.contrib.auth import lo
# Create your views here.


def home(response):

    return render(response, "home.html", {})


def login_view(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(response, user)
            return redirect('/profile/%s' % username)

    form = AuthenticationForm()
    return render(response, "login.html", {"form": form})
