# Write a function named all_positive that takes a list of numbers as a parameter and returns False if any of them are negative or zero,
# and True otherwise (this means the empty list should return True too).

# You will write the function twice. Once here and once in another question. Both versions should use higher-order functions and no loops
# or list-comprehensions to solve the problem.

# The version you write for this question should use map to create a list of booleans, and then use reduce to determine the answer.
# To support length 0 and 1 lists, use reduce(func, list, init) with three parameters where the third parameter is the initial value of
# the reduction (ie, func(init, list[0]) is the first invocation of func instead of fun(list[0], list[1]).
from functools import reduce

def all_positive(nums: list):
    t = map(lambda x : True if x > 0 else False, nums)
    return reduce(lambda x, y : True if x and y else False, t, True)

# Test case
list1 = [9, 5, 11, 1, 8, 7, 3]
list2 = [6, 5, 0, 1, 1, 2, 8]
list3 = []

print(all_positive(list1))
print(all_positive(list2))
print(all_positive(list3))