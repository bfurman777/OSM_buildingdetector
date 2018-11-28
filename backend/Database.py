# see https://dataset.readthedocs.io/en/latest/ for documentation on dataset
import dataset
from Users import *


# is able to retain data of previous entries even after code ends, because the file is in the directory
# db = dataset.connect("sqlite:///mydatabase.db")
#
# # this syntax can be used to create a table and access a table
# table = db["users"]

# this syntax adds info to the database
# dict example: {"column1: info1, column2: info2, ...}
# table.insert(DICT FORM OF INFORMATION)
# table.columns() # will give the columns of the database

# these commands help find information in the database
# table.find(COLUMN HEADER = QUERY) # can return multiple users
# table.find_one(NAME/ID/IDENTIFIER = QUERY) # to find one person

# Find by comparison operator
# elderly_users = table.find(age={'>=': 70})
# possible_customers = table.find(age={'between': [21, 80]})
#
# x = User("Jatin", "jmather25", "jatinm2@illinois.edu", "fakepassword", 18, "Champaign, IL")
# table.insert(x.return_info())
# print()
# print(table.find_one(Username="hoogawaga"))
# print()
# table.update({"Username": "jmather25", "Logins": table.find_one(Username= "jmather25")["Logins"] + 1}, ["Username"])
# for row in table:
#     print(row)
