# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
joined_string = ' '.join(words)
print(joined_string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
words = ['Coding', 'For', 'All']
joined_string = ' '.join(words)
print(joined_string)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company.index('F'))
print(company[7:]) #Via slicing
print(company.strip('Coding ')) #Via using strip function. 

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.rindex('Coding'))
print(company.find('Coding'))
print(company.rfind('Coding'))
print(company.count('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
string = "Python for Everyone"
print(string.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(", "))

# What is the character at index 0 in the string Coding For All.
print(company[0]) #C

# What is the last index of the string Coding For All.
print(company[-1]) #l

# What character is at index 10 in "Coding For All" string.
print(company[10]) # ' '

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = "Python For Everyone"
acronym = []
for i in range(len(string)):
    if i == 0:
        acronym.append(string[i])
    elif string[i] == " ":
        acronym.append(string[i + 1])

print("".join(acronym)) #PFE
    
# Create an acronym or an abbreviation for the name 'Coding For All'
company = "Coding For All"
acronym = ''.join(word[0] for word in company.split()) #Cleaner method for creating acronym.
print(acronym)  # CFA

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = "Coding For All People."
print(string.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction.'
print(sentence.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.replace(' because because because', ''))

# Does 'Coding For All' start with a substring Coding?
print(company.startswith('Coding')) #True

# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding')) #False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip())

# Which one of the following variables return True when we use the method isidentifier():
string1 = '30DaysOfPython'
string2 = 'thirty_days_of_python'
print(string1.isidentifier()) # False
print(string2.isidentifier()) # True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_lib))

# Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
"""
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following:
"""
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""
radius = 10
area = 3.14 * radius ** 2
sentence = "The area of a circle with radius {} is {} meters square".format(str(radius), str(area))
print(sentence)

# Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""
a = 8
b = 6
print(f"""
{a} + {b} = {a + b}
{a} - {b} = {a - b}
{a} * {b} = {a * b}
{a} / {b} = {a / b:.2f}
{a} % {b} = {a % b}
{a} // {b} = {a // b}
{a} ** {b} = {a ** b}
""")
