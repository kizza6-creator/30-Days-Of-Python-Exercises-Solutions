#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
    
print(add_two_numbers(2,3))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    pi = 3.14
    area = pi * (radius * radius)
    return area
    
print(area_of_circle(3))

#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum = 0
    for num in nums:
        try:
            int(num)
            sum += num
        except ValueError:
            return "Invalid data type, must all be integers."
    return sum

print(add_all_nums(1, 3, 5, 10))

#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return f"{celsius} degree celsius equals {fahrenheit} degree fahrenheit."
    
print(convert_celsius_to_fahrenheit(32))

#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    season_dict = {
        'Summer': ['December', 'January', 'February'],
        'Autumn': ['March', 'April', 'May'],
        'Winter': ['June', 'July', 'August'],
        'Spring': ['September', 'October', 'November']
    }
    
    for key in season_dict:
        if month in season_dict[key]:
            return key
            
    return "Ensure correct spelling and capitalisation. Ex: 'December'"
    
print(check_season('Julyy'))

#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)
        
lst = ['December', 'January', 'February']
print_list(lst)

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    rvs_lst = []
    for item in lst:
        rvs_lst.insert(0, item)
        
    return rvs_lst

print(reverse_list(lst))


def reverse_list_fast_manual(lst):
    rvs_lst = []
    for i in range(len(lst) - 1, -1, -1):
        rvs_lst.append(lst[i])   # append is amortized O(1)
    return rvs_lst  

print(reverse_list_fast_manual(lst))

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    lst_upper = []
    for word in lst:
        lst_upper.append(word.upper())
    
    return lst_upper
    
print(capitalize_list_items(lst))

#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    if item not in lst:
        lst.append(item)
    
    return lst
    
print(add_item(lst, 'April'))

#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
        
    return lst
    
print(remove_item(lst, 'April'))



