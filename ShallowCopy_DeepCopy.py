#collection of objects are mutable
# =
#refers same memory location
lst1 = [1,2,3,4]
lst2 = lst1
print(lst2)
lst2[1] = 10
print(lst2)
print(lst1)

#copy(shallow copy)
#refers different memory location
lst1 = [1,2,3,4]
lst2 = lst1.copy()
print(lst2)
lst2[1] = 100
print(lst2)
print(lst1)

#nested shallow copy
lst1 = [[1,2,3,4],[5,6,7]]
lst2 = lst1.copy()
print(lst2)
lst2[1][1] = 1000
print(lst2)
print(lst1)

lst1.append([10,12,15,16])
print(lst1)
print(lst2)

#deep copy
import copy
lst_1 = [1,2,3,4]
lst_2 = copy.deepcopy(lst_1)
print(lst_2)
lst_2[1]=55
print(lst_2)
print(lst_1)

lst_1 = [[1,2,3,4],[5,6,7],[10,11,12]]
lst_2 = copy.deepcopy(lst_1)
print(lst_1)
print(lst_2)
lst_2[1][1]= 60
print(lst_1)
print(lst_2)