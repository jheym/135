# Write a function named all_positive that takes a python list of numbers as a parameter and returns False if any of them are less-than or equal
# to zero, and True otherwise. (This means the empty list should return True too). You will write the function twice. Once here and once in
# another question. Both versions should use higher-order functions and no loops or list-comprehensions to solve the problem. The version you
# will write for this question should use filter to keep either the positive numbers or the non-positive numbers (the choice is yours), and
# then use the len() function to determine the answer.

def all_positive(nums: list):
    t = list(filter(lambda a : a <= 0, nums))
    if len(t) != 0:
        return False
    else:
        return True

# Test case
list1 = [9, 5, 11, 1, 8, 7, 3]
list2 = [6, 5, 0, 1, 1, 2, 8]
list3 = []

print(all_positive(list1))
print(all_positive(list2))
print(all_positive(list3))

