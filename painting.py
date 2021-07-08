interior = int(input("Enter Number of Interior Walls:"))
exterior = int(input("Enter Number of Exterior Walls:"))

if interior:
    int_wall = []
    for i in range (interior):
        int_wall.append(float(input("Surface Area of Interior Wall:")))

if exterior:
    ext_wall = []
    for i in range(exterior):
        ext_wall.append(float(input("Surface Area of Exterior Wall:")))

if interior < 0 or exterior < 0:
    print("Invalid Input!")
    exit()

if exterior and interior:
    cost = (sum(int_wall)*18+sum(ext_wall)*12)
    print("Total Cost:",cost,"INR")
else:
    if exterior:
        e_cost = sum(ext_wall)*12
        print("Total Exterior Cost:",e_cost,"INR")
    elif interior:
        i_cost = sum(int_wall)*18
        print("Total Interior Cost:",i_cost,"INR")
    else:
        print("Total Estimated Cost: 0 INR")