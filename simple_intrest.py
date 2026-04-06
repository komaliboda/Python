#--------------------------------------
#project : simple interest calculator 
#description : calculates simple intrest 
#--------------------------------------

principal = float(input("Enter your principal amount : "))
rate = float(input("Enter rate of intrest intrest : "))
time = float(input("Enter time : "))
unit = input(" is time in days or years : ")
if unit == "days":
    time = time/365

simple_intrest = (principal*rate*time)/100
amount = principal+simple_intrest
print("simple intrest" , simple_intrest)
print("Total amount", amount)


