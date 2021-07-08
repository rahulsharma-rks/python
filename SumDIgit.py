#Program to find the sum of digits of a number
n = int(input("Enter Number:"))
sum = 0
rem = 0
while(n != 0):
    rem = n % 10
    sum = sum + rem
    n = n // 10
print("Sum:%d"%sum)
