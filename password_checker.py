#--------------------------------------
#project : password length checker
#description : checks password length 
#--------------------------------------
 
password = input("Enter your password 🔑  : ")
if len(password) >= 8 :
    print("strong password ")
else : 
    print("password must be atleast 8 characters long ")