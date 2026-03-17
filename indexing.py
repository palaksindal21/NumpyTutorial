#Indexing ---Indexing is a way to access individual elements, rows, columns, or slices of a NumPy array. Unlike Python lists, NumPy allows multi-dimensional indexing and fancy indexing.
# Methods of Indexing in NumPy
# A. Basic Indexing (Integer Indexing) --You can access elements using their integer positions.
import numpy as np
arr = np.array([10,20,30,40,50,60,70])   #1D array
print("Index 0:",arr[0])
print("Index 1:",arr[1])
print("Index 5:",arr[5])
print("Index 6:",arr[6])

arr2d = np.array([[1,2,3],
                  [5,6,7],
                  [8,9,4]])
print("Index [0,0]",arr2d[0,0])   #Indexing in 2D array
print("Index [0,1]",arr2d[0,1])
print("Index [1,0]",arr2d[1,0])
print("Index [1,1]",arr2d[1,1])
print("Index [1,2]",arr2d[1,2])

# Slicing (Range Indexing) ---- You can select multiple elements using slices: start:stop:step
print("Slicing in 1D array")
print("from index 1 to 3",arr[1:4])
print("First 3 elements:",arr[:3])
print("Every second element",arr[::2])

print("Slicing in 2D array")
print(arr2d[0:2,1:3])
print("-----------")
print(arr2d[0:1,1:3])
print(arr2d[1:2,1:3])
print(arr2d[2:3,::])


# Boolean Indexing ---You can select elements based on a condition.
print(arr[arr > 25])

print(arr[arr % 4 == 0])

# Fancy Indexing (Integer Array Indexing) -- You can pass a list/array of indices to select multiple elements at once.    arr[rows_array, cols_array]
# NumPy pairs elements position-wise

# It does NOT take full rows/columns. ---Instead, it selects elements like this:

# (row[0], col[0]) → (0, 1)
# (row[1], col[1]) → (2, 2)
arr3 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
rows = np.array([1,2])
cols = np.array([2,2])

print(arr3[rows,cols])

# Using np.where() ---np.where() returns indices of elements that satisfy a condition.

result = np.where(arr > 20)
print(result)
print(arr[result])
result2 = np.where(arr % 3 == 0)
print(result2)
print(arr[result2])

# Ellipsis ... for Multi-Dimensional Arrays

# The ellipsis ... is used to select all preceding dimensions.
arr3d = np.array([[[1,2], [3,4]],
                  [[5,6], [7,8]]])

print(arr3d[..., 0])  


#  Extract the first row from a 2D NumPy array
arr4 = np.array([[12,13,14],
                 [15,16,17],
                 [20,21,22]])
print("First row:",arr4[0])
print("First row:",arr4[0:1])

#  Extract the last column from a 2D NumPy array

print("Last column:",arr4[:,2])
print("Last column:",arr4[:,2:])

# Extract all even elements from a NumPy array.
arr5 = np.array([11,2,12,24,5,64,7,9,10,13])
a = arr5[arr5 % 2 == 0]
print("Even numbers from array:",a)

# Replace all negative values in an array with zero.
arr6 = np.array([10,-1,2,3,-4,-5,60,31,-22])
arr6[arr6 < 0] = 0
print(arr6)

# Assign a new value to a specific index in a NumPy array.
arr5[5] = 45
print(arr5)

#  Find the index of a specific value in a NumPy array.
index = np.where(arr5 == 24)
print(index)

# Use boolean indexing to filter values greater than a given threshold.
threshold = 20
new_arr=arr5[arr5 > threshold]
print(new_arr)


# Use slicing to extract a subarray from a 3x3 matrix.
print("Subarray",arr4[0:2,1:3])

# Get the indices of all nonzero elements in an array.
indices = np.nonzero(arr6)
print(indices)