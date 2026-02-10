# Declare your age as integer variable
age = 25

# Declare your height as a float variable
my_height = 172.0 # in cm.

# Declare a variable that store a complex number
complex_num = 1 + 1j
print(complex_num)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print("The area of the triangle is", area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perm_triangle = a + b + c
print("The perimeter of the triangle is", perm_triangle)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
l = int(input("Enter the length: "))
w = int(input("Enter the width: "))
area_rectangle = l * w
perm_rectangle = 2 * (l + w)
print("The area of the rectangle is", area_rectangle)
print("The perimeter of the rectangle is", perm_rectangle)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Enter the radius: "))
pi = 3.14
area_circle = pi * (r ** 2)
circumference_circle = 2 * pi * r
print("The area of the circle is", area_circle)
print("The circumference of the circle is", circumference_circle)

# Calculate the slope, x-intercept and y-intercept of y = 2x - 2.
# Given linear equation: y = 2x - 2
m = 2
b = -2

print("Slope:", m)

y_intercept = m * 0 + b
print("y-intercept:", y_intercept)

x_intercept = (0 - b) / m
print("x-intercept:", x_intercept)

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1, x2, y2 = 2, 2, 6, 10
m2 = (y2 - y1) / (x2 - x1)
print(m2)

# Compare the slopes in tasks 8 and 9.
print("Slope from task 8 was", m, "and slope from task 9 was", m2)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def quadratic_formula(x):
    y = (x ** 2) + (6 * x) + 9 
    return y

print(quadratic_formula(2))

# Coefficients of x² + 6x + 9 = 0
a = 1
b = 6
c = 9

# Since it's a perfect square, we can factor directly
x = -b / (2 * a)

print("x =", x)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') > len('dragon'))

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon.')

# There is no 'on' in both dragon and python
#any() function Python any() function returns True IF ANY of the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True else it returns False.
print(any('on' not in word for word in ['dragon', 'python'])) 

# Find the length of the text python and convert the value to float and convert it to string 
l = len('python')
fl = float(l)
string = str(fl)
print(type(string))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
def is_even(num):
    if num % 2 == 0:
        return True
    
    return False

print(is_even(8))
print(is_even(3))

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
fl_to_int = int(2.7)
print(floor_division, fl_to_int)
print(floor_division == fl_to_int)

# Check if type of '10' is equal to type of 10. 
str_ten = str(10)
int_ten = 10
print(type(str_ten) == int_ten)

# Check if int('9.8') is equal to 10
str_to_float = float('9.8')
fl_to_int = int(str_to_float)
print(int_ten == fl_to_int) # False - int() rounds down to nearest integer.

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hrs = int(input("Enter your hours: "))
rate = int(input("Enter rate per hour: "))
weekly_earnings = hrs * rate
print("Your weekly earnings are:", weekly_earnings)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.
yrs = int(input("Enter how many years you have lived: "))
secs_total = 31536000 * yrs
print("You have lived for", secs_total, "seconds.")

# Write a Python script that displays the following table. 
""" 1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125 """
nums = list(range(1, 6))

for n in nums:
    table = []  # Reset the list for each row to allow the clean print for each new row.
    table.append(n)
    for i in range(4):
        result = n ** i
        table.append(result)
    print(*table)  # The * unpacks the list for cleaner printing.
