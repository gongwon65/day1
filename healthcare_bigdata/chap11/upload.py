import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
#인증키

cred = credentials.Certificate(r".\heathcare-chap11-firebase-adminsdk-fbsvc-90921b92ce.json")
#타겟 URL
default_app = firebase_admin.initialize_app(cred, {'databaseURL': 
    'https://heathcare-chap11-default-rtdb.asia-southeast1.firebasedatabase.app/'})

dbRef = db.reference()
print(dbRef.get())

