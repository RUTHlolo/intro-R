## MEV6706 first assignment
# Task 1: Print function and Commenting

## Print your full name
full_name = "Ifeoluwa Ruth Olonijolu"
print(full_name)

## The code below will print the list of favorite places I have visited
fav_palce = ['Abuja', 'Kigali', 'Montréal']
print(fav_palce)

## Task 2: Variables and Data type
fav_color = 'Red' # string data type
N_pets = 2 ## integer
ice_cream = True # Boolean
print('My favorite color is', f'{fav_color},',
      'I have' ,f'{N_pets}' , ' pets',
      f'{ice_cream},',' I like Ice cream')

## Task 3:  Write a code asking for your favorite movie and year of release.
f_movie = str(input('Enter your favourite movie: '))
year = int(input('Enter the year it was released: '))
print('My favourite movie is', f_movie, ', and it was released in', year)

# Task 4: Arithmetic in Python
x = 4
y = 7
print("Addition:", x + y)
print("Difference:", x - y)
print("Product: ", x * y)
print("Division:", y / x)

## Task 5: Conditional Statements
age = int(input('Enter your age: '))
if age < 13:
    print('You are a Child')
elif age >= 18:
    print('You are an Adult')
else:
    print('You are a Teenager')

## Task 6: Loops
## For loop
for i, n in enumerate(range(1,11), start=1):
    print('Number',f'{i}:', n)

## While Loop
count = 6
while count > 0:
    count -= 1
    print('Counting', count)

## Task 7: Functions
def num(k,j):
    return (k * j)/2

num(99, 25.5)

## Task 8: Lists
f_food = ["Rice","Potatoes","Pasta","Cake","Bread"]
for item in f_food:
    print("I like to eat ",item)

## Task 9: Dictionaries
P_details = {"name" : "Abraham", "Age": 45, "Profession": "Developer"}
print("My name is", P_details['name'],
      "I am a ", P_details['Profession'],
      "and I am ", P_details['Age'], "years old"
      )

## Task 10: A function that performs basic math operator
def operator(x,y,z, xyz = Noneone):
    result = xzy
    return result

x = int(input("Your first number: "))
y = int(input("Your second number: "))
z = input("Your a math operator: ")