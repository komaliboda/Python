#--------------------------------------
#project : votes eligibility 
#Description : checks eligibility of vote based on our age
#--------------------------------------

age = int(input("Enter your age : "))

if age < 0 or age > 100:
    print("Invalid age")
elif age >= 18:
    print("you are Eligible to vote")
else: 
    print("you are not Eligible to vote")
    