def even_odd(num):
    if num % 2 == 0:
        return "{} is Even.".format(num)
    else:
        return "{} is Odd.".format(num)

lst = [2,5,10,89,975,1002]

print(list(map(even_odd, lst)))