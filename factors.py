num = int(input("Enter Number:"))
count = 0
for i in range(2, num - 1):
    if num % i ==0:
        print(i)
        i += 1
        count += 1
if  count == 0:
    print("Prime Number.")
