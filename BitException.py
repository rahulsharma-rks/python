def binaryNumber(num):
    if num > 1:
        binaryNumber(num // 2)
    print(num % 2, end = '')


num = int(input("Enter Number:"))
#bits = int(input("Enter Number of Bits:"))

#built-in function bin(num)[:2] to convert decimal to binary
#bit = bin(num)[2:]
print(binaryNumber(num))
