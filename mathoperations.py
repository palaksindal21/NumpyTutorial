# Mathematical operations in Numpy
# Basic arithmetic operations add subract multiplication division
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])

print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division

#Universal function(ufuncs)-- Functions that operate on element wise.
np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divide(a,b)

#power and modulus
c = np.power(a,2)  #square
d = np.mod(a,2)    #remainder
print(c)
print(d)

#Rounding Functions
e = np.round(a)  #nearest value
f = np.floor(a)  #lower integer
g = np.ceil(a)   #higher integer

#Statistical operations
np.sum(a)   #sum
np.mean(a)  #mean
np.max(a)   #maximum
np.min(a)  #minimum
np.std(a)  #standard deviation

# Trigonometric Functions
np.sin(a)
np.cos(a)
np.tan(a)

#Logarithmic and exponential
np.log(a)   #natural logarithm
np.exp(a)   #e^x

# Square Root & Absolute
np.sqrt(a)   #square root
np.abs(a)    #absolute value

# Axis-Based Operations
np.sum(a, axis=0)  #column wise
# np.sum(a, axis=1)  #row wise

# . Add two NumPy arrays element-wise.
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([11,22,33,44,55])

arr3 = np.add(arr1,arr2)
print("Addition:",arr3)

# Subtract two NumPy arrays element-wise.
arr4 = np.subtract(arr2,arr1)
print("Subtraction:",arr4)

# Multiply two NumPy arrays element-wise.
arr5 = np.multiply(arr1,arr2)
print("Multiplication:",arr5)

# Divide two NumPy arrays element-wise.
arr6 = np.divide(arr2,arr1)
print("Division:",arr6)


# Compute the dot product of two matrices.
ab = np.array([[1,2],
               [3,4]])

cd = np.array([[5,6],
               [7,8]])

arr7 = np.dot(ab,cd)  #dot product
print("Dot product:",arr7)

# Compute the dot product of two matrices.
arr8 = np.sum(ab)
print("Sum:",arr8)

#  Compute the mean of an array.
arr9 = np.mean(cd)
print("Mean:",arr9)

# Compute the median of an array.
arr10 = np.median(ab)
print("Median:",arr10)

# . Compute the standard deviation of an array.
arr11 = np.std(ab)
print("Standard deviation:",arr11)

# Compute the variance of an array
arr12 = np.var(cd)
print("Variance:",arr12)


