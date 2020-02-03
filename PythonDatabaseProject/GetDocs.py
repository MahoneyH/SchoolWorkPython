# Author: Hunter M/Erika T.
# Date Updated: 4/19/19
# Description: This docuuments contains all methods that will retrieve Mongo Docs.
# Ex: get User posts, get user profile, get .
# They will be called from here.
# Grabs all information from inside these methods to create the documents


import pprint


def showUser(client, currentUser):

    db = client.ComputerForum
    collection = db.Users
    document = collection.find_one({'User Name': currentUser}, {'Salt': 0, '_id': 0, 'hashedPw': 0, 'isSignedIn': 0})
    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(document)

def showPosts(client, currentUser):
    db = client.ComputerForum
    collection = db.Posts

    for doc in collection.find({'Author': currentUser}, {'_id': 0}):
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(doc)
        print("")

def showOtherUserPosts(client):
    db = client.ComputerForum
    collection = db.Posts
    searchedUser = input("Enter the username you would like to search for: ")

    for doc in collection.find({'Author': searchedUser}, {'_id': 0}):
        pp = pprint.PrettyPrinter(depth=6)
        pp.pprint(doc)


