s = [1, 2, 3, 4, 5]

def reduce(f, init=None):
    if init is None:
        acc = s[0]
        for element in s[1:]:
            acc = f(acc, element)
    else:
        acc = init
        for element in s:
            acc = f(acc, element)
    return acc    
    


# Test case
func = lambda a, v : a + 1

# def func(x, y):
    
    
print(reduce((lambda a, v : a + 1), 0))