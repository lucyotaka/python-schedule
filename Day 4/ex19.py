def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints the number of cheeses based on the cheese_count argument
    print(f"You have {cheese_count} cheeses!")
    # Prints the number of boxes of crackers based on the boxes_of_crackers argument
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Prints a statement indicating it's enough for a party
    print("Man that's enough for a party!")
    # Prints a statement suggesting to get a blanket
    print("Get a blanket.\n")

# Calls the function with numbers directly as arguments
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Uses variables from the script as arguments for the function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Performs math operations inside the function call
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Combines variables and math operations as arguments for the function
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



def greet_person(name, age):
    if age < 18:
        print(f"Hi {name}! You're just a young one!")
    elif age >= 18 and age < 30:
        print(f"Hello {name}! Enjoy your youth!")
    else:
        print(f"Greetings {name}! You're wise and experienced!")

# Running the function in 10 different ways
# 1. Providing arguments directly
greet_person("Alice", 25)

# 2. Using variables as arguments
person_name = "Bob"
person_age = 15
greet_person(person_name, person_age)

# 3. Mixing direct values and variables
greet_person("Charlie", person_age)

# 4. Using expressions in arguments
greet_person("David", 35 - 5)

# 5. Prompting user for input
name_input = input("Enter your name: ")
age_input = int(input("Enter your age: "))
greet_person(name_input, age_input)

# 6. Combining input and direct values
greet_person(name_input, 28)

# 7. Assigning values to variables and calling the function
person_name = "Emily"
person_age = 20
greet_person(person_name, person_age)

# 8. Using calculations in arguments
greet_person("Frank", person_age + 10)

# 9. Passing a negative age value
greet_person("George", -5)

# 10. Passing zero as the age value
greet_person("Hannah", 0)
