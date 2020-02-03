

import DocCreations
import GetDocs
import MenuCreations

def createThread(client, currentUser):
    flag = True

    while flag:
        try:
            userInput = input("What would you like to do?\n"
                              "1. Look at threads\n"
                              "2. View your old posts\n"
                              "3. View posts from other users\n"
                              "4. Edit your profile\n"
                              "5. Create Thread\n")

            if int(userInput) == 1:
                print("Go to Threads.")
                MenuCreations.lookAtThreads(client, currentUser)
                flag = False
            elif int(userInput) == 2:
                print("Here are your old posts.")
            elif int(userInput) == 3:
                print("Here are the posts from other users.")
                # This will get posts from a user they search for
            elif int(userInput) == 4:
                print("You can now edit your profile.")
                GetDocs.showUser(client, currentUser)
            elif int(userInput)==5:
                DocCreations.createThread(client, currentUser)
            else:
                print("Invalid input")
        except ValueError:
            print("Invalid input, please try again")
            createThread(client, currentUser)