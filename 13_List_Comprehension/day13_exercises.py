#Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [n for n in numbers if n <= 0]
print(negative_numbers)

#Flatten the following list of lists of lists to a one dimensional list:
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
one_dimension = [n for row in list_of_lists for n in row]
print(one_dimension)

#Using list comprehension create the following list of tuples: 
result = [(n, *[n**k for k in range(0, 6)]) for n in range(11)] # Use of '*' expands(unpacks) the list into the surrounding tuple --> (n, 1, n**1, n**2...n**5)
print(result)

#Flatten the following list to a new list:
#Output:
#[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [[item[0].upper(), item[0].upper()[:3], item[1].upper()] for lst in countries for item in lst]
print(new_list)

#Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_dict = [{'country': item[0].upper(), 'city': item[1].upper()} for country in countries for item in country]
print(new_dict)

#Change the following list of lists of concatenated strings.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
conc_string = [f"{name[0]} {name[1]}" for lst in names for name in lst]
print(conc_string)

#Write a lambda function which can solve a slope or y-intercept of linear functions. 
# m = (Y(1) - Y(2)) / (X(1) - X(2))
# y = mx + b

slope = lambda x1, y1, x2, y2: None if x1 == x2 else (y1 - y2) / (x1 - x2)
y_intercept = lambda m, x1, y1: None if m is None else (y1 - m * x1)

# Example
m = slope(2, 4, 2, 10)         # vertical line -> None
b = y_intercept(m, 2, 4)       # None (no y-intercept)
print(m, b)                    # None, None

m2 = slope(2, 4, 4, 5)         # 0.5
b2 = y_intercept(m2, 2, 4)     # 3.0
print(m2, b2)                  # 0.5 3.0
