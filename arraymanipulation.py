# Array manipulation
#creating 2D array

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])  #array with 2 rows and 3 columns

# using zeroes(), ones(), full()

np.zeros((2,3))
np.ones((3,2))
np.full((2,2),7)


#Creating 3d array

arr2 = np.array([
    [[1,2], [3,4]],
    [[5,6], [7,8]]
])
print(arr2)

# using zeroes(), ones(), full()
np.zeros((2,2,2)) #(layers,rows, column)
np.ones((3,2,4))

# Using arange() + reshape()
np.arange(8).reshape(2, 2, 2)

#Reshape a 1D array of 9 elements into a 3x3 matrix
arr3 = np.arange(9)
matrix = arr3.reshape(3,3)
print(matrix)

# Flatten a 2D NumPy array into a 1D array.
flatten_arr = arr.flatten()
print(flatten_arr)   #converts multidimensional array into a 1d array

# Stack two NumPy arrays vertically.
a = np.array([1,2,3])
b = np.array([4,5,6])

vertical = np.vstack((a,b)) #Vertical stacking means joining arrays row-wise (one below another).
print(vertical)

result = np.concatenate((a,b), axis=0)
print(result)

# 14. Stack two NumPy arrays horizontally.
c = np.array([[1,2],
              [3,4]])

d = np.array([[5,6],
              [7,8]])
horizontal = np.hstack((c,d))
print(horizontal)

result2 = np.concatenate((c,d), axis=1)
print(result2)


# 15. Concatenate two 1D NumPy arrays
ab = np.array([10,20,30])
cd = np.array([40,50,60])

result3 = np.concatenate((ab,cd))
print(result3)

# 16. Split an array [1,2,3,4,5,6] into three equal parts.

arr4 = np.array([1,2,3,4,5,6])
split = np.split(arr4,3)  #split(array,section,axis)
print(split)

# 17. Change the data type of a NumPy array from float to int.
# astype()  
arr5 = np.array([1.5, 2.7, 3.9])
new = arr5.astype(int)
print(new)

# 18. Reverse a NumPy array
rev = arr4[::-1]
print(rev)

reverse = np.flip(c)
print(reverse)

#  Find the shape and size of a given NumPy array
print("shape:",c.shape)
print("size:",c.size)

#  Create an array and find its transpose.
trans = d.T
print(trans)

transp = np.transpose(d)