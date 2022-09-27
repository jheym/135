# **From Dr. Krovetz:** The following code passes the print_stars tester at
# https://www.codestepbystep.com/problem/view/python/recursion/print_stars but
# is not tail-recursive.

    # def stars(n):
    #     if (n==0):
    #         return ""
    #     else:
    #         return "*" + stars(n-1)

    # def print_stars(n):
    #     print(stars(n))

# Rewrite the stars function to be tail-recursive and submit the tail-recursive
# pair of functions to Code-Step-By-Step. Note: This will require using an
# accumulator in stars (ie, def stars(n, acc):) as seen in class with the
# factorial example.
###############################################################################
# **From Codestepbystep:** Write a recursive function named print_stars that
# accepts an integer parameter n and prints n occurrences of the "*" character
# to the console. For example, the call of print_stars(5) should print ***** .
# Do not use loops or auxiliary data structures; solve the problem recursively.
# You may assume that the value passed is non-negative. 

def stars(n, acc = ""):
    if n == 0:
        return acc
    else:
        acc += "*"
        return stars(n-1, acc)
    
def print_stars(n: int):
    print(stars(n))

    
print(stars(4))

