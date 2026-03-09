countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explain the difference between map, filter, and reduce.
"""
map(function, iterable): Map function will apply the parameter function across all elements included in the iterable object. 
filter(function, iterable): Filter function returns only the elements from the iterable which are classified as 'True' as per the parameter function. - Parameter function must return boolean.  
reduce(function, iterable): Similar to how map function operates however rather than returning an iterable, instead ir returns a single value (conjoined from all operations across all elements).
"""

# Explain the difference between higher order function, closure and decorator
"""
higher order function: 
closure: A closure is created by nesting a function inside another encapsulating function and then returning the nested inner function.
decorator: A decorator is a design pattern in Python that is usually called before definition of a function which allows a user to add new functionality to an existing object without modifying its structure.
"""

# Define a call function before map, filter or reduce. 
def square(x): #function for map & reduce.
    return x ** 2

def is_even(x): #function for filter
    if x % 2 == 0:
        return True
    return False
    
squared_list = map(square, numbers)
print(list(squared_list))
even_list = filter(is_even, numbers)
print(list(even_list))
#squared_number = reduce(square, numbers) #functools module needs to be imported.
#print(squared_number)

# Use for loop to print each country in the countries list.
for country in countries:
    print(country)
    
# Use for to print each name in the names list.
for name in names:
    print(name)
    
# Use for to print each number in the numbers list.
for number in numbers:
    print(number)

number_list = [n for n in numbers] #list comprehension practice.
print(number_list)


