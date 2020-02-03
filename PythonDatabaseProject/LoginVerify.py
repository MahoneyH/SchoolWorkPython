#This will create a system to create a new user, and to login in as a user
#It will call the SecureLogin methods to create a safe salted hash password.

#Ask if you wish to login in, or create a new user
#call contructor for need user
#add the user to the method
#else ask for username and password

#ask for user input to build a new user
#Also call for users to create a password


import AdminLogin
import bcrypt


#client = AdminLogin.loginDatabase()

def userLogin(client):
    userName = input("Enter your user name: ")
    password = input("Enter your password: ")


    db = client.ComputerForum
    collection = db.Users
    document = collection.find_one({'User Name': userName})

    salt = collection.find({'Salt': 1})
    hashedPass = collection.find({'hashedPw': 1})

    # checkPass = SecureLogin.hashUserLogin(password, hashedPass)

    if bcrypt.hashpw(password.encode("utf-8"), document['hashedPw']) == document['hashedPw']:
        print("Successful!")

    else:
        print("NOOOOOO FAIL")

    # This returns the username for the person currently logged in
    return userName
