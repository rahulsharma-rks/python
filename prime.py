#Program to check if a number is prime. Print square root if the number is prime
#import math
a = int(input("Enter Number:"))

#Prime Number are greter than 1
if a > 1:
    for i in range(2, a):
        if (a % i) == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
            break
else:
    print("Not Prime")