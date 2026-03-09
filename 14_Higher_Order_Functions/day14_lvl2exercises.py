countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Fiji']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list
def make_uppercase(word):
    return word.upper()

uppercase_country_list = map(make_uppercase, countries)
print(list(uppercase_country_list))

# Use map to create a new list by changing each number to its square in the numbers list
def square(n):
    return n ** 2

squared_nums = map(square, numbers)
print(list(squared_nums))

# Use map to change each name to uppercase in the names list
uppercase_names = map(make_uppercase, names)
print(list(uppercase_names))

# Use filter to filter out countries containing 'land'.
def land_check(word):
    if 'land' in word:
        return True
    return False

land_countries = filter(land_check, countries)
print(list(land_countries))

# Use filter to filter out countries having exactly six characters.
def six_char_check(word):
    if len(word) == 6:
        return True
    return False
    
six_char_countries = filter(six_char_check, countries)
print(list(six_char_countries))

# Use filter to filter out countries containing six letters and more in the country list.
def six_or_more_char_check(word):
    if len(word) >= 6:
        return True
    return False

six_plus_char_countries = filter(six_or_more_char_check, countries)
print(list(six_plus_char_countries))

# Use filter to filter out countries starting with an 'E'. 
def is_start_e(word):
    if word[0] == 'E':
        return True
    return False
    
e_countries = filter(is_start_e, countries)
print(list(e_countries))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
def is_even(number):
    if number % 2 == 0:
        return True
    return False

square_nums = map(square, numbers)
even_squared = filter(is_even, square_nums)
print(list(even_squared))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    string_lst = [item for item in lst if isinstance(item, str)]
    return string_lst

str_and_nums = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham', 1, 2, 3, 4, 5]
print(get_string_lists(str_and_nums))

# Use reduce to sum all the numbers in the numbers list.
# pass as no reduce module. 

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# pass as no reduce module. 

# Declare a function called categorize_countries that returns a list of countries with some common pattern.

