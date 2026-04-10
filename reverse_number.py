#--------------------------------------
#project : reverse a number
#description : This program reverses a given integer using a while loop by extracting digits one by one.
#--------------------------------------

num = int(input("Enter number : "))
temp = num
rev=0
while temp > 0:
    s=temp%10
    rev=rev*10+s
    temp//=10
print("The reverse number is : ",rev)
    
        
