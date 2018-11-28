# see https://dataset.readthedocs.io/en/latest/ for documentation on dataset
import dataset
from Users import *


# based on queries sent from frontend, backend will respond

# call this to initialize backend
# can put this in every function, or frontend can do it and pass to all the below functions
# for now, I have all functions call it
def init_backend():
    db = dataset.connect("sqlite:///mydatabase.db")
    table = db["users"]
    return table


# creates a new user with passed info. First checks if one exists with passed information
def create_user(name=None, username=None, email=None, password=None, age=None, address=None):
    if check_user_exists(username, password) is True:
        return False

    new_user = User(name, username, email, password, age, address)
    table = init_backend()
    table.insert(new_user.return_info())
    return True


# call this when a user attempts to sign in. It will update the database IF the users' info checks out
def user_sign_in(username=None, password=None):
    if check_user_exists(username, password) is False:
        return False

    table = init_backend()
    # updates this person's logins
    table.update({"Username": username, "Logins": table.find_one(Username=username)["Logins"] + 1}, ["Username"])
    return True


# called inside every function. Checks if user is in database given username and password
def check_user_exists(username=None, password=None):
    table = init_backend()

    if table.find_one(Username=username, Password=password) is not None:
        return True

    else:
        return False


# call this whenever a user queries something. The query will be added to the person's search history
# for some reason, dataset doesn't like entries that are lists, so all search history code is commented out for now
# def add_search_history(username=None, password=None, query=None):
#     if check_user_exists(username, password) is False:
#         return False
#     table = init_backend()
#     table.update({"Username": username, "Search History": table.find_one(Username=username)["Search History"].append(query)}, ["Username"])
#     return True


# call this to see the whole database
def show_database():
    table = init_backend()
    for row in table:
        print(row)


# # sample demo code
# print(create_user(name="Jatin", username="jmather125", email="jatinm2@illinois.edu", password="fakepassword123", age=18, address="Champaign, IL"))
# print()
# print(show_database())
# print()
# print(check_user_exists(username="jmather125", password="fakepassword123"))
# print()
# print(user_sign_in(username="jmather125", password="fakepassword123"))
# print()
# print(show_database())
# print()
# # print(add_search_history(username="jmather125", password="fakepassword123", query="Thomas Siebel Center for Comp. Sci."))
# # print(show_database())
