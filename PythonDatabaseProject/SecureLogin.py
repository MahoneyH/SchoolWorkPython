#Author Hunter Mahoney/Erika Tix
#Created 4/10/19  Updated 4/10/19
#Creating a file for a secure login

#-------------------------------
#   Variable references
#   id: This is randomly created through mongoDb
#
#-------------------------------

import bcrypt

def hashUserLogin (password, salt):
    hashed = bcrypt.hashpw(str(password).encode("utf-8"), bcrypt.gensalt())

    #print(collection)
    print(hashed)
    return hashed

def printHash():

    print(hashUserLogin())









