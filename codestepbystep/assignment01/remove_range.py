def remove_range (n: set, min: int, max: int):
    rm = {m for m in n if min <= m <= max}          # This is called a set comprehension
    for i in rm:
        n.remove(i)
    
my_set = {3, 17, -1, 4, 9, 2, 14}

print(remove_range(my_set, 1, 10))