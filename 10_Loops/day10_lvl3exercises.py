import countries

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for country in countries.countries:
    if 'land' in country:
        print(country)

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
# Swap elements from both ends moving towards center
for i in range(len(fruits) // 2):
    # Swap elements at position i and -(i+1)
    fruits[i], fruits[-(i+1)] = fruits[-(i+1)], fruits[i]

print(fruits)

# Go to the data folder and use the countries_data.py file.
# Solution to load the countries_data.py file
import json

# Load the data from the uploaded file
with open('countries_data.py', 'r', encoding='utf-8') as file:
    countries_data = eval(file.read())

# Verify it loaded correctly
print(f"Successfully loaded {len(countries_data)} countries")
print(f"First country: {countries_data[0]['name']}")

# What are the total number of languages in the data
all_languages = set()

for country in countries_data:
    for language in country['languages']:
        all_languages.add(language)

print(f"Total number of unique languages: {len(all_languages)}")

# Find the ten most spoken languages from the data
from collections import Counter

# Count how many countries speak each language
language_count = Counter()
for country in countries_data:
    for language in country['languages']:
        language_count[language] += 1

# Get top 10
top_10_languages = language_count.most_common(10)
print("Top 10 most spoken languages:")
for language, count in top_10_languages:
    print(f"{language}: {count} countries")

# Find the 10 most populated countries in the world
# Sort countries by population
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Top 10 most populated countries:")
for i, country in enumerate(sorted_by_population[:10], 1):
    print(f"{i}. {country['name']}: {country['population']:,}")