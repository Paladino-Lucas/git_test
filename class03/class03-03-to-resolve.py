#The secret password game
# ask user for password and print acess grants otherwise ask them to choose again.
# the user can try 3 times
# nest loop
# Give the user 3 prompts to enter the correct password


correct_password = "data"

for attempt in range(3):

    password = input("Please enter the secret password:")
    if password == correct_password:
        print("Access granted")
    elif password== "Data22" or password=="data22"or password=="DATA22":
        print("Check your spellings")
    else : print("Access denied")

# show how many attempts are left
    if attempt<= 3:
        print(f"You have {2-attempt} attempts left")
    elif attempt>= 2: 
        print(f"You have {1-attempt} attempts left")
    elif attempt==1:
        print(f"You have {0-attempt} attempts left")
    else:
        print(f"you {0-attempt}block the system")    
    
