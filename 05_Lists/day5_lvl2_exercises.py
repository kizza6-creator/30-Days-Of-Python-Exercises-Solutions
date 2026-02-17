# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
print(max(ages))
print(min(ages))

# Add the min age and the max age again to the list
ages.append(max(ages))
ages.append(min(ages))
print(ages)

# Find the median age (one middle item or two middle items divided by two)
mid = (len(ages) - 1) // 2
print(ages[mid])

# Find the average age (sum of all items divided by their number)
total = sum(ages)
avg_age = total / len(ages)
print(avg_age)

# Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method
min_avg_range = abs(min(ages) - avg_age)
max_avg_range = abs(max(ages) - avg_age)
print(min_avg_range >= max_avg_range)

# Find the middle country(ies) in the countries list
import countries
countries_list = countries.countries
mid = (len(countries_list) - 1) // 2
print(countries_list[mid])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
left_half = countries_list[:mid]
right_half = countries_list[mid:]
print(left_half)
print(right_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
china, russia, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(china)
print(russia)
print(usa)
print(scandic)