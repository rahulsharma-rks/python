menu = [['Espresso Coffee','Cappuucino Coffee','Latte Coffee'], ['Plain Tea',

'Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea',

'Organic Darjeeling Tea'], ['Hot and Sour Soup','Veg Corn Soup','Tomato Soup',

'Spicy Tomato Soup'], ['Hot Chocolate Drink', 'Badam Drink',

'Badam-Pista Drink']]

m = input("Select from Main Menu-\n Coffee(c) \n Tea(t) \n Soup(s) \n Beverages(b): ")
if m =='c' or m =='t' or m=='s' or m=='b':
    if m == 'c':
        submenu = int(input("Select Coffe:"))
        if submenu in range(3):
            print("Welcome to CCD! \nEnjoy your: {}".format(menu[0][submenu - 1]))
        else:
            print("Invalid Input!")
    elif m == 't':
        submenu = int(input("Select Tea:"))
        if submenu in range(8):
            print("Welcome to CCD! \nEnjoy your: {}".format(menu[1][submenu-1]))
        else:
            print("Invalid Input!")
    elif m == 's':
        submenu = int(input("Select Soup:"))
        if submenu in range(4):
            print("Welcome to CCD! \nEnjoy your: {}".format(menu[2][submenu-1]))
        else:
            print("Invalid Input!")
    elif m == 'b':
        submenu = int(input("Select Beverages:"))
        if submenu in range(3):
            print("Welcome to CCD! \nEnjoy your: {}".format(menu[3][submenu-1]))
        else:
            print("Invalid Input!")
    else:
        print("Invalid Input!")