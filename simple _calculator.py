#--------------------------------------
#project : Simple calculator 
#discription : Performs basic operation
#---------------------------------------
num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
addition = num1+num2
substraction = num1-num2
multiplication = num1*num2
exponent = num1**num2
if num2!=0:
    division = num1/num2
    floor_division=num1//num2
else:
    division = "division by zero is error "
    floor_division = "division by zero error "

print( "addition:",addition)
print( "substraction:",substraction)
print( "multiplication:",multiplication)
print( "power:", exponent)
print( "Division:",division)
print( "Floor division: ", floor_division)


