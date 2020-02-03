# This class will call the menus that display to the user

# The first menu will be for User logging in / or signing up
# The second menu will be for posts - this will either allow the user to :
# 1. Create a post
# 2. View old posts - if this is selected then
# 2a. Edit an old post
# 2b. Delete an old post
# 3. View posts from other users
# 4. Edit profile - if this is selected then
# 4a. Edit signature
# 4b. Edit bio
# 4c. Edit old posts
# 4d. Delete an old post

######
### Things to do
### In method of viewThread, need to figure out how to
### Go to see threads

#ask for user input to build a new user
#Also call for users to create a password

import DocCreations
import LoginVerify
import AdminLogin
import GetDocs
from pymongo import MongoClient

import pprint
import AdminMenuCreations
#----------------------------------------------------------------------

import RandomThreads

#def main():
   # client = AdminLogin.loginDatabase()
   # loginSignup(client)

# This method asks the user if they want to login or sign up
def loginSignup(client):

    flag = True
    try:
        while flag:
            userInput = input("Would you like to: \n"
                              "1. Login \n"
                              "2. Sign up for an account \n")

            if int(userInput) == 1:
                currentUser = LoginVerify.userLogin(client)
                print("You are now logged in!")
                modStatus = checkIfMod(client, currentUser)
                if modStatus == False:
                    postMenu(client, currentUser)
                else:
                    AdminMenuCreations.createThread(client, currentUser)

                flag = False
            elif int(userInput) == 2:
                DocCreations.createUser(client)
                print("Welcome to Fascio!")
                flag = False
            elif int(userInput):
                print("Invalid entry, try again!")
    except ValueError:
        print("Invalid input")
        loginSignup(client)

#----------------------------------------------------------------------


#----------------------------------------------------------------------
def postMenu(client, currentUser):
    flag = True
    modStatus = checkIfMod(client, currentUser)
    if modStatus == False:
        postMenu(client, currentUser)
    else:

        while flag:
            try:
                userInput = input("What would you like to do?\n"
                                  "1. Look at threads\n"
                                  "2. View your old posts\n"
                                  "3. View posts from other users\n"
                                  "4. Edit your profile\n")

                if int(userInput) == 1:
                    print("Go to Threads.")
                    lookAtThreads(client, currentUser)
                    flag = False
                elif int(userInput) == 2:
                    print("Here are your old posts.")
                    GetDocs.showPosts(client, currentUser)
                elif int(userInput) == 3:
                    print("Here are the posts from other users.")
                    # This will get posts from a user they search for
                    GetDocs.showOtherUserPosts(client)
                elif int(userInput) == 4:
                    print("You can now edit your profile.")
                    GetDocs.showUser()
                else:
                    print("Invalid input")
            except ValueError:
                print("Invalid input")
                postMenu(client, currentUser)
#----------------------------------------------------------------------


#----------------------------------------------------------------------
def lookAtThreads(client, currentUser):
    db = client.ComputerForum
    collection = db.Threads

    flag = True

    while flag:
        try:
            userInput = input("What would you like to do?\n"
                              "1. Search Thread by Name\n"
                              "2. View All Threads\n"
                              "3. Go To Thread\n"
                              "4. Go Back\n")

            if int(userInput) == 1:
                title = input("Enter Thread Title")
                if collection.find({"Title": title}).count() >0:
                    foundDoc = collection.find({"Title": title})
                    for doc in foundDoc:
                        print(doc)

                else:
                    print("Not found")
            elif int(userInput) == 2:
                #call new menu for thread selection
                viewAllThreads(client, currentUser)
                flag = False
            elif int(userInput) ==3:
                docName = input("Enter Thread Name")
                # call method to look at document of thread
                lookAtSelectedThread(client, currentUser, docName)
                flag = False
            elif int(userInput) == 4:
                #collection.remove({}).skip(1000)
                postMenu(client, currentUser)
                flag = False
                # This will get posts from a user they search for
        except ValueError:
            print("Invalid input")
            lookAtThreads(client,currentUser)
#----------------------------------------------------------------------

#----------------------------------------------------------------------
#this method will display all threads that you can access
#it will display 20 at a time
#you can go forward or go back
#use startsearch to skip a number of items
#use end search to limit the amout of search to be displayed
def viewAllThreads(client, currentUser):
    flag = True
    db = client.ComputerForum
    collection = db.Threads
    threadArr =[]
    startSearch = 0;
    endSearch = 20;


    #for doc in collection.distinct("Title"):
    for doc in collection.find({},{"_id": 0, "Thread Posts": 0,"Time Stamp": 0, "Tags":0}).skip(startSearch).limit(endSearch):
        #threadArr.append(doc)
        print(doc)
        print("")

    #need to add a loop that allows us to keep searching by 10s
    while flag:
        try:
            userInput = input("What would you like to do?\n"
                              "1. Go To Thread\n"
                              "2. Search next 20\n"
                              "3. Search previous 20\n"
                              "4. Go Back\n")

            if int(userInput) == 1:
                docName = input("Enter Thread Name")
                #call method to look at document of thread
                lookAtSelectedThread(client, currentUser, docName)
                flag = False
            elif int(userInput) == 2:
                print("Here are your old posts.")
                startSearch = startSearch +20
                endSearch = endSearch +20
                for doc in collection.find({},{"_id": 0, "Thread Posts": 0,"Time Stamp": 0, "Tags":0}).skip(startSearch).limit(endSearch):
                    #threadArr.append(doc)
                    print(doc)
                    print("")

            elif int(userInput) == 3:
                print("Here are the posts from other users.")
                if startSearch ==0:
                    print()
                else:
                    startSearch -20
                    endSearch -20
                # This will get posts from a user they search for
                for doc in collection.find({}, {"_id": 0, "Thread Posts": 0,"Time Stamp": 0, "Tags":0}).skip(startSearch).limit(endSearch):
                    threadArr.append(doc)
                    print(doc)
                    print("")
            elif int(userInput) == 4:
                print("You can now edit your profile.")
                lookAtThreads(client, currentUser)
            else:
                print("Invalid input")

        except ValueError:
            print("Invalid input")
            viewAllThreads(client, currentUser)
#----------------------------------------------------------------------

#----------------------------------------------------------------------
#this method is used to display the current thread you are looing at
#will need a menu for
#   View posts
#   Add post
#   go back to threads
def lookAtSelectedThread(client, currentUser, docName):
    flag = True
    db = client.ComputerForum
    collection = db.Threads
    document = collection.find({"Title": docName})
    currentDoc = docName
    pp = pprint.PrettyPrinter(depth=6)

    while flag:
        try:
            for doc in document:
                pp.pprint(doc)
            userInput = input("What would you like to do?\n"
                              "1. Create Post\n"
                              "2. View Posts\n"
                              "3. Go back to threads\n")
            if int(userInput) == 1:
                DocCreations.createPost(client, currentUser, currentDoc)
            elif int(userInput) == 2:
                print("Look at Posts")

                newArray = []
                newArray = currentDoc.ThreadPosts
                print(newArray)


            elif int(userInput) == 3:
                viewAllThreads(client, currentUser)
        except ValueError:
            print("Invalid Input")
            lookAtSelectedThread(client, currentUser, docName)

#----------------------------------------------------------------------

def checkIfMod(client, currentUser):
    db = client.ComputerForum
    collection = db.Users
    document = collection.find({'User Name': currentUser})

    GetDocs.showUser(client, currentUser)

    flag = document.distinct('Moderator')
    print(flag[0])
    return flag[0]
#if __name__ == '__main__':
   # main()