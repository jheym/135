# ms.py Modified by Justin Heyman (jheyman@csus.edu) for CDC 135 Fall 2022
# Implements mergesort

from List135 import List135

# merge sorted List135s xs1 and xs2 into a single sorted List135.
# For example, merge([1,3,4,6], [2,5,6]) --> [1,2,3,4,5,6,6]
def merge(xs1, xs2):
    if xs1.empty() and xs2.empty(): # 1st Base Case
        return List135()
    if xs1.empty() or xs2.empty():  # 2nd Base Case
        if xs1.empty():
            return xs2
        else:
            return xs1
    else:
        if xs1.first() < xs2.first():
            t1 = List135().add(xs1.first())
            t2 = merge(xs1.rest(), xs2)
        else:
            t1 = List135().add(xs2.first())
            t2 = merge(xs1, xs2.rest())
        return t2.add(t1.first())
         

# Tail-recursive accumulator algorithm that splits xs elements
# between xs1 and xs2 by alternating between them. xs1 and xs2
# are accumulators that both get initially set to empty List135s.
def split(xs, xs1=List135(), xs2=List135()):
    if xs.empty():
        return (xs1, xs2)
    else:
        return split(xs.rest(), xs2, xs1.add(xs.first()))

def mergesort(xs):
    if xs.empty() or xs.rest().empty():
        return xs
    else:
        (xs1, xs2) = split(xs)
        return merge(mergesort(xs1), mergesort(xs2))

 
# The following is a trick to make this testing code be ignored
# when this file is being imported, but run when run directly
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    a = List135().add(3).add(1).add(8).add(5).add(2).add(4).add(9).add(3).add(1).add(6)
    b = mergesort(a)
    print(a)
    print(b) 