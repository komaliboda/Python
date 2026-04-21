#--------------------------------------
#project : pattern programs 
#description : different numbers pattern
#--------------------------------------

#pattern 1 : number pattern 

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#pattern 2 : reverse number pattern 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

#pattern 3 : continuous number

num = 1
for i in range(1,6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

#pattern 4: reset numbers every row

for i in range(1,6):
    num = 1
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()

#pattern 5 : same number pattern

for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()
        

#pattern 6 : star triangle 

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()


#pattern 7 : reverse star triangle 

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print() 


#pattern 8 :star diamond half pattern 

for i in range(1,6):
    for j in range(i):
        print(" * ",end="  ")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print(" * ",end="  ")
    print() 

#pattern 9 :right aligned triangle 

for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()