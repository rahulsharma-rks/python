def binaryDecimal(n):
    if n > 1:
        binaryDecimal(n // 2)
    print(n % 2,end = " ")

if __name__ == '__main__':
    val = int(input("Enter Number:"))
    binaryDecimal(val)
