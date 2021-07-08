#Program to check if a number is a Perfect square or not.
import math
n = int(input("Enter Number:"))
root = math.sqrt(n)
#check sq value of number is equal to number or not
if int(root + 0.5) ** 2 == n:
    print("Perfect Square.")
else:
    print("Not Perfect Square.")