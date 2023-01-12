from django.shortcuts import render, HttpResponse
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['11_01']
uc = db.User
# Create your views here.


def home(req):
    userData = list(uc.find())
    print('lllllllllllllllllll')
    print(userData)
    return render(req, 'home.html', {'users': userData})


def login(req):
    return render(req, 'login.html')


def signup(req):
    print(req.method)
    if (req.method == "POST"):
        username = req.POST.get('username')
        password = req.POST.get('password')
        username = username.strip()
        print(username, '|')
        print(password, "|")
        userData = {"username": username, "password": password}
        uc.insert_one(userData)
    print('==============', '&&&&&&&&&&&&&&&&&')
    return render(req, 'signup.html')


def deleteUser(req, docId):
    uc.delete_one({'username': docId})
    return HttpResponse(f'<h1> {docId} deleted Successfuly</h1>')
