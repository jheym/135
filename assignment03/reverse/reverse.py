# Reverse.py modified by Justin Heyman (jheyman@csus.edu) for CSC 135 Fall 2022
# Reverses a cons list called List135(), which was developed by Ted Krovetz (tdk@csus.edu)

from List135 import List135

# Reverses the order of a List135 and returns the reversed list.
# [] --> []; [1] --> [1]; [1,2] --> [2,1]; [1,2,3] --> [3,2,1]; etc.
def reverse(xs, acc=List135()):
    if xs.empty():
        return acc
    else:
        return reverse(xs.rest(), acc.add(xs.first()))
 
# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    a = List135().add(3).add(1).add(5).add(2).add(4)
    b = reverse(a)
    print(a)
    print(b)