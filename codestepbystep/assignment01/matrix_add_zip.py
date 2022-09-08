def matrix_add(A: list, B: list):
    pass





# Test Cases  
A = [[1, 2], [3, 4], [5, 6]]
B = [[6, 5], [4, 3], [2,1]]

# zipped = list(zip(A, B))
# a = []
# # print(list(zipped))

#  a = [map(sum, zip(*t)) for t in zip(A, B)]
    
a = []
tmp = []

for z in zip(A, B):
    for v in list(zip(*z)):
        tmp.append(sum(v))
    a.append(tmp.copy())
    tmp.clear()

    
    
print(a)





