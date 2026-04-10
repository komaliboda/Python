#--------------------------------------
#project : counts digits
#description : returns count value 
#--------------------------------------

num = input("Enter number : ")
count = 0
for i in num:
    if i.isdigit():
        count += 1
print("Number of difits : " ,count)