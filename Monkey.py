n = int(input("Enter total number of Monkeys:"))
k = int(input("Enter number of eatable bananas by  single Monkey:"))
j = int(input("Enter number of eatable peanut by  single Monkey:"))
m = int(input("Total Number of Banana:"))
p = int(input("Total Number of Peanut:"))
ate_banana = 0.0
ate_peanut = 0.0
if (n<0 and k<0 or j<0 or m<0 or p<0):
    print("Invalid Input!")
else:
    if (k>0):
        ate_banana = m/k
    elif (j>0):
        ate_peanut = p/j
    n = n-ate_banana-ate_peanut
    print("Total Number of Monkeys left on tree:",n)

