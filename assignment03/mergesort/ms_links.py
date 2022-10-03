# Sanity tester. This is not a thorough test of your submission. It
# is your responsibility to test thoroughly. The sole purpose of this
# file is to do one test to make sure your submission is callable
# and type-correct

from List135 import List135
from ms2 import merge


def equal135(l1, l2):
    if l1.empty() and l2.empty():
        return True
    elif l1.empty() != l2.empty():
        return False
    else:
        return (l1.first() == l2.first()) and equal135(l1.rest(), l2.rest())


l1 = List135().add(6).add(4).add(3).add(1)
l2 = List135().add(6).add(5).add(2)
result = List135().add(6).add(6).add(5).add(4).add(3).add(2).add(1)
print("Pass" if equal135(merge(l1,l2), result) else "Fail")