#--------------------------------------
#project : Tables calculator 
#description : print tables from 1 to 10
#--------------------------------------
for n in range(1,11):
    print("Table of ",n)
    print("---------------------------")
    for i in range(1,11):
        print(n ," * ", i , "=" ,n*i)