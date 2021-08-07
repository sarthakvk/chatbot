from django.contrib.auth import logout
from django.urls import path
from . import views
urlpatterns = [
    path("bot/", views.chat, name="chat"),
    path("login/", views.Flogin, name="login"),
    path("signup/", views.signup, name="signup"),
    path("stat/", views.stat, name="stat"),
    path("logout/", views.Flogout, name="logout"),
]   