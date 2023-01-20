from django.shortcuts import render, HttpResponse, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb://localhost:27017")
db = client['11_01']
uc = db.User
# Create your views here.


def home(req):
    isLogged = dict(req.session).get('docId')
    userData = list(uc.find())
    print('lllllllll', isLogged, 'llllllllll')
    if (isLogged == None):
        return redirect('l')

    return render(req, 'home.html', {'users': userData})


def login(req):
    print('&&&&*****&&&&&&', req.method, "&&&&&&*******", sep="\n")
    if (req.method == "POST"):
        username = req.POST.get("username")
        isUser = uc.find_one({'username': username})
        print('&&&&&&&&&&&&', isUser, '&&&&&&&&&', sep="\n")
        if (isUser):

            print(isUser)
            print(isUser.get('docId'))
            req.session['docId'] = isUser.get('docId')
            return redirect('h')
        else:
            return redirect('s')

    return render(req, 'login.html')


def signup(req):
    if (req.method == "POST"):
        username = req.POST.get('username')
        password = req.POST.get('password')
        username = username.strip()
        print(username, '|')
        print(password, "|")
        userData = {"username": username, "password": password}
        result = uc.insert_one(userData)
        myId = result.inserted_id
        print(myId)
        uc.update_one({'_id': ObjectId(myId)}, {"$set": {"docId": str(myId)}})
        return redirect('s')

    print('==============', '&&&&&&&&&&&&&&&&&')
    return render(req, 'signup.html')

# ObjectId(oid=63c0f9744300c383d01ad102)


def deleteUser(req, docId):
    uc.delete_one({'docId': docId})  # 63c8df21b95d3a5c350da0e1
    return redirect('h')


def logout(req):
    del req.session['docId']
    return redirect('l')
