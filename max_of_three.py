#--------------------------------------
#project : Largest of three numbers
#--------------------------------------

num1 = int(imput("Enter  first number : "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number : "))
if num1>=num2 and num1>=num3:
    print("first number is largest")
    
elif num2>=num1 and num2>=num3:
    print("second number is largest")
    
else:
    print("Third number is largest")