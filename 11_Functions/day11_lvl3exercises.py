#Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    
    nums = range(2, n)
    for number in nums:
        if n % number == 0:
            return False
    
    return True

print(is_prime(19))

#Write a functions which checks if all items are unique in the list.
# Time Complex: O(n*2) & Space Complex: O(1)
def unique_list(nums):
    if len(nums) <= 1:
        return True
        
    for first, n in enumerate(nums):
        for second in range(first + 1, len(nums)):
            if n == nums[second]:
                return False
    
    return True
    
nums = [1, 2, 3, 4, 4]
print(unique_list(nums))

# Hash-based solution. Time Complex: O(n) & Space Complex: O(n)
def all_unique(nums):
    seen = set()
    for x in nums:
        if x in seen:      
            return False   
        seen.add(x)       
    return True           

print(all_unique(nums))

#Write a function which checks if all the items of the list are of the same data type.
def same_type(lst):
    for item in lst:
        if type(item) != type(lst[0]): #Comparing with just the first element as is satisfies whether all items are of the same type.
            return False
    return True

lst = [1, 3, 5, 6, '7']    
print(same_type(lst))
