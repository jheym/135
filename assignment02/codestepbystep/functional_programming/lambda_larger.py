# Define a lambda expression named f that accepts two integer parameters and
# returns the larger of the two; for example, if passed 4 and 11, it would
# return 11. Do not write an entire function; just write a statement of the
# form: `f = lambda parameters: expression` 

f = lambda a, b: max(a, b)

# Test Case
print(f(5, 10))