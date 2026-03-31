# ----------------------------------------
# Project: Student Marks Calculator
# Description: Calculates total and average
# ----------------------------------------


name = input("Enter student name: ")

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

# Process
total = m1 + m2 + m3
average = total / 3


print("\n--- Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average) 