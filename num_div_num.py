
num1 = int(input("Enter Number_1:"))
num2 = int(input("Enter Number_2:"))
num3 = int(input("Enter Number_3:"))
num4 = int(input("Enter Number_4:"))
num5 = int(input("Enter Number_5:"))
chck = int(input("Enter Number to Check Divisibility:"))
num_list = [num1,num2,num3,num4,num5]
res = list(filter(lambda x: (x % chck == 0), num_list));
print("Number divisible by",chck,"are",res);


