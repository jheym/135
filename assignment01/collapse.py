def collapse(input):
    a = []
    b = []
    for i in range(0, len(input), 2):
        a.append(input[i])
    for i in range(1, len(input), 2):
        b.append(input[i])
    if len(input) % 2 == 1:
        b.append(0)  # To prepare for zip function
    listsums = [x + y for (x, y) in zip(a, b)]
    return listsums

# Test case (odd digits)
input = [1, 8, 3, 5, 5, 4, 8, 9, 10]
print(collapse(input))
