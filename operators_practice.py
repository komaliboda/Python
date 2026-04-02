# ----------------------------------------
# Project: Operators Practice
# Description: Demonstrates arithmetic,
# relational, and logical operators
# ----------------------------------------

# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# --------------------
# Arithmetic Operators
# --------------------
print("\n--- Arithmetic Operations ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Avoid division error
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")

# --------------------
# Relational Operators
# --------------------
print("\n--- Relational Operations ---")
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 == num2:", num1 == num2)

# --------------------
# Logical Operators
# --------------------
print("\n--- Logical Operations ---")
print("num1 > 0 and num2 > 0:", num1 > 0 and num2 > 0)
print("num1 > 0 or num2 > 0:", num1 > 0 or num2 > 0)
print("not(num1 > num2):", not(num1 > num2))