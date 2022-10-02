s = [1, -1, 3, 4, 5, 3]

def reduce(f, iter: list, init=None):
    if init is None:
        acc = iter[0]
        for element in iter[1:]:
            acc = f(acc, element)
    else:
        acc = init
        for element in iter:
            acc = f(acc, element)
    return acc    
    
def filter(f, iter: list):
    acc = []
    for element in iter:
        if f(element):
            acc.append(element)
    return acc
        

# Test case
func = lambda a, v : a + 1

# def func(x, y):
    
print(filter(lambda v : v > 0, s))    
print(reduce((lambda a, v : a + 1), s, 0))

a = []
a.append(('A', 'a'))
a.append(('B', 'b'))