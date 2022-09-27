   
# Define a lambda expression named f that accepts two string parameters 
# representing a first and last name and concatenates them together to return 
# a string in "Last, First" format. For example, if passed "Cynthia" and "Lee", 
# it would return "Lee, Cynthia". Do not write an entire function; just write a
# statement of the form: `f = lambda paramaters: expression`

f = lambda fname, lname: str(lname) + ', ' + str(fname)

# Test Case
print(f("Cynthia", "Lee"))