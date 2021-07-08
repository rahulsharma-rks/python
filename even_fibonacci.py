a = 1
b = 1
c = 0
sum = 0
max = 4000000
while c < 4000000:
    c = a+b
    if c % 2 == 0:
        sum += c
    a = b
    b = c
print(sum)


    
