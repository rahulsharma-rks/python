"""def even_odd(num):
    if num % 2 == 0:
        return True
        """


lst = [2,5,10,89,975,1002.1865,12]

#print(list(filter(even_odd,lst)))

print("FILTER")
print(list(filter(lambda num:num%2==0,lst)))

print("MAP")
print(list(map(lambda num:num%2==0,lst)))



