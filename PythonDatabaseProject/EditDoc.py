# This class will allow the user to:
# 1. Edit their signature
# 2. Delete a post



import pprint


def editSignature(client, currentUser):
    # This method allows a user to edit their signature
    db = client.ComputerForum
    collection = db.Users
    #documents = collection.find({"User Name": currentUser})

    newSignature = input('What would you like to change your signature to?\n')

    collection.find_one_and_update({"User Name": currentUser}, {"$set": {"Signature": newSignature}})


def editBio(client, currentUser):
    # This method allows a user to edit their personal bio
    db = client.ComputerForum
    collection = db.Users
    #documents = collection.find({"User Name": currentUser})

    newBio = input("Enter your new personal bio.\n")
    collection.find_one_and_update({"User Name": currentUser}, {"$set": {"Bio": newBio}})


def deletePost(client, currentUser):
    # This method allows users to delete one of their old posts.
    db = client.ComputerForum
    collection = db.Posts
    # documents = collection.find({"User Name": currentUser})
    deleteTitle = input("Enter the title of the post you would like to delete: \n")


    if collection.find_one({"Title": deleteTitle}):
        print("Your post was found", deleteTitle)
        collection.remove({"Title": deleteTitle})

