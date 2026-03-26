# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0 
for number in range(101):
    sum += number
print(f'The sum of all numbers is {sum}')

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0 
for number in range(1, 101):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')