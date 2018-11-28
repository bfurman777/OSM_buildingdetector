import sys
sys.path.append('../')
import backend

# need the following syntax to call classes from another file
# x = backend.Users.User("Jatin", "jmather", "jatinm2@illinois.edu", "fakepassword", 18, "Champaign, IL")
# print(x)

# need the following syntax to call functions from another file
# backend.init_backend() <- from backend.py
# since there is no function overlap there should be no problem

# to call functions
# backend.create_user(name="Jatin", username="jmather125", email="jatinm2@illinois.edu", password="fakepassword123", age=18, address="Champaign, IL")
# to see the changes
# backend.show_database()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') #base page that loads up on start/accessing the website
def login():  #this method is called when the page starts up
   return render_template('login.html') #displays the relevant page


@app.route('/NewAccount.html') #activates when create a new account is clicked
def newAccount():
   return render_template('/NewAccount.html') #links to the create a new account page


@app.route('/test',methods = ['POST', 'GET'])   #this page is a test page to show if the information is saved
def result():
   if request.method == 'POST': # if the user hits the submit button. post is called
      result = request.form
      
      return render_template("test.html",result = result) #this links to the result page and dispalys the proper information


if __name__ == '__main__': #causes the program to boot
   app.run(debug = True)

