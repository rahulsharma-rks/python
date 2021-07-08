#Generators Vs Iterators

#Iterable
lst = [1,2,3]
for i in lst:
    print(i)

#Iterator
Iterable = iter(lst)
print(Iterable)
for i in Iterable:
    print(i)
print(type(Iterable))

#to create iterator we use iter() keyword and to create generator we use function along with yield
#generator is used to create iterator
#Generator
#yield saves the local variable value and also return local variable value
#generator is faster compared to iterator 
#iterator is much more memory efficient
def square(n):
    for i in range(n):
        yield i**2

print(square(3))

import types,collections
print(issubclass(types.GeneratorType,collections.Iterator))
