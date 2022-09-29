from List135 import List135

# merge sorted List135s xs1 and xs2 into a single sorted List135.
# For example, merge([1,3,4,6], [2,5,6]) --> [1,2,3,4,5,6,6]
def merge(xs1, xs2):
    print(xs1, xs2)
    
    if xs1.empty() and xs2.empty():
        return None
    
    if xs1.empty():
        return xs2
    
    if xs2.empty():   







             

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
    a = List135().add(3).add(1).add(5).add(2).add(4)
    b = mergesort(a)
    print(a)
    print(b) 