#Logical operator
#And
a=2
b=9
c=3
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")
#Or
if a>b or b>c:
    print("either A or B are greater")
#not
print(not(a))