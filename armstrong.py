num = int(input("Enter Number:"))
arm = 0
temp = num
while temp > 0:
    dig = temp % 10
    arm += dig ** 3
    temp //= 10
if num == arm:
    print(num," is Armstrong Number.")
else:
    print(num," is not Armstrong Number.")