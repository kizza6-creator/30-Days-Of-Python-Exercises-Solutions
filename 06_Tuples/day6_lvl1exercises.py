# Create an empty tuple
tpl1 = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Kevin', 'Jordan', 'Chris', 'Alex')
sisters = ('Kelly', 'Chrysi', 'Sophie')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('Grace')
family_members.append('Rosario')
family_members = tuple(family_members)
print(family_members)


