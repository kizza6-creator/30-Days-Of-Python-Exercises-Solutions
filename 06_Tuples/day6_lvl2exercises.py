# Unpack siblings and parents from family_members
family_members = ('Kevin', 'Jordan', 'Chris', 'Alex', 'Kelly', 'Chrysi', 'Sophie', 'Grace', 'Rosario')
siblings = family_members[:family_members.index('Grace')]
parents = family_members[family_members.index('Grace'):]
print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'mango')
vegetables = ('lettuce', 'carrot', 'cucumber')
animal = ('fox', 'lion', 'alpaca')
food_stuff_tp = fruits + vegetables + animal

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = len(food_stuff_lt) // 2
slice_mid = food_stuff_lt[:mid] + food_stuff_lt[mid + 1:]
print(slice_mid)

# Slice out the first three items and the last three items from food_stuff_lt list
new_lt = food_stuff_lt[3:-3]
print(food_stuff_lt)
print(new_lt)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)
