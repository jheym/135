import math

def quadratic(a: int, b: int, c: int):
    d = math.sqrt(b*b-4*a*c)
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    print("First root =", x1)
    print("Second root =", x2)


# Test Case    
quadratic(1, -7, 12)