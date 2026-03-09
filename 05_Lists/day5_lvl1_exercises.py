# Declare an empty list
empty_lst = []

# Declare a list with more than 5 items
lst = ['banana', 'mango', 'apple', 'orange', 'strawberry', 'pear']

# Find the length of your list
print(len(lst))

# Get the first item, the middle item and the last item of the list
mid = (len(lst) - 1) // 2
print(lst[0])
print(lst[mid])
print(lst[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
personal = ['Kieren', 25, '172cm', True, 'XX Melbourne City']
print(personal)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
mid = (len(it_companies) - 1) // 2
print(it_companies[0]) #First
print(it_companies[mid]) #Middle
print(it_companies[-1]) #Last

# Print the list after modifying one of the companies
it_companies[0] = 'Nvidia'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Samsung')
print(it_companies)

# Insert an IT company in the middle of the companies list
mid = (len(it_companies) - 1) // 2
it_companies.insert(mid, 'Oppo')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = it_companies[3].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
sentence = '#;  '.join(it_companies)
print(sentence)

# Check if a certain company exists in the it_companies list.
print('Facebook' in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse = True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[3:])

# Slice out the last 3 companies from the list
print(it_companies[:-3])

# Slice out the middle IT company or companies from the list
mid = (len(it_companies) - 1) // 2
print(it_companies[mid])
print(it_companies[:mid] + it_companies[mid + 1:])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
mid = (len(it_companies) - 1) // 2
it_companies.pop(mid)

# Remove the last IT company from the list
it_companies.pop(-1)

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end
print(full_stack.index('Redux')) #4
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)
