
list1 = [3, 7, 3, -1, 2, 3, 7, 2, 15, 15]
list2 = [-5, 15, 2, -1, 7, 15, 36]

def num_in_common(a,b):
    c = [*set(a)] + [*set(b)]                                      # set() function removes duplicates
    numdupes = len(c) - len([*set(c)])
    return(numdupes)
    

    