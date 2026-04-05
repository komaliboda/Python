#--------------------------------------
#project :✅ marks grade system 
#Description : assign grade based on marks
#--------------------------------------

marks = int(input("Enter your marks : "))
if marks < 0 or marks > 100:
    print("invalid marks")
elif marks >= 90:
    print("grade : A")
elif marks >= 75:
    print("grade : B")
elif marks >= 50:
    print("grade : C")
else:
    print("Fail")