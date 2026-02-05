from lvl1_exercises import first_name, last_name, age, is_married, country

# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(is_married))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name. 
print('First name length:', first_name, 'Last name length:', last_name)

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
print(num_one, ",", num_two)

# Subtract num_two from num_one and assign the value to a variable diff
subtraction = num_one - num_two
print(subtraction)

# Multiply num_two and num_one and assign the value to a variable product.
multiply = num_one * num_two
print(multiply)

# Divide num_one by num_two and assign the value to a variable division
divide = num_one / num_two
print(divide)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
modulus = num_two % num_one
print(modulus)

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle.
radius = 30
pi = 3.14
area_of_circle = pi * (radius ** 2)
print(area_of_circle)

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
diameter = radius * 2
circum_of_circle = pi * diameter
print(circum_of_circle)

# Take radius as user input and calculate the area.
user_radius = int(input("Enter the radius: "))
user_diameter = user_radius * 2
area_of_circle = pi * (user_radius ** 2)
circum_of_circle = pi * user_diameter
print(area_of_circle)
print(circum_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country of residence: ")
age = int(input("Enter your age: "))

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
#Completed via python shell. --> Entering 'python' in terminal.