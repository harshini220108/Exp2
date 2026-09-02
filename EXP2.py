import numpy as np
# An exemple array
arr = np.array([[-1, 2, 0, 4],
[4, -0.5, 6, 0],
[2.6, 0, 7, 8],
[3, -7, 4, 2.0]])
# Slicing array
temp = arr[:1, ::1]
print ("Array with first 2 rows and alternate columns(0 and 2):\n", temp)
# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print ("\nElements at indices (0, 3), (1(, 2), (2, 1),(3, 0):\n", temp)
# boolean array indexing example
cond = arr > 0 # cond is a boolean array
temp = arr[cond]
print ("\nElements greater than 0:\n", temp)
arr = np.array([[1, 2, 3], [4, 5, 6]])
transposed_arr = np.transpose(arr)
print("Original array:\n", arr)
print("Transposed array:\n", transposed_arr)
arr2 = np.array([[1, 5, 6],
[4, 7, 2],
[3, 1, 9]])
b=arr2.flatten()
print("flatten array",b)
k=arr2.reshape(1,9)
print("reshape array",k)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.size)
aa = np.random.randint(((1,10),(11,20),(2,5)))
aa
F=np.arange(1,26).reshape(5,5)
F
a =  np.arange(4)
print("Dimensions in _1darr are: ", a)