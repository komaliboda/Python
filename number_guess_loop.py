#--------------------------------------
#project : Guessing Number Game 
#--------------------------------------

secret_number = 8
print("Enter a number between 0 to 100")
while True:
    guess = int(input("enter  your guess number : "))
    if guess < 0 or guess > 100:
        print("invalid input (0-100) only ")
    elif secret_number == guess:
        print("correct guess 💯 ")
        break 
    elif guess > secret_number:
        print("Too high ")
    else:
        print("Too low ")
