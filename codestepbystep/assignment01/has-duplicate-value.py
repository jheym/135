# Returns true if the sizeof UNIQUE elements in each list (keys, values) are different
# This works because there cannot be duplicate keys in a python dictionary anyways
def has_duplicate_value(names: list):
    if len(set(names.keys())) != len(set(names.values())):
        return True
    else:
        return False
    
