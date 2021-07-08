print("Welcome To Pizza Parlour")
size = input("Enter Size(S/M/L) of Pizza:")
add_pepperoni = input("Do You Want Extra Pepperoni? Y/N:")
extra_cheese = input("Do You Want Extra Cheese? Y/N:")
bill = 0
if size == "S":
    bill = 15
    print("Cost of Small Pizza: 15$")
elif size == "M":
    bill = 20
    print("Cost of Medium Pizza: 20$")
else:
    bill = 25
    print("Cost of Large Pizza: 25$")
if add_pepperoni == "Y":
    bill += 2

if extra_cheese == "Y":
    bill += 1

print(f"Your Final Bill is {bill} $")