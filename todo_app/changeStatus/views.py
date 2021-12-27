from django.shortcuts import render
import pyrebase

# Create your views here.
config={
    "apiKey": "AIzaSyCRayTHspURWXG_CekN6x0JsGkRljqjshc",
    "authDomain": "ftodolists-b38b4.firebaseapp.com",
    "databaseURL": "https://todolists-b38b4-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "todolists-b38b4",
    "storageBucket": "ftodolists-b38b4.appspot.com",
    "messagingSenderId": "621099248368",
    "appId": "1:621099248368:web:81aedc860b6b43d2733035",
    "measurementId": "G-6PXX15C7GQ"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

def index(request):
    name = database.child('data').child('name').get().val()
    db = database.child('data').child('Database').get().val()
    fw = database.child('data').child('Framework').get().val()

    context = {
        'name':name,
        'Database':db,
        'Framework':fw,
    }

    return render(request,'index.html',context)