'''LINEAR ALGEBRA OPERATIONS IN NUMPY

1. Creating Arrays (Vectors & Matrices)-- A vector is a 1D array of numbers.
A matrix is a 2D array arranged in rows and columns.

a = np.array([1, 2, 3])          
b = np.array([[1, 2], [3, 4]])   

 2. Matrix Addition & Subtraction--Adding two matrices by adding corresponding elements.
  Subtracting corresponding elements of two matrices.
 A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

add = A + B         
sub = A - B         

Scalar Multiplication-- Multiplying each element of a matrix by a scalar value.
scalar_mult = 2 * A

4. Matrix Multiplication--Product of two matrices where rows of first matrix are multiplied
with columns of second matrix.
Using dot() or @ operator
mat_mult1 = np.dot(A, B)
mat_mult2 = A @ B

 Element-wise Multiplication--Multiplying corresponding elements of two matrices.
 elem_mult = A * B

 6. Transpose of Matrix--Interchanging rows and columns of a matrix.
 transpose = A.T


 7. Determinant of Matrix-- A scalar value that represents certain properties of a square matrix
such as invertibility.
determinant = np.linalg.det(A)

9. Inverse of Matrix--A matrix which when multiplied with the original matrix gives identity matrix.
inverse = np.linalg.inv(A)

10. Eigenvalues and Eigenvectors--Eigenvalues are scalars and eigenvectors are non-zero vectors such that
A*v = λ*v.
eigenvalues, eigenvectors = np.linalg.eig(A)

11. Rank of Matrix--Maximum number of linearly independent rows or columns in a matrix.
rank = np.linalg.matrix_rank(A)

12. Trace of Matrix--Sum of diagonal elements of a square matrix.
trace = np.trace(A)

13. Solving Linear Equations (Ax = B)-Finding vector x such that Ax = B.
A_eq = np.array([[3, 1], [1, 2]])
B_eq = np.array([9, 8])
solution = np.linalg.solve(A_eq, B_eq)

Identity Matrix--A square matrix with 1s on diagonal and 0s elsewhere.
identity = np.eye(3)

15. Zero Matrix and Ones Matrix--Zero matrix: all elements are 0
Ones matrix: all elements are 1
zeros = np.zeros((2, 2))
ones = np.ones((2, 2))

16. Norm of a Vector-Measure of length or magnitude of a vector.
vector = np.array([3, 4])
norm = np.linalg.norm(vector)

Dot Product-- Sum of products of corresponding elements of two vectors.
dot_product = np.dot([1, 2], [3, 4])

 Cross Product--Vector product of two 3D vectors resulting in a vector perpendicular to both.
 cross_product = np.cross([1, 2, 3], [4, 5, 6])

 Reshaping Arrays--Changing the shape of an array without changing its data.
arr = np.array([1, 2, 3, 4])
reshaped = arr.reshape(2, 2)

Concatenation--Joining two or more arrays along an axis.
concat = np.concatenate((A, B), axis=0)

Splitting Arrays--Dividing an array into multiple sub-arrays.
split = np.split(arr, 2)




'''
import numpy as np
a = np.array([1, 2, 3])          
b = np.array([[1, 2], [3, 4]])   

arr = np.array([1, 2, 3, 4])
reshaped = arr.reshape(2, 2)

split = np.split(arr, 2)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

concat = np.concatenate((A, B), axis=0)

add = A + B         
sub = A - B         
scalar_mult = 2 * A

transpose = A.T

cross_product = np.cross([1, 2, 3], [4, 5, 6])

dot_product = np.dot([1, 2], [3, 4])

vector = np.array([3, 4])
norm = np.linalg.norm(vector)

zeros = np.zeros((2, 2))
ones = np.ones((2, 2))

identity = np.eye(3)

A_eq = np.array([[3, 1], [1, 2]])
B_eq = np.array([9, 8])
solution = np.linalg.solve(A_eq, B_eq)


eigenvalues, eigenvectors = np.linalg.eig(A)


trace = np.trace(A)

rank = np.linalg.matrix_rank(A)

vector = np.array([3, 4])
norm = np.linalg.norm(vector)


inverse = np.linalg.inv(A)


determinant = np.linalg.det(A)


A = np.array([[4, 2], [3, 1]])

# 71. Determinant of a square matrix
# Determinant is a scalar value that indicates whether a matrix
# is invertible (non-zero determinant means invertible).

det = np.linalg.det(A)
print("determinant:",det)

# Inverse of a square matrix
inverse = np.linalg.inv(A)
print("Inverse:",inverse)

# 73. Rank of a matrix
rank = np.lingalg.matrix_rank(B)
print("Rank:",rank)

# 74. Eigenvalues of a matrix
eigenvalues = np.linalg.eig(B)[0]
print("Eigen values:",eigenvalues)

# 75. Eigenvectors of a matrix
eigenmatrix = np.linalg.eig(B)[1]
print("eigen matrix:",eigenmatrix)

# 76. Singular Value Decomposition (SVD) -- 
U, S, Vt = np.linalg.svd(B)
print("Singular value decomposition:",U,S,Vt)

# 77. Solve system of linear equations (Ax = B)--Finds vector x such that Ax = B.
A_eq = np.array([[2, 1], [1, 3]])
B_eq = np.array([8, 13])
solve = np.linalg.solve(A_eq, B_eq)
print("Solution:",solve)

# 78. Frobenius norm of a matrix -- Square root of sum of squares of all elements in the matrix.
fro_norm = np.linalg.norm(B, 'fro')
print("Frobenius norm:",fro_norm)

# 79. Trace of a matrix-- Sum of diagonal elements of a square matrix.
trace = np.trace(A)
print("Trace:",trace)

# 80. Cholesky Decomposition--Factorizes a positive-definite matrix into L * Lᵀ
# where L is a lower triangular matrix.
P = np.array([[4, 2], [2, 3]])
cholesky = np.linalg.cholesky(P)














