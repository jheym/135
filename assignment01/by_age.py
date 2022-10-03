def by_age(dict_in: dict[str, int], min_age: int, max_age: int):
    """
    Takes a dictionary with names as keys and ages as values and returns
    a new dictionary with ages as keys and a concatenation of names for that age.
    """
    
    # def by_value(item):    # For sorting by value item in dict.items() (which is a list of tuples)
    #     return item[1]
    
    # Lambda can replace the above helper function since the function body is so short.
    by_value = lambda item: item[1]
   
    new_dict = {}
    for key, value in sorted(dict_in.items(), key=by_value):
        if min_age <= value <= max_age:
            if value in new_dict:
                new_dict[value] = str(new_dict.get(value)) + " and " + str(key)
                continue
            new_dict[value] = key
    return new_dict


# Test Case
dict_in = {
    'Allison': 18,
    'Benson': 48,
    'David': 20,
    'Erik': 20,
    'Galen': 15,
    'Grace': 25,
    'Helene': 40,
    'Janette': 18,
    'Jessica': 35,
    'Marty': 35,
    'Paul': 28,
    'Sara': 15,
    'Stuart': 98,
    'Tyler': 6,
    'Zack': 20
}

print(by_age(dict_in, 18, 60))
