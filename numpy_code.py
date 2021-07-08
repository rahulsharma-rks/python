import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#ndim tells us how many dimenstions does array has.
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Array Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('3rd element on 2nd dim: ', arr[1, 2])

#Slicing
#Slice elements from index 1 to index 5 from the following array.
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Iteration
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

#Join
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

#Split
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

#Search
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#Sort
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))