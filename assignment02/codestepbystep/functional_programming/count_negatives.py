# https://www.codestepbystep.com/problem/view/python/functional/count_negatives

# Write a function named count_negatives that takes a list of integers as a
# parameter and returns how many numbers in the list are negative. For example,
# if the list is [5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6], you should return
# 7.

# Use Python's functional programming constructs, such as list comprehensions,
# map, filter, reduce, to implement your function. Do not use any loops or
# recursion in your solution.



# def count_negatives(nums: list):
#     return len([x for x in nums if x < 0])

def count_negatives(nums: list):
    return len(list(filter(lambda n : n < 0, nums)))

#Test Case
nums = [5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6]
print(count_negatives(nums))
    