name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown' 

# conversion constants
inches_to_cm = 2.54 # constant for inches_to_cm
pound_to_kg = 0.453592 # constant for pounds_to_kg

# conversion formula 
centimeters = height * inches_to_cm
kilograms = weight * pound_to_kg

print(f"Let's talk about {name}.")
print(f"He's {centimeters} centimeters tall.")
print(f"He's {kilograms} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {centimeters}, and {kilograms} I get {total}.")