#Program to print Fibonacci series upto n numbers.
def fibonacci():
    n = int(input("Enter Number:"))
    i = 1
    if n == 0:
        fib = [0]
    elif  n == 1:
        fib = [1]
    elif n == 2:
        fib = [1,1]
    elif  n > 2:
        fib = [1,1]
        while i < (n - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
        return fib


print(fibonacci())
input()

    
