# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Intel', 'Nvidia', 'Netflix', 'Salesforce'])

# Remove one of the companies from the set it_companies
it_companies.remove('Twitter')
it_companies.discard('IBM')
it_companies.pop() #random deletion. 
print(it_companies)

# What is the difference between remove and discard
# remove() will raise an error if an item does not exist in the set whereas discard() will not --> provides us the option to impose strict or non-strict rules in our program.
it_companies.discard('IBM')