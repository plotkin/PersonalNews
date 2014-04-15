import webapp2
from usermodel import *
from google.appengine.ext import db

class MainPage(webapp2.RequestHandler):

    def get(self):
        #self.response.write(self.request.uri)

    	user = User(name = "lol", role = "manager", email = "olol@lol.lol")
    	user.put()
    	users = db.GqlQuery("SELECT * FROM User")
    	for user in users:
        	self.response.write(user.name)
                        
    
application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)