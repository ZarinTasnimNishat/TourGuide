from django.shortcuts import render
#from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, "TourGuideSystem/index.html")


def signup(request):
    return render(request, "TourGuideSystem/signup.html")


def signin(request):
    return render(request, "TourGuideSystem/signin.html")


def signout(request):
    pass
