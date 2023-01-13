from django.shortcuts import render, HttpResponse, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
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
        result = uc.insert_one(userData)
        iID = result.inserted_id
        # filterDoc = ObjectId(iID)
        data = uc.update_one({"_id": ObjectId(iID)}, {
                             "$set": {"docId": str(iID)}})
        print(data)
        return redirect('h')
    print('==============', '&&&&&&&&&&&&&&&&&')
    return render(req, 'signup.html')

# ObjectId(oid=63c0f9744300c383d01ad102)


def deleteUser(req, docId):
    uc.delete_one({'docId': docId})
    return redirect('h')
