# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_st = set(age)
print(len(age)) #8
print(len(age_st)) #5

# Explain the difference between the following data types: string, list, tuple and set
# string: A string is an immutable sequence of characters. - can be letters, numbers etc.
# list: A list is an ordered, indexed, mutable sequence that can hold elements of different types.
# tuple: A tuple is an ordered, indexed, immutable sequence.
# set: A set is a mutable, unordered collection of unique, immutable elements.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_clean = sentence.replace(".", "")
sentence_lt = sentence_clean.split()
sentence_st = set(sentence_lt)
print(sentence_st)
print("Total words:", len(sentence_lt))
print("Unique words:", len(sentence_st))



