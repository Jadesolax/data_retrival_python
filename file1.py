# The script reads a CSV file, processes its content, and searches for a user based on their email address.

# It demonstrates:

# File handling (opening, reading, and closing files).

# Looping through data.

# String manipulation (splitting and extracting fields).

# Conditional logic (checking for matches).

# User input and interaction.

## bring the csv file into the current file

# open the file for reading only
fobject = open("users.csv", "r")

# read the file and storing the content in the "result" variable

## readlines() will read the entire file line by line into a list [ ]
result = fobject.readlines()

# print(result)

## loop through the list
result_length = len(result)

# print(result_length)

counter = 0

entered_email_address = input("Enter your email address: ")

while counter < result_length:
  
    if counter != 0:
        data = result[counter]
        box = data.split(",")
        # print(box)
        ## print all the email addresses for each user
        email_address = box[3]
        firstname = box[1]
        id = box[0]
        status = box[4]

        if entered_email_address == email_address:
            print("Welcome " + firstname)
            break

    
    
        
    counter = counter + 1


fobject.close()