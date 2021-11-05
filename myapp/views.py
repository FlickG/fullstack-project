from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Tangina MO!")


def my_name(request):
    context = {"name": "FlickM top 31 Mir4"}
    return render(request, "myapps/myapps.html", context)


# Create your views here.
