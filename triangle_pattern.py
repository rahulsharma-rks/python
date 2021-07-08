a = int(input("Enter Number:"))

# i loop for range(height) of the triangle
# first j loop for printing space ' '
# second j loop for printing stars '*'

for i in range(a):
    for j in range((a - i) -1):
        print(end=" ")
    for j in range( i + 1):
        print("*",end=" ")
    print()
