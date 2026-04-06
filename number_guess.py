#--------------------------------------
#project : Number guess game
#description : Checks user guess against secret number
#--------------------------------------

secret_number=8
user_guess=int(input("Enter your guess  : "))
if user_guess == secret_number: 
    print(" correct guess✅")
elif user_guess > secret_number: 
    print("Too high ")
else: 
    print("Too low")
