import datetime
from google.appengine.ext import db
from google.appengine.api import users

class User(db.Model):
  name = db.StringProperty(required=True)
  role = db.StringProperty(required=True,
                           choices=set(["executive", "manager", "producer"]))
  email = db.StringProperty()