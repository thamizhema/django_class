from django.shortcuts import render, HttpResponse

# Create your views here.


def login(req):
    return HttpResponse("<h1>Login page</h1>")
