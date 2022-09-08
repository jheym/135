####################### Without List Comprehension ########################### 
#
# def matrix_add(A: list, B: list):
#     C = []
#     for i in range(len(A)):
#         C.append([])              # Appends number of rows based matrix A
#         for j in range(len(A[0])):
#             C[i].append(A[i][j] + B[i][j])
# return C   
#
##############################################################################

# ////////////////////////// Zip implementation //////////////////////////////
# def matrix_add(A: list, B: list):
#     C = []
#     tmp = []
#     for z in zip(A, B):
#         for v in list(zip(*z)):
#             tmp.append(sum(v))
#         C.append(tmp.copy())
#         tmp.clear()    
#     zipped = zip(A, B)
#     return C
##############################################################################

#///////////////////// List Comprehension Implementation /////////////////////
def matrix_add(A: list, B: list):
    """Adds two matrices together. Assumes both matrices have the same 
    amount of rows and columns."""
    
    C = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return C  


# Test Cases  
A = [[1, 2], [3, 4], [5, 6]]
B = [[6, 5], [4, 3], [2,1]]

print(matrix_add(A, B))
print(matrix_add([[1, 2, 3], [4, 4, 4]], [[5, 5, 6], [0, -1, 2]]))
print(matrix_add([[7, 2, 9, 3], [-2, 0, 6, 1], [11, 5, 4, 8]], [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(matrix_add([[42]], [[17]]))







