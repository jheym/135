def generate_odds():
    return (i for i in range(20) if i % 2 != 0)


# Test case
# Note the return value needs the unpacking operator or else it prints a generator object address
print(*generate_odds())