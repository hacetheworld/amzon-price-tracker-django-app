from django.shortcuts import render, redirect
# from django.contrib.auth import r

# Create your views here.


def content(response, username):
    # print(type(str(response.user)))
    if(len(str(response.user)) > 0 and str(response.user) != 'AnonymousUser'):
        return render(response, "content.html", {})
    else:
        return redirect("/")
