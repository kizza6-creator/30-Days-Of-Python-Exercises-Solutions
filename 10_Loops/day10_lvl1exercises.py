# Iterate 0 to 10 using for loop, do the same using while loop.
for number in range(11):
    print(number)

i = 0
while i < 11:
    print(i)
    i += 1
print('Loop ends.')

# Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(11, -1, -1):
    print(number)

i = 10
while i >= 0: 
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
n = 1
while n < 8:
    print('#' * n)
    n += 1
print('Right angled triangle completed!')

# Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()


# Print the following pattern:
""" 0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100 """
for number in range(11):
    print(f'{number} x {number} = {number ** 2}')

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in skills:
    print(skill)

# Use for loop to iterate from 0 to 100 and print only even numbers
for number in range(101):
    if number % 2 == 0 and number != 0:
        print(number)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for number in range(101):
    if number % 2 != 0 and number != 0:
        print(number)