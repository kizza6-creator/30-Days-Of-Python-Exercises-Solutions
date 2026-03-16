# Write a code which gives grade to students according to theirs scores:
""" 90-100, A
80-89, B
70-79, C
60-69, D
0-59, F """
score = int(input("Enter the student's score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer
# Dictionary with seasons as keys and lists of months as values
seasons = {
    "Autumn": ["September", "October", "November"],
    "Winter": ["December", "January", "February"],
    "Spring": ["March", "April", "May"],
    "Summer": ["June", "July", "August"]
}

# Get user input
month = input("Enter a month: ")

# Find the season
season_found = None
for season, months in seasons.items():
    if month in months:
        season_found = season
        break

if season_found:
    print(f"The season is {season_found}")
else:
    print("Invalid month entered")

# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruit = input("Enter a fruit: ")

if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print(fruits)