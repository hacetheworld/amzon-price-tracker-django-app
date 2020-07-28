from django.urls import path

from .views import register, logout_request

urlpatterns = [
    path('logout/', logout_request, name='logout'),
    path('register/', register, name='register'),
]
