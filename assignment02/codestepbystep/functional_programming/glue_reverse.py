# https://www.codestepbystep.com/problem/view/python/functional/glue_reverse

# Write a function called glue_reverse that accepts a list of strings as its
# parameter and returns a single string consisting of the list's elements
# concatenated together in reverse order. For example, if the list stores
# ["the", "quick", "brown", "fox"], you should return "foxbrownquickthe". If
# the list is empty, return an empty string, "".

# Use Python's functional programming constructs, such as list comprehensions,
# map, filter, reduce, to implement your function. Do not use any loops or
# recursion in your solution.



# def glue_reverse(wordlist: list):
#     return ''.join([*reversed(wordlist)])

from functools import reduce


def glue_reverse(s: list):
    # y + x reverses the words and '' is the initializer which is optional, but
    # needed in this case
    return reduce((lambda x, y : y + x), s, '')  
 
          
    


#Test Case
stuff = ['the', 'quick', 'brown', 'fox']
print(glue_reverse(stuff))