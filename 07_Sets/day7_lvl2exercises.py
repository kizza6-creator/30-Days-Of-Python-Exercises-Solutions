# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
joined_st = A.union(B)
print(joined_st)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))
print(B.issuperset(A))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
st1 = A | B
st2 = B | A
print(st1)
print(st2)

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del st1, st2

