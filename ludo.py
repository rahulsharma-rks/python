import random
choice = input("Do You Want To Roll Dice:")
min = 1
max = 6
if choice == 'Yes' or choice == 'Y' or choice == 'yes' or choice == 'y':
    output = random.randint(min,max)
    print(output)