from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import RegisterForm
# Create your views here.


def register(response):

    if(response.method == "POST"):
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisterForm()

    return render(response, "registration.html", {"form": form})


def logout_request(response):
    logout(response)
    return redirect("/")
