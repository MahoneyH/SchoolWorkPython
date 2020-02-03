# This file creates 1000 threads with a text file

import datetime
import random


def createRandomThread(client):


    x = 0
    db = client.ComputerForum
    collection = db.Threads


    userArr = ["AliceWonderland", "BobBurger", "CatarinaWine", "DonaldDog", "EdgyEggs", "FinleyNinja",
               "GregoryGengar", "HollyJolly", "IcyIguana", "JumpingJelly"]

    file = open("RandomWords.txt", "r")
    count = 1
    for x in file:
        title = x.rstrip('\n')
        #file.readline()
        creator = random.choice(userArr)
        threadPost = []
        tags = []
        newThread = [

            {"Title": title,
             "Creator": creator,
             "Thread Posts": threadPost,
             "Time Stamp": datetime.datetime.utcnow(),
             "Tags": tags}
        ]

        collection.insert_many(newThread)
        count =+ 1

        if count == 10:
            break


