# https://www.codestepbystep.com/problem/view/python/functional/largest_even

# Write a function named largest_even that takes a list of integers as a
# parameter and returns the largest even number from a list of integers. An
# even integer is one that is divisible by 2. For example, if the list is [5,
# -1, 12, 10, 2, 8], your function should return 12. You may assume that the
# list contains at least one even integer.

# Use Python's functional programming constructs, such as list comprehensions,
# map, filter, reduce, to implement your function. Do not use any loops or
# recursion in your solution.

def largest_even(nums: list):
    return max([i for i in nums if i % 2 == 0])

print(largest_even([5, -1, 12, 10, 2, 8]))