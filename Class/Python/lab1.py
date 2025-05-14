from operator import index

# Lab 1: Python Beginner
# Lab Requirements:

# Python 3.x installed (e.g., via Anaconda or directly)

# Code editor or IDE (e.g., PyCharm, VS Code, Jupyter Notebook, or IDLE)

################################################################################################
# Step 1: Hello World & Comments
# Objective: Understand how to print and write comments.

# This is a single-line comment
print("Hello, world!")  # Print a message

# Task: Write your name and age using print().


################################################################################################
# Step 2: Variables and Data Types
# Objective: Learn to create and use variables.

name = "Pablo"
age = 43
height = 180
is_professor = True

print(name, age, height, is_professor)

# Task: Create variables for your favorite food, number of pets you have, and whether you like this course.
fav_food = 'Rice'
no_pet = 0
like_course = True
print(fav_food, no_pet, like_course)
################################################################################################
# Step 3: Taking User Input
# Objective: Learn how to accept user input and store it.

name = input("What is your name? ")
print("Nice to meet you, " + name + "!")

# Task: Ask the user for their age and print it back with a message.

Age = input("How old are you? ")
print('I am ' + Age)
################################################################################################
# Step 4: Arithmetic Operations
# Objective: Learn to use mathematical operations.

a = 10
b = 3

print("Addition:", a + b)
print("Division:", a / b)
print("Composed operations", a * b + a^2)


# Task: Write a code that takes two numbers and prints their sum, product, and difference.
a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
print("The sum of the numbers is :", a + b)
print("Product is :", a * b)
print('Difference between the number is:', a - b)

################################################################################################
# Step 5: Conditional Statements
# Objective: Use if, elif, and else to control program flow.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")

# Task: Write a code that checks if a number is even or odd.
Spec_no = int(input("Enter your special number: "))
if Spec_no % 2 == 0:
    print("Special number is even.")
elif Spec_no % 2 == 1:
    print("Special number is odd.")
else:
    print("Special number is neither even nor old")

##############################################################################################
# Step 6: Loops – for and while
# Objective: Learn loop structures.

# For loop
for i in range(5):
    print("Looping:", i)

# While loop
count = 0
while count < 10:
    print("Counting:", count)
    count += 1

# Task: Write a program that prints all numbers from 1 to 10 using both for and while.
## For loop
for i in range(1,11):
    print("Looping:", i)
## While loop
count = 1
while count <= 10:
    print("Counting:", count)
    count += 1
##############################################################################################
# Step 7: Functions
# Objective: Learn how to define and call functions.

def greetings(x):
    print("Hello, " + x + "!")

greetings("Pablo")

# Task: Create a function that takes two numbers and returns their average.
def aver(n1,n2):
    average = (n1+n2)/2
    return average

aver(7,29)

##############################################################################################
# Step 8: Lists
# Objective: Understand lists and indexing.

fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Access first item
fruits.append("orange")  # Add item
print(fruits)

# Task: Create a list of 5 favorite movies and print each one using a loop.
F_movie = ['Winx_club', 'Iron_man', 'Avengers', 'Lion_king', 'Merlin']
i = 6
for item in F_movie:
    i -= 1
    print('Favorite Movie', f'{i}:', item)

##############################################################################################
# Step 9: Dictionaries
# Objective: Work with key-value pairs.

person = {"name": "Pablo", "age": 43}
print(person["name"])
print(person["age"])

person["age"] = 36  # Update value