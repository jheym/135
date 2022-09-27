# https://www.codestepbystep.com/problem/view/python/functional/total_circle_area

# Write a function named total_circle_area that accepts a list of real numbers
# representing the radii of the circles as a parameter and returns the sum of
# the areas of a group of circles, rounded to the nearest integer. Recall that
# the area of a circle of radius r is π r2. For example, if the list is [3.0,
# 1.0, 7.2, 5.5], your function should return 289. If the list is empty, return
# 0.

# Use Python's functional programming constructs, such as list comprehensions,
# map, filter, reduce, to implement your function. Do not use any loops or
# recursion in your solution.

from math import pi

# def total_circle_area(realnums: list):
#     return round(sum([(math.pi * radius ** 2) for radius in realnums]))

def total_circle_area(realnums: list):
    return round(sum(map(lambda r : pi * r ** 2, realnums)))

print(total_circle_area([3.0, 1.0, 7.2, 5.5]))
    