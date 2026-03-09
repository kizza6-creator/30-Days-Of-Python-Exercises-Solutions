#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    if number <= 0:
        return "Must be an integer greater than zero."
    
    numbers = range(number+1) #+ 1 to include 100 in range list. 
    evens = 0
    odds = 0
    
    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    return f"""the number of odds are {odds}. 
the number of evens are {evens}."""
              
print(evens_and_odds(-1))

#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n == 0: # Base case
        return 1
    else: # Recursive case
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120

def factorial_iterative(n):
    if n == 0:
        return 1
        
    result = 1
    for num in range(1, n + 1):
        result *= num
    
    return result

print(factorial_iterative(6))

#Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(arr):
    if len(arr) == 0:
        return "The array is empty."
    
    return "The array is not empty."
    
numbers = list(range(0))
print(is_empty(numbers))

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(nums):
    sum = 0
    
    for n in nums:
        sum += n
    
    mean = sum / len(nums)
    return mean

nums = [6, 7, 3, 5]
print(calculate_mean(nums))

def calculate_median(nums):
    sorted_nums = sorted(nums)
    mid = len(sorted_nums) // 2
    
    if len(sorted_nums) % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    
print(calculate_median(nums))

def calculate_range(nums):
    pass

#Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name="Guest"):
    return f"Hello, {name}!"
    
print(greet())
print(greet("Kieren"))

#Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
def show_args(**args):
    for k, v in args.items():
        print(f"Received: {k}: {v}")
        
show_args(name="Kieren", age=25, city="Sydney")