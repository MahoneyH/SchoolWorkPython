#Author: Hunter M/Erika T.
#Date Updated: 4/18/19
#Description: This docuuments contains all methods that creates new Mongo Docs.
#Ex: new User, new Post, New thread, new Comments.
#They will be called from here.
#Grabs all information from inside these methods to create the documents


#.distinct to grab a feild from a document.
import datetime
import bcrypt
import SecureLogin
from pymongo import MongoClient



def createUser(client):
    db = client.ComputerForum
    collection = db.Users

    firstName = input("Enter First Name: ")
    lastName = input("Enter Last Name: ")
    userName = input("Enter Username: ")
    password = input("Enter password: ")
    salt = bcrypt.gensalt()
    encryptedPass = SecureLogin.hashUserLogin(password, salt)
    myPost = []
    upvotedPost =[]
    signature = firstName + " " + lastName
    mod = False
    signIn = False

    newUser =[
        {"First Name": firstName,
         "Last Name": lastName,
         "User Name": userName,
         "Salt": salt,
         "hashedPw": encryptedPass,
         "Bio": "",
         "User Posts": myPost,
         "Upvoted Posts": upvotedPost,
         "Signature": signature,
         "Moderator": mod,
         "isSignedIn": signIn}
    ]

    collection.insert_many(newUser)

#Need to add the post to the post document, but also add it into
#the thread documents array.
#pass the selected thread document to the method
#add a field to get the thread you are in.
def createPost(client, currentUser, currentDoc):

    db = client.ComputerForum
    collection = db.Users
    postCollection = db.Posts
    documents =collection.find({"User Name": currentUser})

    collectionThread = db.Threads
    distinctTitle = currentDoc
    #.distinct("Title")

    title = input("Enter Title for the post: ")
    author = currentUser
    content = input("Enter posts content: ")
    signature = documents.distinct("Signature")
    print(signature)
    upVotes = 0
    comments =[]
    tags = createTags()


    newPost = [
        {"Title": title,
         "Author": author,
         "Content": content,
         "Signature": signature[0],
         "Time Stamp" : datetime.datetime.utcnow(),
         "Upvotes": upVotes,
         "Comments": comments,
         "Tags": tags
         }
    ]

    print(newPost)
    postCollection.insert_many(newPost)


    #will need the title of the thread, and maybe the author

    collectionThread.update({'Title': distinctTitle}, {'$push': {'Thread Posts': {"Title": title,
         "Author": author,
         "Content": content,
         "Signature": signature[0],
         "Time Stamp" : datetime.datetime.utcnow(),
         "Upvotes": upVotes,
         "Comments": comments,
         "Tags": tags
         } } }
                            )
    #return newPost

def createThread(client, currentUser):
    flag = True
    db = client.ComputerForum
    collection = db.Threads

    while flag:
        title = input("Enter Thread Title: ")
        #verify that the name doesnt already exisit.
        if collection.find({'Title': title}).count() > 0:
            print("Name already Taken")
        else:
            flag = False

    creator = currentUser
    threadPost = []
    tags = createTags()

    newThread = [

        {"Title": title,
         "Creator": creator,
         "Thread Posts": threadPost,
         "Time Stamp": datetime.datetime.utcnow(),
         "Tags": tags}
    ]


    collection.insert_many(newThread)

def createComment(client, currentUser, currentPost):
    db = client.ComputerForum
    collection = db.Posts
    distinctTitle = currentPost.distinct("Title")
    comment = input("Enter your Comment: ")

    newComment = [
        {"User" : currentUser,
         "Comment": comment}
    ]

    #should add a comment to a post.
    collection.update({'Title': distinctTitle}, {'$push': {'Thread Posts': newComment}})

def createTags():
    flag = True
    tags = []

    while flag:
        choice = input("Add a tag: (1 = yes, 2 = No")

        if int(choice) ==1:
            tag = input("Enter a tag: ")
            tags.append(tag)
        elif int(choice) ==2:
            flag = False
        else:
            print("Invalid choice")

    return tags
