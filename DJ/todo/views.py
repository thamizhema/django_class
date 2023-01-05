from django.shortcuts import render, HttpResponse

# Create your views here.


products = ["milk", 'sugar', 'ghee', 'butter']
userInfo = {'name': "python", 'email': "python@gmail.com"}


def home(req):
    data = {
        'username': "JavaScript",
        'age': 20,
        "products": products,
        'userInfo': userInfo
    }

    return render(req, 'home.html')


def login(req):
    return render(req, 'login.html')


def signup(req):
    return render(req, 'signup.html')
