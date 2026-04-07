#--------------------------------------
#project : temperature checker
#description : check temperature conditions 
#--------------------------------------

temperature = float(input("Enter temperature 🌡️ :  "))
if temperature < 0:
    print(" freezing 🥶 ")
elif temperature > 40:
    print("Too hot 🥵 ")
elif temperature > 30:
    print("hot 🔥 ")
elif temperature >= 20:
    print("warm 😳")
else:
    print("cool 🧊")