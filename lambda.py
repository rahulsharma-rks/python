"""A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
lambda arguments : expression

Single Expression
"""
"""x = lambda a : a * 5
print(x(5))"""

"""y = lambda a,b : a * b
print(y(5,6))"""

"""def my_fun(n):
    return lambda a : a * n

mydoubler = my_fun(2)
mytripler = my_fun(3)
print(mydoubler(11))
print(mytripler(10))
"""
even = lambda a:a%2==0
print(even(5))
