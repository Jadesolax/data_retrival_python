# ask the user to enter their name
username = input("Hello, please enter your name: ")

## greet the user using their name
print("Welcome " + username + "!")

topic = input("Enter a new journal topic: ")
notes = input("Enter journal content: ")

## check if a file exists already (journaling.txt file)
import os

if os.path.isfile("journaling.txt"):
    print("The journaling file exists already ...")
    print("I will not be recreating it ...")
    fobject = open("journaling.txt", "a")
    heading = topic + " - By " + username + "\n"
    fobject.write(heading)
    fobject.write("------------------- \n")
    fobject.write(notes + "\n")
    fobject.write("\n")
    fobject.write("--- \n")
    fobject.close()
else: 
    print("The journaling file does not exist ...")
    print("I will be creating it..")
    
    fobject = open("journaling.txt", "w")

    heading = topic + " - By " + username + "\n"
    fobject.write(heading)
    fobject.write("------------------- \n")
    fobject.write(notes + "\n")
    fobject.write("\n")
    fobject.write("--- \n")
    fobject.close()

