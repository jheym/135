# max_value = int(input("Max value? "))
# a = 0
# b = 1
# c = 0
# nums = [0]
# while c < max_value:
#      c = a + b
#      nums.append(c)
#      a = b
#      b = c
# print(*nums, sep=', ')
     


def max_fibonacci(max_val):
    f = [0, 1]
    a, b = (0, 1)
    while f[-1] <= max_val:
        f.append(f[a] + f[b])
        a += 1; b += 1
    f.pop()
    return f

print("This program lists the Fibonacci sequence.")
f = max_fibonacci(int(input("Max value? ")))
print(*f, sep=', ')
    



     
     