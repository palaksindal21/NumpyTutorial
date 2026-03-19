'''
Broadcasting -- Broadcasting allows NumPy to perform operations on arrays of different shapes without actually copying data.
It automatically expands smaller array to match the larger one.

Rules of Broadcasting
Compare shapes from right to left
Two dimensions are compatible if:
They are equal, OR
One of them is 1

1. Scalar Broadcasting-- A single value (scalar) is applied to all elements of an array.
2.1D to 2D Broadcasting (Row-wise) - A 1D array is broadcasted across rows of a 2D array. Values added to each row.
3. Column-wise Broadcasting-- A column vector is broadcasted across columns.    Values added column-wise.
4.Higher-Dimensional Broadcasting- Broadcasting between arrays of different dimensions (e.g., 2D & 3D).NumPy automatically expands dimensions.
5. Broadcasting with Different Shapes (General Case)- Arrays of different shapes are broadcasted based on compatibility rules.


'''

'''
Advanced operations 
1. Vectorized Operations -- Perform operations on entire arrays element-wise without loops.
Arrays (a, b) of same shape or broadcastable.Faster than loops.

2. Fancy Indexing-- Access elements using index arrays or lists.
Parameters-Array,Index list/array

3.Boolean Indexing - Filter elements based on conditions.
Parameters-
Array
Condition (True/False)

4.Reshaping (reshape())--Changes shape of array without changing data.
arameters
New shape (rows, columns)

5.Flattening (flatten())-Converts multi-dimensional array into 1D array.
Parameters
order (optional)

6.Stacking Arrays (vstack, hstack)-Stacking Arrays (vstack, hstack)
Parameters
Tuple of arrays

7. Splitting Arrays (split())-Divides array into multiple sub-arrays.
Parameters
Array
Number of parts


'''
import numpy as np

# 51. Add a scalar value to all elements of an array.
arr1 = np.array([[10,20,30],
                 [11,12,13]])
b = 5
result = arr1 + b
print("add",result)
# 52. Multiply an array by a scalar value.
result2 = arr1*b
print("multiplication",result2)
# 53. Divide all elements of an array by a scalar.
result3 = arr1/b
print("divide",result3)
# 54. Compute the exponential of all elements in an array.
exponent = np.exp(arr1)
print("Exponent",exponent)

# 55. Compute the natural logarithm of all elements in an array.
logarithm = np.log(arr1)
print("Logarithm:",logarithm)

# 56. Compute the sine of all elements in an array.
sine = np.sin(arr1)
print("sin:",sine)

# 57. Compute the cosine of all elements in an array.
cosin = np.cos(arr1)
print("cosine:",cosin)

# 58. Compute the square root of all elements in an array.
squareroot = np.sqrt(arr1)
print("squareroot:",squareroot)

# 59. Compute the absolute value of all elements in an array.
absolute_value = np.absolute(arr1)
print("Absolute value:",absolute_value)

# 60. Find the element-wise maximum of two arrays.
a = np.array([1, 5, 3])
b = np.array([4, 2, 6])
result5 = np.maximum(a,b)
print(result5)

# 1D to 2D Broadcasting (Row-wise)
arr2 = np.array([[1, 2, 3],
              [4, 5, 6]])

arr3 = np.array([10, 20, 30])

print("1D to 2D broadcasting:", arr1+arr2)

# Column-wise Broadcasting

arr4 = np.array([[10],
               [20]])
print("Column wise broadcasting:",arr2+arr4)

# Higher-Dimensional Broadcasting
arr5 = np.array([[1, 2, 3]])
arr6 = np.array([[[10, 20, 30]]])
print("Higher dimensional broadcasting:", arr5+arr6)

# Broadcasting with Different Shapes (General Case)""
arr7 = np.array([[1], [2], [3]])   # shape (3,1)
arr8 = np.array([10, 20, 30])  
print("Broadcasting with different shapes:",arr7+arr8)

# Vectorized Operations
print("Vectorized array:", a+b)

# Reshaping (reshape())
shape = np.array([1,2,3,4])
print("Reshaped array:",shape.reshape(2,2))

# plitting arrays
arr10 = np.array([10,20,30,40,50,60])
print("Split:",np.split(arr10, 2))


