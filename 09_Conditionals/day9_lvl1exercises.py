# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
""" Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive. """
user_age = int(input("Enter your age: "))
legal_age = 18
age_diff = legal_age - user_age

if user_age >= legal_age:
    print("You are old enough to learn to drive.")
elif age_diff == 1:
    print(f"You need {age_diff} more year to learn to drive.")
else:
    print(f"You need {age_diff} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:
""" Enter your age: 30
You are 5 years older than me. """
user_age = int(input("Enter your age: "))
my_age = 25
age_diff = abs(my_age - user_age)

if user_age > my_age:
    if age_diff == 1:
        print(f"You are {age_diff} year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
elif user_age < my_age:
    if age_diff == 1:
        print(f"You are {age_diff} year younger than me.")
    else:
        print(f"You are {age_diff} years younger than me.")
else:
    print("We are the same age!")


# Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
""" Enter number one: 4
Enter number two: 3
4 is greater than 3 """
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))

if number_one > number_two:
    print(f"{number_one} is greater than {number_two}.")
elif number_two > number_one:
    print(f"{number_two} is greater than {number_one}.")
else:
    print("Both numbers are the same.")