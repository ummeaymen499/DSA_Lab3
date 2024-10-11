def printMatrix(A, starting_index, rows, columns):
    start_row, start_col = starting_index

    for i in range(start_row, start_row + rows):
        for j in range(start_col, start_col + columns):
            print(A[i][j], end=" ")
        print() 

def MatAdd(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

def MatAddPartial(A, B, start, size):
    start_row, start_col = start
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            result[i][j] = A[start_row + i][start_col + j] + B[start_row + i][start_col + j]
    
    return result

def MatMul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result        

def MatMulRecursive(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Divide matrices into 4 submatrices each
    mid = n // 2
    A11, A12, A21, A22 = partition(A)
    B11, B12, B21, B22 = partition(B)
    
    # Recursively compute the submatrices of the result
    C11 = MatAdd(MatMulRecursive(A11, B11), MatMulRecursive(A12, B21))
    C12 = MatAdd(MatMulRecursive(A11, B12), MatMulRecursive(A12, B22))
    C21 = MatAdd(MatMulRecursive(A21, B11), MatMulRecursive(A22, B21))
    C22 = MatAdd(MatMulRecursive(A21, B12), MatMulRecursive(A22, B22))
    
    return combine(C11, C12, C21, C22)

def partition(matrix):
    mid = len(matrix) // 2
    A11 = [row[:mid] for row in matrix[:mid]]
    A12 = [row[mid:] for row in matrix[:mid]]
    A21 = [row[:mid] for row in matrix[mid:]]
    A22 = [row[mid:] for row in matrix[mid:]]
    return A11, A12, A21, A22

def combine(C11, C12, C21, C22):
    top = [C11[i] + C12[i] for i in range(len(C11))]
    bottom = [C21[i] + C22[i] for i in range(len(C21))]
    return top + bottom

def MatMulStrassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    # Divide matrices into 4 submatrices each
    A11, A12, A21, A22 = partition(A)
    B11, B12, B21, B22 = partition(B)
    
    # Strassen's 7 products
    M1 = MatMulStrassen(MatAdd(A11, A22), MatAdd(B11, B22))
    M2 = MatMulStrassen(MatAdd(A21, A22), B11)
    M3 = MatMulStrassen(A11, MatSub(B12, B22))
    M4 = MatMulStrassen(A22, MatSub(B21, B11))
    M5 = MatMulStrassen(MatAdd(A11, A12), B22)
    M6 = MatMulStrassen(MatSub(A21, A11), MatAdd(B11, B12))
    M7 = MatMulStrassen(MatSub(A12, A22), MatAdd(B21, B22))
    
    # Combine submatrices to get the final result
    C11 = MatAdd(MatSub(MatAdd(M1, M4), M5), M7)
    C12 = MatAdd(M3, M5)
    C21 = MatAdd(M2, M4)
    C22 = MatAdd(MatSub(MatAdd(M1, M3), M2), M6)
    
    return combine(C11, C12, C21, C22)

def MatSub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

if __name__=="__main__":
    A = [
    [1, 2],
    [3, 4],
]

B = [
    [5, 6],
    [7, 8],
]

print(MatMulStrassen(A, B))