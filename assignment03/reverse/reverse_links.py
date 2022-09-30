# Sanity tester. This is not a thorough test of your submission. It
# is your responsibility to test thoroughly. The sole purpose of this
# file is to do one test to make sure your submission is callable
# and type-correct

from List135 import List135
from reverse import reverse


def equal135(l1, l2):
    if l1.empty() and l2.empty():
        return True
    elif l1.empty() != l2.empty():
        return False
    else:
        return (l1.first() == l2.first()) and equal135(l1.rest(), l2.rest())


a = List135().add(3).add(1).add(5).add(2).add(4)
b = List135().add(4).add(2).add(5).add(1).add(3)
print("Pass" if equal135(reverse(a), b) else "Fail")
