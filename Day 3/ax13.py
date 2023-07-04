from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

def process_user_data(name, age):
    #process user data
    print("Name:", name)
    print("Age:", age)

# collect user data
user_data = input("Enter your name and age (seperated by a comma): ")

#unpack user data
name, age = user_data.split(",")

#call the function with unpacked variables
process_user_data(name.strip(), age.strip())

def process_user_data(name, age, email, address):
    #process user data
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Address:", address)

# collect user data
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
address = input("Enter your address: ")

# call the function with arguments
process_user_data(name, age, email, address)


import sys

# get input from command-line argument
arg_value = sys.argv[1] if len(sys.argv)>1 else ""
print("command-line argument value:", arg_value)

# get additional input from the user
user_input = input("Enter something: ")
print("User input:", user_input)