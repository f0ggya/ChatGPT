from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('send_message', views.send_message),
    path('login', views._login)
]