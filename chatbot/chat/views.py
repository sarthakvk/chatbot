from django.db.models.query import RawQuerySet
from django.views import generic
import random
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from .models import User, ButtonCalls
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt


# chat view
def chat(request):
    context = {"user": request.user}
    return render(request, "chat/index.html", context)


# utility to choose random jokes
def respond_to_websockets(message):
    jokes = {
        "stupid": [
            """Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
            """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association.""",
        ],
        "fat": [
            """Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
            """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """,
        ],
        "dumb": [
            """Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
            """Yo' Mama is so dumb, she locked her keys inside her motorcycle.""",
        ],
    }

    result_message = {"type": "text", "source": "BOT"}
    if "fat" == message:
        result_message["text"] = random.choice(jokes["fat"])

    elif "stupid" == message:
        result_message["text"] = random.choice(jokes["stupid"])

    elif "dumb" == message:
        result_message["text"] = random.choice(jokes["dumb"])

    else:
        result_message[
            "text"
        ] = "Hello! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."

    return result_message


# signup
@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, "chat/signup.html", {"sucess": None})
    else:
        print(request.POST)
        email = request.POST.get("email")
        name = request.POST.get("name")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(email=email, password=password, name=name)
            user.set_password(password)
            user.save()
        except Exception as e:
            return redirect(signup)
        login(request,user)
        return redirect(chat)


# login front
@csrf_exempt
def Flogin(request):
    if request.method == "GET":
        return render(request, "chat/login.html", {"sucess": None})
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(chat)
        else:
            return redirect(Flogin)


# logout front
def Flogout(request):
    logout(request)
    return redirect(chat)


# show stats of count per user
def stat(request):
    context = {
        "bs": ButtonCalls.objects.all()
    }
    return render(request, "chat/stat.html", context)