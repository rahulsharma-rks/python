num1 = int(input("Enter number_1:"))
num2 = int(input("Enter number_2:"))
temp1 = num1
temp2 = num2
while  temp2 != 0:
    t = temp2
    temp2 = temp1 % temp2
    temp1 = t
hcf = temp1
lcm = (num1*num2)/hcf 
print("HCF:",hcf)
print("LCM:",lcm)
