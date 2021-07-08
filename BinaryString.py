def append_bits(X,L):
    return [X + element for element in L]

#Recursive function
def generate_bits(n):
    if n == 0:
        return []
    elif  n == 1:
        return  ["0","1"]
    else:
        return (append_bits("0", generate_bits(n - 1))) + (append_bits("1", generate_bits(n - 1)))

n = int(input("Enter Number:"))
print("Binary String of",n,"is :", generate_bits(n))
